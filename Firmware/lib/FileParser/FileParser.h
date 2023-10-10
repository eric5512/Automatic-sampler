#pragma once

#include <FileHelper.h>
#include <Point.h>

struct MovementInfo {
    union {
        struct {
            Point manual_points[20]; // If it's configured in manual mode it uses this array
            uint8_t num_points;
        };
        
        struct { // If it's in automatic mode, it uses this fields
            uint32_t num_points_x;
            uint32_t num_points_y;
            uint32_t num_points_z;
        };
    };

    MovementInfo(): num_points_x(0), num_points_y(0), num_points_z(0), automatic(true) {};

    bool automatic;
};


bool parse_movement_file(MovementInfo *mov);