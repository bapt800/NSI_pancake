#include "doctest.h"
#include <unistd.h>


SCENARIO("sleep 1 second") {

  GIVEN("a one second sleep duration") {
    unsigned int duration =1 ;

    WHEN("call sleep with this duration") {
      int ret = sleep(duration) ;

      THEN("it's expected nobody interupted our rest") {
        CHECK(ret == 0);
      }
    }
  }
} 

SCENARIO("sleep 2 second") {

  GIVEN("a 2 second sleep duration") {
    unsigned int duration = 2 ;

    WHEN("call sleep with this duration") {
      int ret = sleep(duration) ;

      THEN("it's expected nobody interupted our rest") {
        CHECK(ret == 0);
        
      }
      AND_THEN("")
      {
        CHECK(0 == 0);
      }
    }
  }
} 
