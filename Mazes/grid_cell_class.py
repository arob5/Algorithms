#
# grid_cell_class.py
# Class implementations for a grid (which is a container for cells) and a cell (which fits into the container grid) 
# Last Modified: 8/11/2017
# Modified By: Andrew Roberts
#

class Cell(): 
	def __init__(self, row, column):
		self.row = row
		self.column = column
		self.neighbors = {"north": None, "south": None, "east": None, "west": None}
		self.links = [] 

	def link(self, cell, bidir=True):
		self.links.append([cell.row, cell.column])
		if bidir:
			cell.link(self, False)
	
	def unlink(self, cell, bidir=True):
		self.links.remove([cell.row, cell.column]) 
		if bidir:
			cell.unlink(self, False)

	def is_linked(self, cell):
		return [cell.row, cell.column] in self.links

	def current_neighbors(self):
		neighbor_cells = []
		for key in self.neighbors.keys():
			if self.neighbors[key] is not None: 
				neightbor_cells.append(self.neighbors[key])
		return neighbor_cells


class Grid():
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		
		self.grid = self.prepare_grid()	
		self.configure_cells()			
		
	def prepare_grid(self):
		return [[Cell(i,j) for j in range(self.columns)] for i in range(self.rows)]	

	def configure_cells(self):
		# Rightmost border
		for i in range(self.rows):
			self.grid[i][self.columns-1].neighbors["east"] = None

		# Leftmost border 
		for i in range(self.rows):
			self.grid[i][0].neighbors["west"] = None

		# Topmost  border
		for j in range(self.columns):
			self.grid[0][j].neighbors["north"] = None

		# Bottommost border
		for j in range(self.columns):
			self.grid[self.rows-1][j].neighbors["south"] = None
		
		# All cells	
		for i in range(0, self.rows):
			for j in range(0, self.columns):
				if i != 0: 
					self.grid[i][j].neighbors["north"] = self.grid[i-1][j]
				if i != (self.rows-1):
					self.grid[i][j].neighbors["south"] = self.grid[i+1][j]
				if j != (self.columns-1):
					self.grid[i][j].neighbors["east"] = self.grid[i][j+1]
				if j != 0:
					self.grid[i][j].neighbors["west"] = self.grid[i][j-1]

	def cell_at(self, row, col):
		return self.grid[row][col]

	def row_at(self, row):
		try:
			return self.grid[row]
		except Exception:
			print("Row out of bounds")

	def column_at(self, col):
		try:
			return [row[col] for row in self.grid]
		except Exception:
			print("Column out of bounds")

	def print_grid(self):
		top_and_bottom_wall = "+" + ("---+" * self.columns)

		print(top_and_bottom_wall)
		for i, row in enumerate(self.grid):
			if i != 0:
				self.print_top_wall(row)	
			self.print_bottom_wall(row)		
		print(top_and_bottom_wall)	

	@staticmethod
	def print_top_wall(row):
		print("+", end="")

		for cell in row:
			if cell.is_linked(cell.neighbors["north"]):
				print("   +", end="")
			else:
				print("---+", end="")
		print("")

	@staticmethod
	def print_bottom_wall(row):
		print("|", end="")

		for cell in row[:-1]:
			if cell.is_linked(cell.neighbors["east"]):	
				print("    ", end="")
			else:
				print("   |", end="")
		print("   |")

