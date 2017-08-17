#
# search_algs.py
# Search algorithms to find shortest path between to U.S. states
# Last Modified: 8/17/2017
# Modified By: Andrew Roberts
#

import pandas as pd
import numpy as np

def bfs(state_df, start):
	current = start
	state_df.loc[current, "Distance"] = 0
	q, S = [current], set([current])

	while q:
		current = q.pop()
		for state in state_df.loc[current, "Borders"]: 
			if state not in S:
				S.add(state)
				q = [state] + q
				state_df.loc[state, "Previous"] = current
				state_df.loc[state, "Distance"] = state_df.loc[current, "Distance"] + 1

# Implement recursively
def shortest_path(state_df, start, goal):
	current = goal
	path = []

	while current != start:
		path.append(current)
		current = state_df.loc[current, "Previous"]		
	path.append(start)

	print(path[::-1])
	
	"""
	print(current, end="")
	while current != goal:
		if current != start:
			print("-->", current, end="")

		current = state_df.loc[current, "Previous"]
	print("-->", goal)
	"""
	
	
	
