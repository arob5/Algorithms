#
# grid_cell_class.py
# Class implementations for a grid (which is a container for cells) and a cell (which fits into the container grid) 
# Last Modified: 8/14/2017
# Modified By: Andrew Roberts
#

import png

class Cell(): 
	def __init__(self, row, column):
		self.row = row
		self.column = column
		self.neighbors = {"north": None, "south": None, "east": None, "west": None}
		self.links = [] 

	def link(self, cell, bidir=True):
		"""Forms a link (passage) between two cells

		Args:
		    cell (Cell object): Cell to link with
		    bidir (bool): Bidirectional link	
		"""
		self.links.append([cell.row, cell.column])
		if bidir:
			cell.link(self, False)
	
	def unlink(self, cell, bidir=True):
		"""Unlinks two cells

		Args:
		    cell (Cell object): Cell to unlink from
		    bidir (bool): Bidirectional link	
		"""	
		self.links.remove([cell.row, cell.column]) 
		if bidir:
			cell.unlink(self, False)

	def is_linked(self, cell):
		""" Checks if two cells are linked

		Args:
            	    cell (Cell object): Cell to check if linked to

		Returns:
		    bool: True if linked, False otherwise
		"""
		return [cell.row, cell.column] in self.links

	def current_neighbors(self, dir=["north", "south", "east", "west"]):
		""" Returns list of neighbor cells
		
		Args:
		    dir (list): List of directions to consider; default: all directions

		Returns:
		    list: Neighbor cells (Where neighbor exists and direction is in dir)

		"""
		n = self.neighbors
		return [n[key] for key in n if n[key] is not None and key in dir]

class Grid():
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		
		self.grid = self.prepare_grid()	
		self.configure_cells()			
		
	def prepare_grid(self):
		""" Returns 2-D grid of Cell objects"""
		return [[Cell(i,j) for j in range(self.columns)] for i in range(self.rows)]	

	def configure_cells(self):
		"""Updates neighbor dictionaries of each Cell object in grid"""
		for i in range(self.rows):
			for j in range(self.columns):
				self.cell_at(i, j).neighbors["north"] = self.cell_at(i-1, j)
				self.cell_at(i, j).neighbors["south"] = self.cell_at(i+1, j)
				self.cell_at(i, j).neighbors["east"] = self.cell_at(i, j+1)
				self.cell_at(i, j).neighbors["west"] = self.cell_at(i, j-1)
	
	def cell_at(self, row, col):
		"""Returns Cell object at (row, col) if in bounds, else returns None"""
		try:
			return self.grid[row][col]
		except IndexError:
			return None

	def row_at(self, row):
		"""Returns row at index 'row' if in bounds, else raises Exception"""
		try:
			return self.grid[row]
		except IndexError:
			print("Row out of bounds")

	def column_at(self, col):
		"""Returns col at index 'col' if in bounds, else raises Exception"""
		try:
			return [row[col] for row in self.grid]
		except IndexError:
			print("Column out of bounds")

	def print_grid(self):
		"""Prints grid to console using ASCII characters"""
		top_and_bottom_wall = "+" + ("---+" * self.columns)

		print(top_and_bottom_wall)
		for i, row in enumerate(self.grid):
			if i != 0:
				self.print_top_wall(row)	
			self.print_bottom_wall(row)		
		print(top_and_bottom_wall)	

	@staticmethod
	def print_top_wall(row):
		"""Helper function for print_grid, prints top part of walls"""
		print("+", end="")

		for cell in row:
			if cell.is_linked(cell.neighbors["north"]):
				print("   +", end="")
			else:
				print("---+", end="")
		print("")

	@staticmethod
	def print_bottom_wall(row):
		"""Helper function for print_grid, prints bottom part of walls"""
		print("|", end="")

		for cell in row[:-1]:
			if cell.is_linked(cell.neighbors["east"]):	
				print("    ", end="")
			else:
				print("   |", end="")
		print("   |")

