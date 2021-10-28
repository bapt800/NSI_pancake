#include "hetD.hpp"

hetD::hetD(void)
{
}

hetD::~hetD(void)
{
    delete stack;
}

template <typename T>
void hetD::append(T d)
{
    std::cout << "hetD::append() T-> type != (int or str or char)";
}

template <>
void hetD::append<int>(int d)
{
    hetD_internalStruct_int buff(d);

    stack->push_back(buff);
}

template <>
void hetD::append<std::string>(std::string d)
{
    hetD_internalStruct_string buff(d);

    stack->push_back(buff);
}

template <>
void hetD::append<const char *>(const char *d)
{
    hetD_internalStruct_string buff(d);

    stack->push_back(buff);
}

template<typename T>
T hetD::pop()
{
    hetD_internalStruct_string data_internal = stack->back();

    stack->pop_back();
    return data_internal;
}

void hetD::FUTUR(void)
{
    std::cout << stack->back().data << std::endl;
}