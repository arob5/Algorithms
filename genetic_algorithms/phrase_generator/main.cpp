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

int main() {

	srand((int)time(0));

	Population p("AAAAAAAAAA", .25, 10); 
	p.calc_fitness(); 
	p.print(); 

	std::cout << "\n\n\n\n\n\n"; 

	p.roulette_wheel_selection(); 	

	return 0; 
}
