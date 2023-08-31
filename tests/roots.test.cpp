#include "doctest.h"

#include "roots.h"
#include "test_defs.h"

float sqrt_of_2(float x) {
    return x * x - 2.0;
}

float sqrt_of_4(float x) {
    return x * x - 4.0;
}

TEST_CASE("bisection") {
    CHECK(approx_eps(1.41406, 0.01) == root_bisection(sqrt_of_2, 0, 2));
    CHECK(approx_eps(1.41, 0.01) == root_bisection(sqrt_of_2, 0, 2));

    CHECK(approx_eps(2, 0.1) == root_bisection(sqrt_of_4, 0.0, 4.1));
}

TEST_CASE("bisection exact root") {
    // FIXME: se o primeiro chute cai certinho na raíz, 2 por exemplo, 
    // f(2) == 0, não é positivo nem negativo. O teste fica "indefinido".
    // Deveria ter o teste sign(f(root)) == 0: return root;
    CHECK(approx_eps(2, 0.1) == root_bisection(sqrt_of_4, 0.0, 4.0));
}