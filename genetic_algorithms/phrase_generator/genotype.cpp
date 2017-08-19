/*
* genotype.cpp
* Purpose: Class implementation for chlass defining pseudo-DNA as a character array
* Last Modified: 8/19/2017
* Modified By: AndrewRoberts
*/

#include <cstdlib>
#include <iostream>
#include <math.h>
#include <ctime>
#include "genotype.h"

/*
* Constructor - Initializes random DNA
*/
Genotype::Genotype(int dna_length, float mutation_rate) {
	this->dna_length = dna_length; 
	this->mutation_rate = mutation_rate; 

	for(int i = 0; i < dna_length; i++) {
		dna.push_back(random_char()); 	
	}	
	
}

/*
* Returns a random character in the ASCII range:
* 32 - 126
*
*/
char Genotype::random_char() {
	
	char ch = (rand() % 95) + 32;
	return ch; 

}

/*
* Converts dna char array to string
* Returns: string (genotype)
*/
std::string Genotype::arr_to_str() {

	std::string dna_string = ""; 

	for(int i = 0; i < dna_length; i++) 
		dna_string += dna[i]; 
	
	return dna_string; 

}

/*
* Performs a simple crossover on two "parents" and produces a "child"
* Child will have half of DNA of each parent
*
* Args: Genotype& (Reference to second parent)
* Returns: Genotype (chld)
*/
Genotype Genotype::crossover(Genotype &vec) {

	Genotype child(dna_length, mutation_rate); 
	int midpoint = ceil(dna_length / (float)2); 

	for(int i = 0; i < dna_length; i++) {
		if(i < midpoint)
			child.dna[i] = dna[i]; 
		else
			child.dna[i] = vec.dna[i]; 	
	}	

	return child; 
	
}

/*
* Mutates DNA; will change individual genes (chars) with certain probability
* Probability of individual char being changed depends on mutation_rate
*/
void Genotype::mutate() {

	for(int i = 0; i < dna_length; i++) {

		if(((double)rand() / RAND_MAX) <= mutation_rate)
			dna[i] = random_char();  

	}

}

// TEMP - For debugging
void Genotype::print() {

	for(int i = 0; i < dna_length; i++)
		std::cout << dna[i] << " "; 

	std::cout << std::endl; 
}
