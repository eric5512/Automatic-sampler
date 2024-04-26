#include <MovementHelper.h>

MovementHelper* MovementHelper::get_instance() {
    static MovementHelper mh;

    return &mh;
}

bool MovementHelper::move(const Motor& mot, const Direction& dir, const coord_t qty) {
    switch (mot) {
    case MOT_X:
        return this->motor_x.move_mm(dir, qty);
    case MOT_Y:
        return this->motor_y.move_mm(dir, qty);
    case MOT_Z:
        return this->motor_z.move_mm(dir, qty);
    }

    return false;
}

bool MovementHelper::move(const Motor& mot, const coord_t coord) {
    DRV8822_IF *moti;
    switch (mot) {
    case MOT_X:
        moti = &this->motor_x;
    case MOT_Y:
        moti = &this->motor_y;
    case MOT_Z:
        moti = &this->motor_z;
    }

    Direction dir;
    coord_t qty;
    if (moti->pos > coord) {
        dir = CCW;
        qty = moti->pos - coord;
    } else {
        dir = CW;
        qty = coord - moti->pos;
    }
    
    return moti->move_mm(dir, qty);
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
    while (!this->final_x())
        this->motor_x.move(CCW);
    for (uint8_t i = 0; i < TICS_TO_MM_X; i++)
        this->motor_x.move(CW);

    while (!this->final_y())
        this->motor_y.move(CCW);
    for (uint8_t i = 0; i < TICS_TO_MM_Y; i++)
        this->motor_y.move(CW);

    while (!this->final_z())
        this->motor_z.move(CW);
    
    uint32_t size_z = 0;
    while (!this->final_z()) {
        this->motor_z.move(CCW);
        size_z++;
    }
    for (uint8_t i = 0; i < TICS_TO_MM_Z; i++)
        this->motor_x.move(CW);

    this->motor_z.move(CW);
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

#undef MOV_DELAY_X
#undef MOV_DELAY_Y
#undef MOV_DELAY_Z
#undef TICS_TO_MM_X
#undef TICS_TO_MM_Y
#undef TICS_TO_MM_Z