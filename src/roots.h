#pragma once

#include <math.h>

#define MAX_ITER 10000

// https://iq.opengenus.org/typedef-function-pointer-c/#:~:text=The%20keyword%20typedef%20is%20used,us%20by%20C%2FC%2B%2B.
typedef float (*Function)(float);

#define ERR_ABS(a, b) (abs(a - b))        // a > b
#define ERR_REL(a, b) ((a - b) / (a + b)) // a > b

float root_bisection(Function f, float x1 = 0.0, float x2 = 1.0, float rel_err = 0.01) {
    uint iterations = 0;
    float root = 0;
    float f_x1 = 0;

    // while (ERR_ABS(x2, x1) > abs_err && iterations < MAX_ITER) {
    while (ERR_REL(x2, x1) > rel_err && iterations < MAX_ITER) {
        root = (x1 + x2) / 2;

        if (f(root) == 0)
            return root;

        if (f(x1) * f(root) < 0) {
            x2 = root;
        } else {
            x1 = root;
        }

        iterations++;
    }

    return root;
}