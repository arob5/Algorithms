/*
* genotype.cpp
* Purpose: Class implementation for chlass defining pseudo-DNA as a character array
* Last Modified: 8/18/2017
* Modified By: AndrewRoberts
*/

Genotype::Genotype(int len) {
	for(int i = 0; i < len; i++) {
		dna.push_back(random_char()); 	
	}	
}

/*
* Returns a random character in the ASCII range:
* 32 - 126
*
*/
char Genotype::random_char() {
// ASCII: 32 - 126

	char ch = rand() % 95 + 32;
	return ch; 

}
