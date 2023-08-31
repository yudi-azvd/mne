#include "doctest.h"

#include "roots.h"
#include "test_defs.h"

float f(float x) {
    return x * x - 2;
}

TEST_CASE("bisection") {
    CHECK(approx(1.41406) == root_bisection(f, 0, 2));
    
    CHECK(approx_eps(1.41, 0.1) == root_bisection(f, 0, 2));
}
