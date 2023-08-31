#pragma once

#include <math.h>

#define MAX_ITER 10000

// https://iq.opengenus.org/typedef-function-pointer-c/#:~:text=The%20keyword%20typedef%20is%20used,us%20by%20C%2FC%2B%2B.
typedef float (*Function)(float);

float root_bisection(Function f, float x1 = 0.0, float x2 = 1.0, float abs_err = 0.01) {
    uint iterations = 0;
    float root = 0;

    while (abs(x2 - x1) > abs_err && iterations < MAX_ITER) {
        root = (x1 + x2)/2;
        if (f(x1) * f(root) < 0) {
            x2 = root;
        } else {
            x1 = root;
        }

        iterations++;
    }

    return root;
    // return 0;
}