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
*
* Also calculates initial fitness values and evaluates the first generation
*
* Args: string (target/goal phrase), float (probability of mutation for each char),
*       int (number of individuals in population)
*/
Population::Population(std::string target_phrase, float mutation_rate, 
                                         int population_size, float goal_threshold) {	

	this->mutation_rate = mutation_rate; 
	this -> population_size = population_size; 
	this->goal_threshold = goal_threshold; 

	n_generations = 1;
	finished = false; 
	
	target = str_to_arr(target_phrase);  

	for(int i = 0; i < population_size; i++)
		population.push_back(Genotype(target_phrase.length())); 	

	calc_fitness(); 
	evaluate(); 

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

/*
* Generates a new population corresponding to a new generation
* Chooses parents using roulette selection, then creates and mutates child
*/
void Population::new_generation() {

 	std::vector<Genotype> new_population; 

	for(int i = 0; i < population.size(); i++) {
		int index_parent1 = roulette_wheel_selection(); 
		int index_parent2 = roulette_wheel_selection(); 
	
		Genotype child = population[index_parent1].crossover(population[index_parent2]); 	
		child.mutate(mutation_rate); 

		new_population.push_back(child); 

	}

	population = new_population; 
	calc_fitness(); 	
	n_generations++; 
	evaluate(); 

}

/*
* Finds individual with best fitness in current generation
* Stores this individual's dna and checks to see if solution has been found
*/
void Population::evaluate() {

	int best_fitness = population[0].get_fitness(); 
	int best_genotype_index = 0; 

	for(int i = 1; i < population.size(); i++) {
		
		if(population[i].get_fitness() > best_fitness) {
			best_fitness = population[i].get_fitness(); 
			best_genotype_index = i; 				
		}
	}

	current_best = population[best_genotype_index].arr_to_str();

	if(best_fitness >= (target.size() * target.size() * goal_threshold))
		end_evolution(); 

}

/*
* Sets 'finished' to false to signify solution has been found
* Prints out results to console
*/
void Population::end_evolution() {

	finished = true; 

	std::cout << "\n-----Found solution-----" << std::endl;  
	std::cout << "--> '" << current_best << "'" << std::endl; 
	std::cout << "--> Completed in " << n_generations << " generations" << std::endl; 
	std::cout << "--> Goal threshold: " << goal_threshold << std::endl; 
	std::cout << "--> Mutation rate: " << mutation_rate << std::endl; 
	std::cout << "--> Population size: " << population_size << std::endl; 

}

/*
* Getter method to check if evolution is finished
*/
bool Population::evolution_finished() {

	return finished; 

}

/*
* Getter method to return string of best individual's DNA
*/
std::string Population::best_individual() {

	return current_best;  

}

float Population::print_avg_fitness() {

	int sum = 0; 
	for(int i = 0; i < population.size(); i++)
		sum += population[i].get_fitness(); 

	return sum / (float)population.size(); 	

}

void Population::print() {

	for(int i = 0; i < population.size(); i++) {
		std::cout << population[i].get_fitness() << "-----"; 
		population[i].print(); 
	}
}
