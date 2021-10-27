#pragma once
#include <string>
#include <vector>

#include <iostream> //debug

struct hetD_internalStruct
{
    int d_int;
    std::string d_str;
};

class hetD
{
private:
    std::vector<hetD_internalStruct> *data = new std::vector<hetD_internalStruct>;

public:
    hetD(void);
    ~hetD();

    template <typename T>
    void append(T d);

    hetD_internalStruct pop();
};
