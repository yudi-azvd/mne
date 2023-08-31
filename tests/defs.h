#pragma once

#include "doctest.h"

#define approx(x) (doctest::Approx(x))
#define approx_eps(x, e) (doctest::Approx(x).epsilon(e))