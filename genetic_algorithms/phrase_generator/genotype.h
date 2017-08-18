/*
* genotype.h
* Purpose: Class defining pseudo-DNA as a character array
* Last Modified: 8/18/2017
* Modified By: AndrewRoberts
*/

#ifndef GENOTYPE_H_
#define GENOTYPE_H_

#include <vector>

class Genotype() {
	public:
		Genotype(int len); 
		char random_char(); 
		string arr_to_str(); 	
		std::vector<char> crossover(std::vector<char>); // Should function return &, *, or copy?  
		void mutate(); 
		
	
	private:
		std::vector<char> dna; 
		std::vector<char> target; 
		


}

#endif
