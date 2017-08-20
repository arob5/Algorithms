/*
* population.cpp
* Purpose: TODO
* Last Modified: 8/19/2017
* Modified By: AndrewRoberts
*/

#include <iostream>
#include <cstdlib>
#include "population.h"

/*
* Constructor - Stores mutation rate, target phrase, and initializes 
*               population of 'Genotypes' (individuals)
* Args: string (target/goal phrase), float (probability of mutation for each char),
*       int (number of individuals in population)
*/
Population::Population(std::string target_phrase, float mutation_rate, int population_size) {	

	this->mutation_rate = mutation_rate; 
	
	target = str_to_arr(target_phrase);  

	for(int i = 0; i < population_size; i++)
		population.push_back(Genotype(target_phrase.length())); 	

}

/*
* Converts target/goal phrase from a string to a vector
* 
* Args: string (target/goal phrase as string)
* Returns: vector<char> (target/goal phrase as char vector)
*/
std::vector<char> Population::str_to_arr(std::string target_phrase) {

	int dna_len = target_phrase.length(); 
	std::vector<char> target_arr; 

	for(int i = 0; i < dna_len; i++)
		target_arr.push_back(target_phrase[i]); 

	return target_arr; 
		
}

/*
* Calculates fitness for each individual in population
* Fitness values are stores as private variables in each Genotype object
*/
void Population::calc_fitness() {

	int pop_size = population.size(); 

	for(int i = 0; i < pop_size; i++)
		population[i].calc_fitness(target); 

}

/*
* Uses a roulette wheel selection to randomly select an individual from the population
* Selection is weighted by the individuals' fitness levels
*
* Returns: int (index of selected individual in population vector) 
*/
int Population::roulette_wheel_selection() {

	int fitness_sum = 0; 
	for(int i = 0; i < population.size(); i++)
		fitness_sum += population[i].get_fitness(); 

	if(fitness_sum == 0)
		return rand() % population.size(); 


	int rnd = rand() % fitness_sum; 

	int cum_sum = 0; 
	for(int i = 0; i < population.size(); i++) {
		cum_sum += population[i].get_fitness(); 	

		if(cum_sum > rnd)
			return i; 

	}

	return -1; 	
	
}

void Population::print() {

	for(int i = 0; i < population.size(); i++) {
		std::cout << population[i].get_fitness() << "-----"; 
		population[i].print(); 
	}
}
