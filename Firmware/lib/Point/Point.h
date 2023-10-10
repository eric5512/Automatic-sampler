#pragma once

#include <inttypes.h>

struct Point {
    uint16_t x;
    uint16_t y;
    uint16_t z;

    Point(uint16_t x_c, uint16_t y_c, uint16_t z_c): x(x_c), y(y_c), z(z_c) {};
    Point(): x(0), y(0), z(0) {};
};