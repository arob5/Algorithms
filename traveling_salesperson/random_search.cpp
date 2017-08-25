/*
*
* random_search.cpp
* Attempting to solve TSP in a completely randomized fashion 
* Basically a demonstration of the infeasability of an exhaustive search for this problem
*
* Last Modified: 8/24/2017
* Modified By: Andrew Roberts
*
*/

#include <iostream> 
#include <vector>
#include "City.h"

float calc_path_distance(std::vector<City>&); 
void random_swap(std::vector<City>&); 
float update_best_dist(float, float); 

const int NUM_CITIES = 100; 
const int X_MAX = 1000; 
const int Y_MAX = 1000; 
const int N_ITR = 1000000; 

int main() {

	srand((int)time(0)); 

	std::vector<City> city_pop; 	
	
	for(int i = 0; i < NUM_CITIES; i++) 
		city_pop.push_back(City(X_MAX, Y_MAX)); 	

	int i = 0; 
	float best_dist = calc_path_distance(city_pop);  
	while(i < N_ITR) {
		random_swap(city_pop); 
		float curr_dist = calc_path_distance(city_pop); 
		best_dist = update_best_dist(best_dist, curr_dist); 
		std::cout << "Current: " << curr_dist << "----- Best: " << best_dist << std::endl; 
		i++; 
	}

	return 0; 

}

float calc_path_distance(std::vector<City> &city_pop) {

	float total_dist = 0; 
	for(int i = 0; i < city_pop.size()-1; i++)
		total_dist += (city_pop[i]-city_pop[i+1]); 

	return total_dist; 

}

void random_swap(std::vector<City> &city_pop) {

	int rand_index_1 = rand() % NUM_CITIES;  
	int rand_index_2 = rand() % NUM_CITIES;  

	iter_swap(city_pop.begin() + rand_index_1, city_pop.begin() + rand_index_2); 

}

float update_best_dist(float best_dist, float curr_dist) {

	if(curr_dist < best_dist)
		return curr_dist; 

	return best_dist; 

}
