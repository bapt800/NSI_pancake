#include "hetD.hpp"

hetD::hetD(void)
{
}

hetD::~hetD()
{
    delete data;
}

template <typename T>
void hetD::append(T d)
{
    std::cout << "hetD::append() T-> type != (int or str or char)";
}

template <>
void hetD::append<int>(int d)
{
    hetD_internalStruct buff;

    buff.d_int = d;

    data->push_back(buff);
}

template <>
void hetD::append<std::string>(std::string d)
{
    hetD_internalStruct buff;

    buff.d_str = d;

    data->push_back(buff);
}

template <>
void hetD::append<const char*>(const char* d)
{
    hetD_internalStruct buff;

    buff.d_str = std::string(d);

    data->push_back(buff);
}

hetD_internalStruct hetD::pop()
{
    hetD_internalStruct data_internal = data->back();

    data->pop_back();
    return data_internal;
}