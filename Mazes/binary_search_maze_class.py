#
# binary_search_maze_class.py
# Implementation of Binary Search Algorithm to generate a random maze
# Last Modified: 8/9/2017
# Modified By: Andrew Roberts
#

import grid_cell_class
import numpy as np

class BinarySearchMaze():
	@staticmethod
	def mazeify(grid):
		for i in range(grid.rows):
			for j in range(grid.columns): 
				neighbors_dict = grid.grid[i][j].neighbors
				
				neighbors = []
				for key in neighbors_dict:
					if (neighbors_dict[key] is not None) and (key in ["north", "east"]):
						neighbors.append(neighbors_dict[key])	
				
				to_link = np.random.choice(neighbors) 
				grid.grid[i][j].link(to_link)	
