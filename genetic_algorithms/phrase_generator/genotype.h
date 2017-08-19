/*
* genotype.h
* Purpose: Class defining pseudo-DNA as a character array
* Last Modified: 8/19/2017
* Modified By: AndrewRoberts
*/

#ifndef GENOTYPE_H_
#define GENOTYPE_H_

#include <vector>

class Genotype {
	public:
		Genotype(int len, float mutation_rate); 
		char random_char(); 
		std::string arr_to_str(); 	
		Genotype crossover(Genotype&); 
		void mutate(); 
		void print(); 
		
	private:
		int dna_length; 
		float mutation_rate; 
		std::vector<char> dna; 	
		
};

#endif
