#include "doctest.h"

#include "roots.h"
#include "test_defs.h"
#include "functions.h"


TEST_CASE("regula falsi") {
    CHECK(approx_eps(1.41406, 0.01) == root_false_position(sqrt_of_2, 0, 2));
    CHECK(approx_eps(1.41, 0.01) == root_false_position(sqrt_of_2, 0, 2));

    CHECK(approx_eps(2, 0.1) == root_false_position(sqrt_of_4, 0.0, 4.1));
}

TEST_CASE("regula falsi exact root") {
    CHECK(approx_eps(2, 0.1) == root_false_position(sqrt_of_4, 0.0, 4.0));
}