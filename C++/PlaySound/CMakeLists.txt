cmake_minimum_required(VERSION 3.0)
project (PlaySound) 




#main prog
add_executable(main main.cpp)

target_link_libraries(main winmm.lib)

target_link_libraries(main Winmm.dll)
file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/winmm.dll
     DESTINATION ${CMAKE_CURRENT_BINARY_DIR})

#target_link_libraries(main -lwinmm) #why ?



file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/onEclateClubMixInedit.wav
     DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
