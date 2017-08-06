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
		cell.link(self, false) if bidir
	
	def unlink(self, cell, bidir=True):
		del self.links[cell] 
		cell.unlink(self, False) if bidir

	def links(self):
		return list(self.links.keys())				

	def is_linked(self, cell):
		return cell in self.links

	def current_neighbors(self):
		neighbor_cells = []
		for key in self.neighbors.keys():
			neightbor_cells.append(self.neighbors[key]) if self.neighbors[key] is not None
		return neighbor_cells


class Grid():
	def __init__(rows, columns):
		self.rows = rows
		self.columns = columns
		
		self.grid = self.prepare_grid()	
		self.configure_cells()			
		
	def prepare_grid():
		return [[Cell(i, j) for i in range(self.rows)] for j in range(self.columns)]	
			
