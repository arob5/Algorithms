#
# maze_generation_algorithms.py
# Various algorithms to generate a random maze
# Last Modified: 8/13/2017
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

def sidewinder(grid):
	# Northern row
	for j, cell in enumerate(grid.row_at(0)[:-1]):
		cell.link(grid.cell_at(0, j+1))

	for i, row in enumerate(grid.grid):
		if i == 0:
			continue
		cell_run = [grid.cell_at(i, 0)]
		for j, cell in enumerate(row):
			if j == grid.columns-1:
				cell_chosen = np.random.choice(cell_run)
				cell_chosen.link(cell_chosen.neighbors["north"])
				break	

			expand_run = np.random.choice([0, 1])
			if expand_run:
				cell.link(grid.cell_at(i, j+1))
				cell_run.append(cell)
			else:
				cell_chosen = np.random.choice(cell_run)
				cell_chosen.link(cell_chosen.neighbors["north"])
				cell_run = [grid.cell_at(i, j+1)]
				
	
