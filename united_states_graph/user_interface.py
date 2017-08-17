#
# user_interface.py
# A simple interface to search for shortest paths between two states
# Last Modified: 8/17/2017
# Modified By: Andrew Roberts
#

import pandas as pd
import numpy as np
import search_algs

# TODO - catch exception when trying to make a path to Hawaii/Alaska
def main():
	START = "Illinois"
	state_df = pd.read_pickle("state_df.pickle")
	search_algs.bfs(state_df, START)
	search_algs.shortest_path(state_df, START, "Arizona")

main()
