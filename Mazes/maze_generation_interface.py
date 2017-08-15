#
# binary_tree_demo.py
# Produces a maze utilizing the Cell, Grid, and BinarySearchMaze classes 
# Last Modified: 8/15/2017
# Modified By: Andrew Roberts
#

import maze_generation_algorithms
import maze_search_algorithms
import grid_cell_class
import sys

def main():
	rows, cols, alg = parse_cmd_line_args(sys.argv[1:])
	grid = grid_cell_class.Grid(rows, cols)

	if alg == "binary":
		maze_generation_algorithms.binary_search(grid)
	elif alg == "sidewinder":
		maze_generation_algorithms.sidewinder(grid)

	print("Maze generated using {} algorithm".format(alg))
	print("Enter 'm' to print maze, 'p' to print maze with optimal path, 'q' to quit")
	
	usr_input = None
	while usr_input != "q":
		usr_input = input(">> ")
		if ensure_valid_input(usr_input):
			execute_user_command(grid, usr_input)
		else:
			print("Unrecognized command")

def parse_cmd_line_args(args_list):
	""" Ensures correct number of command line arguments

	Args:
 	    args_list (list): List of command line arguments (not including filename)

	Returns:
	    -int: Number of rows for grid
	    -int: Number of columns for grid
	    -str: Maze generation algorithm to use
	
	Raises exception if there are not 3 arguments passed (not including filename) 
	"""

	try:
		if len(args_list) != 3:
			raise Exception
	except Exception:
		print("Must pass 3 command line arguments: -#rows -#cols --algorithm")
		sys.exit(1)

	return get_cmd_line_values(args_list)
	
def get_cmd_line_values(args_list):
	""" Returns parsed values from command line input

	Args:
	    args_list (list): List of command line arguments (not including filename)

	Returns:
	    -int: Number of rows for grid
	    -int: Number of columns for grid
	    -str: Maze generation algorithm to use
	    
	Raises exception if any command line input is not valid
	"""
	try:
		n_rows = int(args_list[0][1:])
	except Exception:
		print("First argument must look like '-k', where k is a valid int")
		sys.exit(1)
	
	try:
		n_cols = int(args_list[1][1:])
	except Exception:
		print("Second argument must look like '-k', where k is a valid int")
		sys.exit(1)
	
	try:
		valid_input = ["binary", "sidewinder"]
		if args_list[2][2:] not in valid_input:
			raise Exception
	except Exception:
		print("Third argument must look like '--a', where a is one of the following: {}".format(valid_input))
		sys.exit(1)
	else:
		alg = args_list[2][2:]

	return n_rows, n_cols, alg	

def ensure_valid_input(usr_input):
	"""Returns True if input valid, otherwise False"""
	return usr_input in ["m", "p", "q"]
		
def execute_user_command(grid, usr_input):
	if usr_input == "m":
		grid.print_grid()

	if usr_input == "p":
		valid_input = False
		while not valid_input:
			valid_input = execute_bfs(grid)			
	
def execute_bfs(grid):
	start = input("Enter row and column of start node (row <space> column): ")
	goal = input("Enter row and column of goal node (row <space> column): ") 

	try:
		start = tuple(map(int, start.split()))	
		goal = tuple(map(int, goal.split()))
	except Exception:
		print("Invalid input")
		return False

	try:
		optimal_path = maze_search_algorithms.bfs(grid, start, goal)

		if not optimal_path:
			raise Exception 

		grid.print_grid(optimal_path)	
	except Exception:
		print("No path found")

	return True
			
main()
