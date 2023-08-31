#include <math.h>

#include "roots.h"

float root_bisection(Function f, float x1, float x2, float rel_err) {
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
// False posição
float root_regula_falsi(Function f, float x1, float x2, float rel_err) {
    uint iterations = 0;
    float xi = 0;
    float f_x1 = 0;

    while (ERR_REL(x2, x1) > rel_err && iterations < MAX_ITER) {
        // xi = (x2 * f(x1) - x1 * f(x2)) / (f(x1) - f(x2));
        // menos avaliação de funções:
        xi = x2 - f(x2) * (x2 - x1) / (f(x2) - f(x1));

        if (f(x1) * f(xi) < 0) {
            x2 = xi;
        } else {
            x1 = xi;
        }

        iterations++;
    }

    return xi;
}