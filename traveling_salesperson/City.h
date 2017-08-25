/*
* City.h
*
* Class definition for a "City" to be used in various travelling salesperson tests
*
* Last Modified: 8/24/2017
* Modified By: Andrew Roberts
*
*/

#ifndef CITY_H
#define CITY_H

#include <cstdlib>
#include <ctime>

class City {
	public: 
		City(int, int); 
		float operator-(const City&); 
		void print_coords(); 


	private: 
		int x, y; 

}; 

#endif 
