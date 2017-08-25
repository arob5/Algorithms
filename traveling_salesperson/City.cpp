/*
* City.cpp
*
* Class implementation for a "City" to be used in various travelling salesperson tests
*
* Last Modified: 8/24/2017
* Modified By: Andrew Roberts
*
*/

#include <iostream>
#include <cmath>
#include "City.h"

City::City(int x_max, int y_max) {

	x = rand() % x_max; 
	y = rand() % y_max;  

}

float City::operator-(const City &neighbor_city) {

	float x_dist = pow(neighbor_city.x - this->x, 2.0); 
	float y_dist = pow(neighbor_city.y - this->y, 2.0); 

	return sqrt(x_dist + y_dist); 

} 

void City::print_coords() {

	std::cout << "(" << x << ", " << y << ")" << std::endl; 

}
