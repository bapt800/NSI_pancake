#include <iostream>
#include "fx2000.hpp"

int main(int argc, char **argv)
{
    
    std::cout << "\n Hello Cmake and DocTest \n";

    int16_t x;
    int16_t y;

    std::cin >> x;
    std::cin >> y;
    std::cout << x << " + " << y << " = " << addXY(x, y) << std::endl;
}