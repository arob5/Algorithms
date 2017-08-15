#
# maze_search_algorithms.py
# Graph algorithms for traversing the mazes
# Last Modified: 8/15/2017
# Modified By: Andrew Roberts
#

import grid_cell_class

def bfs(grid, start, goal):
	links = get_links(grid)
	links[start]["prev"] = "root"
	visited = set()
	q = [start]

	while q:
		current = q.pop()
		if current == goal:
			return bfs_optimal_path(start, goal, links)
		unvisited = [cell for cell in links[current]["adj"] if links[cell]["prev"] is None]
		if unvisited:
			q = unvisited + q
			for cell in unvisited:
				links[cell]["prev"] = current
	return None	

def bfs_optimal_path(start, goal, links):
	current = goal
	optimal_path = []

	while current != "root":
		optimal_path.append(current)
		current = links[current]["prev"]		

	return optimal_path[::-1]


def get_links(grid):
	""" Returns an adjacency list for linked cells
	
	Args:
	    grid (Grid object): Grid/maze made up of Cell objects
	
	Returns:
	    links_dict (dict): Adjacency list

	"""
	links_dict = {}
	for i in range(grid.rows):
		for j in range(grid.columns):
			curr_cell = grid.cell_at(i, j)
			linked_with = set()
			for cell in curr_cell.current_links():
				linked_with.add(cell.cell_location())
			links_dict[(i, j)] = {"adj": linked_with, "prev": None}

	return links_dict
