#
# grid_cell_class.py
# Class implementations for a grid (which is a container for cells) and a cell (which fits into the container grid) 
# Last Modified: 8/9/2017
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
	
	def print_grid(self):
		SPACE = "   "
		WALL  = "   |"
		SPACE_HORIZ = "   +"
		WALL_HORIZ = "---+"

		top_bottom_walls = "+" + ("---+" * self.columns)
		row_strings_top  = []
		row_strings_bottom = []

		for i, row in enumerate(self.grid):
			ascii_row_top = "|"
			ascii_row_bottom = "+"
			for j, cell in enumerate(row):
				if j != (self.columns-1):
					if cell.is_linked(cell.neighbors["east"]):
						ascii_row_top += SPACE
					else:
						ascii_row_top += WALL
				if i != (self.rows-1): 
					if cell.is_linked(cell.neighbors["south"]):
						ascii_row_bottom += SPACE_HORIZ
					else:
						ascii_row_bottom += WALL_HORIZ	
	
			ascii_row_top += WALL
			row_strings_top.append(ascii_row_top)
			if i != (self.rows-1):
				row_strings_bottom.append(ascii_row_bottom)

#		row_strings_top.append("|" + WALL*self.columns)	

		print(top_bottom_walls)
		for top, bot in zip(row_strings_top, row_strings_bottom):
			print(top)
			print(bot)
		print(row_strings_top[-1])
		print(top_bottom_walls)

g = Grid(10, 10)
grid = g.grid

g.print_grid()


#for i in range(10):
#	print(grid[i])
