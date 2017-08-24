#include <SFML/Audio.hpp>
#include <SFML/Graphics.hpp>
#include <vector>
#include <cstdlib>
#include <ctime>


const int NUM_CITIES = 20;
const int WIDTH = 1500;
const int HEIGHT = 1150;

void init_cities(std::vector<sf::CircleShape>&, int);
void draw_cities(sf::RenderWindow&, std::vector<sf::CircleShape>&);
void random_swap(std::vector<sf::CircleShape>&);

int main(int argc, char const** argv)
{
    
    srand((int)time(0));
    sf::RenderWindow window(sf::VideoMode(WIDTH, HEIGHT), "SFML window");
    

    std::vector<sf::CircleShape> cities(NUM_CITIES);
    init_cities(cities, 20);
    
    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            // Close window: exit
            if (event.type == sf::Event::Closed) {
                window.close();
            }

            // Escape pressed: exit
            if (event.type == sf::Event::KeyPressed && event.key.code == sf::Keyboard::Escape) {
                window.close();
            }
        }
        
        window.clear(sf::Color(255, 153, 102));
        draw_cities(window, cities);
        
        sf::RectangleShape line(sf::Vector2f(150, 5));
        line.setPosition(WIDTH-150, 200);
        line.rotate(-100);
 
        
        window.draw(line);
        random_swap(cities);
       
        
        window.display();
    }

    return EXIT_SUCCESS;
}


/*
 * Initilizes vector of circles, representing "cities"
 * Cities initialized at random locations
 *
 * Args: -> vector<sf::CircleShape>& (reference to vector containing
 *          circles representing cities)
 *       -> int (radius of each circle)
 *
 */
void init_cities(std::vector<sf::CircleShape> &cities, int radius) {
    
    for(int i = 0; i < cities.size(); i++) {
        cities[i].setRadius(radius);
        cities[i].setFillColor(sf::Color(51, 153, 255));
        cities[i].setOutlineThickness(5);
        cities[i].setOutlineColor(sf::Color(255, 255, 255));
        cities[i].setPosition(rand()%WIDTH, rand()%HEIGHT);
    }
    
}

/*
 * Loops through the cities vector and draws each circle
 *
 * Args: -> sf::RenderWindow& (Reference to window)
 *       -> vector<sf::CircleShape>& (Reference to cities vector)
 *
 */
void draw_cities(sf::RenderWindow &window, std::vector<sf::CircleShape> &cities) {
    
    for(int i = 0; i < cities.size(); i++) {
        window.draw(cities[i]);
    }
    
}

/*
 * Swap random 2 elements from cities vector
 * Reordering of vector represents a unique path through the cities
 *
 * Args: vector<sf::CircleShape>& (Reference to cities vector)
 *
 */
void random_swap(std::vector<sf::CircleShape> &cities) {
    
    int cities_len = cities.size();
    int pos1 = rand() % cities_len;
    int pos2 = rand() % cities_len;
    
    std::iter_swap(cities.begin() + pos1, cities.begin() + pos2);
    
}
