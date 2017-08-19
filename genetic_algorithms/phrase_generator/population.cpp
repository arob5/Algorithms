/*
* population.cpp
* Purpose: TODO
* Last Modified: 8/19/2017
* Modified By: AndrewRoberts
*/

#include <iostream>
#include "population.h"

Population::Population(std::string target_phrase, float mutation_rate) {	

	this->mutation_rate = mutation_rate; 
	
	target = str_to_arr(target_phrase);  

}

std::vector<char> Population::str_to_arr(std::string target_phrase) {

	int dna_len = target_phrase.length(); 
	std::vector<char> target_arr; 

	for(int i = 0; i < dna_len; i++)
		target_arr.push_back(target_phrase[i]); 

	return target_arr; 
		
}

void Population::print() {

	for(int i = 0; i < target.size(); i++)
		std::cout << target[i] << " "; 
	std::cout << std::endl; 

}
