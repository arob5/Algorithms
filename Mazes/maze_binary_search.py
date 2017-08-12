#
# maze_binary_search.py
# Implementation of Binary Search Algorithm to generate a random maze
# Last Modified: 8/11/2017
# Modified By: Andrew Roberts
#

import grid_cell_class
import numpy as np

def mazeify(grid):
	# Northern row
	for j, cell in enumerate(grid.row_at(0)[:-1]):
		cell.link(grid.cell_at(0, j+1))

	# Eastern column
	for i, cell in enumerate(grid.column_at(grid.columns-1)[:-1]):
		cell.link(grid.cell_at(grid.columns-1, i+1))	

	# Interior cells
	for i in range(grid.rows-1):
		for j in range(grid.columns-1): 
			cell_neighbors = grid.cell_at(i, j).neighbors
			
			neighbors_relevant = []
			for key in cell_neighbors:
				if (cell_neighbors[key] is not None) and (key in ["north", "east"]):
					neighbors_relevant.append(cell_neighbors[key])	
				
			to_link = np.random.choice(neighbors_relevant) 
			grid.cell_at(i, j).link(to_link)	
