#
# simulation.py
# Population of "balls" finding a path to goal using genetic algorithm
# Last Modified: 8/28/2017
# Modified By: Andrew Roberts
#

from collections import namedtuple
from functools import reduce
import numpy as np
import random
import agents
import pygame
import math
import time
pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

Color = namedtuple("Color", ["red", "green", "blue"])
goal_color = Color(255, 255, 153)
light_blue = Color(153, 204, 255)

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Pathfinder")
clock = pygame.time.Clock()

GOAL = (int(np.round(DISPLAY_WIDTH/2)), int(np.round(DISPLAY_HEIGHT*.15)))
N_BALLS = 200
INIT_POS = (int(np.round(DISPLAY_WIDTH/2)), int(np.round(DISPLAY_HEIGHT)))
INDEX_LIM = 150
FRAME_UPDATE_INTERVAL = 3

def game_loop():
	game_exit = False
	
	ball_array = [agents.Ball(game_display, INIT_POS, INDEX_LIM, GOAL) for i in range(N_BALLS)]

	frame = 0
	index = 0
	while not game_exit: 

		if index == INDEX_LIM-1:
			ball_array = new_generation(ball_array)	
			index = 0

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit = True		

		game_display.fill(light_blue)	

		for ball in ball_array:
			ball.draw(index)
		pygame.draw.circle(game_display, goal_color, GOAL, 20)

		pygame.display.update()

		if frame % FRAME_UPDATE_INTERVAL == 0: 
			index += 1
		frame += 1
		clock.tick(60)

def new_generation(ball_array):
	new_pop = []
	
	for i in range(N_BALLS):
		parent_1_index = roulette_wheel_selection(ball_array)
		parent_2_index = roulette_wheel_selection(ball_array)

		child = ball_array[parent_1_index].crossover(ball_array[parent_2_index], INIT_POS)
		#child.mutate()
		new_pop.append(child)

	return new_pop

def roulette_wheel_selection(ball_array):
	fitness_sum = reduce(lambda x, y: x+y, [ball.fitness for ball in ball_array])
	
	if fitness_sum == 0:
		return np.random.randint(low=0, high=N_BALLS) 

	rnd = random.uniform(0, fitness_sum)
	
	cum_sum = 0
	for i in range(N_BALLS):
		cum_sum += ball_array[i].fitness

		if cum_sum > rnd:
			return i
			
	return -1

game_loop()
pygame.quit()

