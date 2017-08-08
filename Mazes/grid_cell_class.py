#
# grid_cell_class.py
# Class implementations for a grid (which is a container for cells) and a cell (which fits into the container grid) 
# Last Modified: 8/6/2017
# Modified By: Andrew Roberts
#

class Cell(): 
	def __init__(self, row, column):
		self.row = row
		self.column = column
		neighbors = {"north": None, "south": None, "east": None, "west": None}
		self.links = {} 

	def link(self, cell, bidir=True):
		self.links[cell] = True
		if bidir:
			cell.link(self, false)
	
	def unlink(self, cell, bidir=True):
		del self.links[cell] 
		if bidir:
			cell.unlink(self, False)

	def links(self):
		return list(self.links.keys())				

	def is_linked(self, cell):
		return cell in self.links

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
		return [[Cell(i,j) for i in range(self.rows)] for j in range(self.columns)]	

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
		
		# Interior cells	
		for i in range(1, self.rows-1):
			for j in range(1, self.columns-1):
				self.grid[i][j].neighbors["north"] = grid[i-1][j]
				self.grid[i][j].neighbors["south"] = grid[i+1][j]
				self.grid[i][j].neighbors["east"] = grid[i][j+1]
				self.grid[i][j].neighbors["west"] = grid[i][j-1]
			

g = Grid(10, 10)
grid = g.grid

for i in range(10):
	print(grid[i])
