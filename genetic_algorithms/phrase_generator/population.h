/*
* population.h
* Purpose: TODO
* Last Modified: 8/19/2017
* Modified By: AndrewRoberts
*/

#include "genotype.h"

class Population {
	public:
		Population(std::string target_phrase, float mutation_rate, 
                                         int n_individuals, float goal_threshold); 
		void calc_fitness(); 
		int roulette_wheel_selection(); 
		void new_generation(); 
		bool evolution_finished(); 
		std::string best_individual(); 
		float print_avg_fitness(); 
		void print(); 	
	
	private:
		std::vector<char> str_to_arr(std::string); 
		void evaluate(); 
		void end_evolution(); 

		std::vector<Genotype> population; 
		std::vector<char> target; 
		float mutation_rate; 
		int n_generations; 
		int population_size; 
		float goal_threshold; 

		std::string current_best; 
		bool finished; 
			
};
