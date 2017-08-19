/*
* main.cpp
* main() for phrase generator genetic algorithm
* Last Modified: 8/19/2017
* Modified By: Andrew Roberts
*/

#include <iostream> 
#include "genotype.h"
#include <vector>

int main() {


	srand((int)time(0));

	float mr = .25; 

	Genotype genotype(10, mr); 	
	Genotype g2(10, mr); 
	
	genotype.print(); 
	g2.print();  

	Genotype child = genotype.crossover(g2); 	
	child.print(); 	

	child.mutate(); 
	child.print();

	return 0; 
}
