#include "doctest.h"
#include "roots.h"

#include "defs.h"

float f(float x) {
    return x;
}

TEST_CASE("bisection") {
    CHECK(root_bisection(f) == doctest::Approx(0.2));
    CHECK(root_bisection(f) == approx(0.2));
    CHECK(root_bisection(f) == approx_eps(0.2, 0.1));
}
