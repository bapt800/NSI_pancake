#include <iostream>
#include "hetD.hpp"

int main(int argc, char **argv)
{
    
    std::cout << "\n --> START <-- \n";

    hetD data_garbage;

    data_garbage.append(65);
    data_garbage.append("ee");
    

    std::cout << data_garbage.pop().d_str << std::endl;
    std::cout << data_garbage.pop().d_int << std::endl;


}