#
# binary_tree_demo.py
# Produces a maze utilizing the Cell, Grid, and BinarySearchMaze classes 
# Last Modified: 8/7/2017
# Modified By: Andrew Roberts
#

import grid_cell_class
import binary_search_maze_class


# Create a grid
grid = grid_cell_class.Grid(10, 10)
grid.print_grid()

# Run the binary search algorithm
bs = binary_search_maze_class.BinarySearchMaze()
bs.mazeify(grid)
grid.print_grid()
