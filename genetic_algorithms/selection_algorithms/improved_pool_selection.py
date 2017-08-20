#
# improved_pool_selection.py
# Selecting elements from list based on weighted probability
# Last Modified: 8/20/2017
# Modified By: Andrew Roberts
#

import numpy as np

NUM_SAMPLES = 100000

pool = [10, 2, 5] # Values correspond to fitness scores
times_selected = [0, 0, 0]
fitness_sum = sum(pool)	


for i in range(NUM_SAMPLES):
	rnd = np.random.randint(low=0, high=fitness_sum)

	for i, elem in enumerate(pool):
		rnd -= elem
		if rnd < 0:
			times_selected[i] += 1
			break 

print("Elem 1 selected {0[0]} times with probability of selection {1}".format(times_selected, pool[0]/fitness_sum))
print("Elem 2 selected {0[1]} times with probability of selection {1}".format(times_selected, pool[1]/fitness_sum))
print("Elem 3 selected {0[2]} times with probability of selection {1}".format(times_selected, pool[2]/fitness_sum))
			
		
	

