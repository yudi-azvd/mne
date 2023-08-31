#pragma once

#include <math.h>

#define MAX_ITER 10000

// https://iq.opengenus.org/typedef-function-pointer-c/#:~:text=The%20keyword%20typedef%20is%20used,us%20by%20C%2FC%2B%2B.
typedef float (*Function)(float);

#define ERR_ABS(a, b) (abs(a - b))        // a > b
#define ERR_REL(a, b) ((a - b) / (a + b)) // a > b

float root_bisection(Function f, float x1 = 0.0, float x2 = 1.0, float rel_err = 0.01);

float root_regula_falsi(Function f, float x1 = 0.0, float x2 = 1.0, float rel_err = 0.01);