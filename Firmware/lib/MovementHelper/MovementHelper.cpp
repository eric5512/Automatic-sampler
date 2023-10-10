#include <MovementHelper.h>

MovementHelper* MovementHelper::get_instance() {
    static MovementHelper mh;

    return &mh;
}

bool MovementHelper::move(const Motor& mot, const Direction& dir) {
    switch (mot) {
    case MOT_X:
        return this->motor_x.move(dir, false);
    case MOT_Y:
        return this->motor_y.move(dir, false);
    case MOT_Z:
        return this->motor_z.move(dir, false);
    }

    return false;
}

bool MovementHelper::move(const Motor& mot, const coord_t coord) {
    return false; // TODO: move motor to coordinate
}

bool MovementHelper::move(const Point& point) {
    if (!this->move(MOT_X, point.x)) 
        return false;

    if (!this->move(MOT_Y, point.y)) 
        return false;

    if (!this->move(MOT_Z, point.z)) 
        return false;

    return true;
}

void MovementHelper::origin() {
    while (this->final_x()) {
        this->motor_x.move(CCW, true);
    }
    this->motor_x.move(CW, true);

    while (this->final_y()) {
        this->motor_y.move(CCW, true);
    }
    this->motor_y.move(CW, true);

    while (this->final_z()) {
        this->motor_z.move(CW, true);
    }
    uint32_t size_z = 0;
    while (this->final_z()) {
        this->motor_z.move(CCW, true);
        size_z++;
    }
    this->motor_z.move(CW, true);
    this->MAX_POS_Z = size_z;
}

bool MovementHelper::final_x() {
    return this->motor_x.final_mot();
}

bool MovementHelper::final_y() {
    return this->motor_y.final_mot();
}

bool MovementHelper::final_z() {
    return this->motor_z.final_mot();
}
