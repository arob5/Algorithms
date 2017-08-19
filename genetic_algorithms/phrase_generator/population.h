/*
* population.h
* Purpose: TODO
* Last Modified: 8/19/2017
* Modified By: AndrewRoberts
*/

#include "genotype.h"

class Population {
	public:
		Population(std::string target_phrase, float mutation_rate, int n_individuals); 
		void calc_fitness(); 
		void roulette_wheel_selection(); 
		void print(); 	
	
	private:
		std::vector<char> str_to_arr(std::string); 

		std::vector<Genotype> population; 
		std::vector<char> target; 
		float mutation_rate; 
		int n_generations; 
		bool finished; 
			
};
