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
Genotype::Genotype(int dna_length) {
	this->dna_length = dna_length; 

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
* Calculates the fitness of the DNA sequence
* Fitness defined as number of correct characters squared (order matters)
* 
* Args: vector<char>& (Reference to target/goal vector)
*/
void Genotype::calc_fitness(std::vector<char> &target) { 

	int score = 0; 
	
	for(int i = 0; i < dna_length; i++) {

		if(dna[i] == target[i])
			score++; 	

	}

	fitness = (score * score);  
	
}

/*
* Performs a simple crossover on two "parents" and produces a "child"
* Child will have some DNA from each parent
* To determine number of chars from each parent, random midpoint is selected
*
* Args: Genotype& (Reference to second parent)
* Returns: Genotype (chld)
*/
Genotype Genotype::crossover(Genotype &g) {

	Genotype child(dna_length); 
	int midpoint = rand() % dna_length; 

	for(int i = 0; i < dna_length; i++) {
		if(i < midpoint)
			child.dna[i] = dna[i]; 
		else
			child.dna[i] = g.dna[i]; 	
	}	

	return child; 
	
}

/*
* Mutates DNA; will change individual genes (chars) with certain probability
* Probability of individual char being changed depends on mutation_rate
*
* Args: float (probability of each gene being mutated)
*/
void Genotype::mutate(float mutation_rate) {

	for(int i = 0; i < dna_length; i++) {

		if(((double)rand() / RAND_MAX) <= mutation_rate)
			dna[i] = random_char();  

	}

}

/*
* Returns the fitness score of the individual (genotype) 
*/
int Genotype::get_fitness() {

	return fitness; 

}

// TEMP - For debugging
void Genotype::print() {

	for(int i = 0; i < dna_length; i++)
		std::cout << dna[i] << " "; 
	

	std::cout << std::endl; 

}
