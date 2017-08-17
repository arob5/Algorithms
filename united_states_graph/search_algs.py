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

def shortest_path_wrapper(state_df, start, current):
	if current in ["Hawaii", "Alaska"]:
		print("No path found")	
	else:
		print("{} state journey".format(int(state_df.loc[current, "Distance"])))
		shortest_path(state_df, start, current, current)
		print(current)


def shortest_path(state_df, start, current, goal):
	if current != start:
		shortest_path(state_df, start, state_df.loc[current, "Previous"], goal)
	if current != goal:
		print(current, "--> ", end="")
	
	
	
