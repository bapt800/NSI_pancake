cmake_minimum_required(VERSION 3.0)
project (DocTest_Exemple) 

enable_testing()

add_library(doctest_implement OBJECT doctest_implement.cpp)

add_executable(test1 test1.cpp $<TARGET_OBJECTS:doctest_implement>)
add_test(NAME test1 COMMAND test1)

add_executable(test2 test2.cpp $<TARGET_OBJECTS:doctest_implement>)
add_test(NAME test2 COMMAND test2 )





#main prog
add_executable(main main.cpp hetD.cpp)

