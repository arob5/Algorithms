#
# agents.py
# Classes defining a vector and an individual that makes up the population
# Last Modified: 8/28/2017
# Modified By: Andrew Roberts
#

import numpy as np
import pygame
import math

class Vector():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, vec):
		try: 
			return Vector(self.x + vec.x, self.y + vec.y)
		except TypeError:
			print("Argument must be a vector")

	def __mul__(self, scalar):
		try:
			return Vector(self.x * scalar, self.y * scalar)
		except TypError:
			print("Scalar value must be int or float")

	__rmul__ = __mul__
		
	def length(self):
		return math.sqrt(self.x*self.x + self.y*self.y) 

	def normalize(self):
			if self.length() == 0:
				self.x += np.random.choice([-1, 1])

			return self * (1 / self.length())
	
	def return_coordinates_tuple(self):
		return (self.x, self.y)

class Ball():
	def __init__(self, surface, pos, lifetime, goal, vel=None, speed_scale=4):
		self.surface = surface
		x, y = pos
		self.pos = Vector(x, y)
		self.speed = speed_scale
		self.radius = 7
		
		if vel is None:
			self.vel = self.create_velocity_list(lifetime)
		else:
			self.vel = vel

		self.color = (255, 153, 102)
		self.lifetime = lifetime
		self.goal = goal
		self.fitness = 0

	def create_velocity_list(self, lifetime):
		return [(self.speed*self.random_direction()) for i in range(lifetime)]
	
	def random_direction(self):
		theta = np.random.randint(low=0, high=360)
		dx = int(np.round(math.cos(math.radians(theta))))
		dy = int(np.round(math.sin(math.radians(theta))))

		return Vector(dx, dy)		
	
	def draw(self, index):
		self.pos = self.pos + self.vel[index]
		self.fitness += self.calc_fitness(index)

		pygame.draw.circle(self.surface, self.color, self.pos.return_coordinates_tuple(), self.radius)

	def calc_fitness(self, index):
		x, y = self.pos.return_coordinates_tuple()	
		goal_x, goal_y = self.goal

		return (1 / (math.sqrt(math.pow(x - goal_x, 2.0) + math.pow(y - goal_y, 2.0))))

	def crossover(self, ball2, pos):

		midpoint = np.random.randint(low=0, high=len(self.vel))
		child_vel = []
		
		for i, v in enumerate(self.vel):
			if i < midpoint:
				child_vel.append(v)
			else:
				child_vel.append(ball2.vel[i])
		
		return Ball(self.surface, pos, self.lifetime, self.goal, child_vel)
