#pragma once

#include <FileHelper.h>
#include <Point.h>

struct Movement {
    union {
        Point manual_points[20]; // If it's configured in manual mode it uses this array
        struct { // If it's in automatic mode, it uses this fields
            uint32_t num_points_x;
            uint32_t num_points_y;
            uint32_t num_points_z;
        };
    };

    uint8_t num_points;
    bool automatic;
};


bool parse_movement_file(Movement *mov);