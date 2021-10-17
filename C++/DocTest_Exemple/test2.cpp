#include "doctest.h"
#include "fx2000.hpp"

TEST_CASE("test fx2000 add") {
    CHECK(addXY(5, 5) == 10);
}

TEST_CASE("test fx2000 soustract") {
    CHECK(addXY(5, -5) == 0);
}

TEST_CASE("not error") {
    CHECK( 0 == 0 );
}