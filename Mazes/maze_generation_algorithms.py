#
# maze_generation_algorithms.py
# Various algorithms to generate a random maze
# Last Modified: 8/12/2017
# Modified By: Andrew Roberts
#

import grid_cell_class
import numpy as np

def binary_search(grid):
	# Northern row
	for j, cell in enumerate(grid.row_at(0)[:-1]):
		cell.link(grid.cell_at(0, j+1))

	# Eastern column
	for i, cell in enumerate(grid.column_at(grid.columns-1)[:-1]):
		cell.link(grid.cell_at(i+1, grid.columns-1))	

	# Interior cells
	for i in range(1, grid.rows):
		for j in range(grid.columns-1): 
			cell_neighbors = grid.cell_at(i, j).current_neighbors(["north", "east"])	
			to_link = np.random.choice(cell_neighbors) 
			grid.cell_at(i, j).link(to_link)	