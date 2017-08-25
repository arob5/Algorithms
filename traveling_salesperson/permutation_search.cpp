/*
* 
* permutation_search.cpp
* A TSP search method that loops through all possible paths (permutations of cities)
* Slightly better than random_search.cpp but still not scalable 
*
* Last Modified: 8/25/2017
* Modified By: Andrew Roberts
*
*/

#include <iostream> 
#include <vector>
#include "City.h"

void next_permutation(int[], int size); 
float calc_path_distance(std::vector<City>&); 
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

	int test[] = {7, 2, 3, 1, 0}; 
	for(int i = 0; i < 5; i++)
		std::cout << test[i] << " "; 
	std::cout << "\n";

	next_permutation(test, 5); 


/*
	int i = 0; 
	float best_dist = calc_path_distance(city_pop);  
	while(i < N_ITR) {
		next_permutation(city_pop); 
		float curr_dist = calc_path_distance(city_pop); 
		best_dist = update_best_dist(best_dist, curr_dist); 
		std::cout << "Current: " << curr_dist << "----- Best: " << best_dist << std::endl; 
		i++; 
	}
*/

	return 0; 

}

void next_permutation(int arr[], int size) {

	int best_index_x = -1; 
	int biggest_x = -1; 
	for(int i = 0; i < size-1; i++) {	

		if(arr[i] < arr[i+1]) {

			if(arr[i] > biggest) {
				biggest_x = arr[i]; 
				best_index_x = i; 
			}
		
		}
	
	}


	int best_index_y = -1; 
	int biggest_y = -1;  
	for(int i = 0; i < size-1; i++) {
		

	}


	std::cout << "Best index x: " << best_index_x << std::endl;
	std::cout << "Largest value x: " << biggest_x << std::endl; 

}

float calc_path_distance(std::vector<City> &city_pop) {

	float total_dist = 0; 
	for(int i = 0; i < city_pop.size()-1; i++)
		total_dist += (city_pop[i]-city_pop[i+1]); 

	return total_dist; 

}

float update_best_dist(float best_dist, float curr_dist) {

	if(curr_dist < best_dist)
		return curr_dist; 

	return best_dist; 

}
