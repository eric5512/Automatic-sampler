#pragma once

#include <Arduino.h>

#include <Point.h>
  
enum Motor { MOT_X, MOT_Y, MOT_Z };
enum Direction { CW = 0, CCW = 1 };

class MovementHelper {
private:
    const uint8_t PIN_ST    = 0;
    const uint8_t PIN_DIR   = 1;
    const uint8_t PIN_EN_X  = 6;
    const uint8_t PIN_EN_Y  = 7;
    const uint8_t PIN_EN_Z  = 9;

    const uint8_t PIN_BTN_X = 16;
    const uint8_t PIN_BTN_Y = 17;
    const uint8_t PIN_BTN_Z = 22;

    const uint32_t MAX_POS_X = 100;
    const uint32_t MAX_POS_Y = 100;
    uint32_t MAX_POS_Z = 100;

    struct DRV8822_IF {
        uint8_t dir, st, en;
        uint32_t pos, max_pos;
        DRV8822_IF(uint8_t c_dir, uint8_t c_st, uint8_t c_en, uint32_t c_max_pos) : 
            dir(c_dir), st(c_st), en(c_en), pos(0), max_pos(c_max_pos) {
                pinMode(dir, OUTPUT);
                pinMode(st, OUTPUT);
                pinMode(en, OUTPUT);
            };

        bool move(Direction rdir, bool cal) {
            if (!cal) {
                if (rdir == CCW && this->pos >= max_pos 
                || rdir == CW && this->pos <= 0) return false;

                if (rdir == CCW) this->pos++;
                else this->pos--;
            }

            digitalWrite(dir, rdir);
            digitalWrite(en, 0);

            digitalWrite(st, 1);
            digitalWrite(st, 0);

            digitalWrite(en, 1);

            return true;
        }
    };
    
    DRV8822_IF motor_x, motor_y, motor_z;

    uint16_t pos_x, pos_y, pos_z;
    
    MovementHelper() : motor_x(PIN_DIR, PIN_ST, PIN_EN_X, MAX_POS_X),
                       motor_y(PIN_DIR, PIN_ST, PIN_EN_Y, MAX_POS_Y),
                       motor_z(PIN_DIR, PIN_ST, PIN_EN_Z, MAX_POS_Z),
                       pos_x(0), pos_y(0), pos_z(0) {};

    MovementHelper(MovementHelper& other) = delete;
    MovementHelper operator=(MovementHelper& other) = delete;
public:
    static MovementHelper* get_instance();

    bool move(const Motor&, const Direction&);

    bool move(const Motor&, uint16_t);

    bool move(const Point&);

    void origin();

    bool final_x();
    bool final_y();
    bool final_z();
};