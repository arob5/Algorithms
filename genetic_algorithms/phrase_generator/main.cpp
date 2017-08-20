/*
* main.cpp
* main() for phrase generator genetic algorithm
* Last Modified: 8/19/2017
* Modified By: Andrew Roberts
*/

#include <iostream> 
#include "population.h"
#include "genotype.h"
#include <vector>

const float MUTATION_RATE = .01; 
const int POPULATION_SIZE = 200; 
const float GOAL_THRESHOLD = 1;

int main() {

	srand((int)time(0));

	std::string user_phrase; 	

	std::cout << "Enter a word or phrase below: \n" << ">>"; 
	getline(std::cin, user_phrase); 

	Population p(user_phrase, MUTATION_RATE, POPULATION_SIZE, GOAL_THRESHOLD); 

	while(!p.evolution_finished()) {
		std::cout << p.best_individual() << "-----" << p.print_avg_fitness() << std::endl; 
		p.new_generation(); 
	}

	return 0; 
}
