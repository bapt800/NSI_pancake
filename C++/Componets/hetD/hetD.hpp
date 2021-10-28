#pragma once
#include <string>
#include <vector>

#include <iostream> //debug

template<typename T>
struct hetD_internalStruct
{
    T data;
};


class hetD_internalStruct_virtual //depreciate
{};

class hetD_internalStruct_int : public hetD_internalStruct_virtual //depreciate
{
private:
    int data;
public:
    hetD_internalStruct_int(int value) {data = value;}
    ~hetD_internalStruct_int() {}
};

class hetD_internalStruct_string : public hetD_internalStruct_virtual //depreciate
{
private:
    std::string data;
public:
    hetD_internalStruct_string(std::string value) {data = value;}
    ~hetD_internalStruct_string() {}
};



class hetD
{
private:
    std::vector<hetD_internalStruct_virtual> *stack = new std::vector<hetD_internalStruct_virtual>;

public:
    hetD(void);
    ~hetD(void);

    template <typename T>
    void append(T d);

    template<typename T>
    T pop();

    void FUTUR(void);
};
