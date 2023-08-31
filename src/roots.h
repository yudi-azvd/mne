#pragma once

// https://iq.opengenus.org/typedef-function-pointer-c/#:~:text=The%20keyword%20typedef%20is%20used,us%20by%20C%2FC%2B%2B.
typedef float (*Function)(float);

float root_bisection(Function f) {
    return (*f)(0.2);
}