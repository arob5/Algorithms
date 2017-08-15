#
# maze_search_algorithms.py
# Graph algorithms for traversing the mazes
# Last Modified: 8/15/2017
# Modified By: Andrew Roberts
#

import grid_cell_class

def bfs(grid):
	links = get_links(grid)
#	print(links)

	for key, value in links.items():
		print(key, ":", value)

def get_links(grid):
	links_dict = {}
	for i in range(grid.rows):
		for j in range(grid.columns):
			curr_cell = grid.cell_at(i, j)
			linked_with = set()
			for cell in curr_cell.current_links():
				linked_with.add(cell.cell_location())
			links_dict[(i, j)] = linked_with

	return links_dict
