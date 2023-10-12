#pragma once

#include <Arduino.h>

#include <Point.h>
  
enum Motor { MOT_X, MOT_Y, MOT_Z };
enum Direction { CW = 0, CCW = 1 };

#define MOV_DELAY 1
#define TICS_TO_MM 159

class MovementHelper {
private:
    const uint8_t PIN_ST    = 0;
    const uint8_t PIN_DIR   = 1;
    const uint8_t PIN_EN_X  = 9;
    const uint8_t PIN_EN_Y  = 7;
    const uint8_t PIN_EN_Z  = 6;

    const uint8_t PIN_BTN_X = 16;
    const uint8_t PIN_BTN_Y = 17;
    const uint8_t PIN_BTN_Z = 22;

    const coord_t MAX_POS_X = 400;
    const coord_t MAX_POS_Y = 177;
    coord_t MAX_POS_Z = 0;


    struct DRV8822_IF {
        uint8_t dir, st, en, end;
        uint32_t pos, max_pos;
        DRV8822_IF(uint8_t c_dir, uint8_t c_st, uint8_t c_en, uint8_t c_end, uint32_t c_max_pos) : 
            dir(c_dir), st(c_st), en(c_en), end(c_end), pos(0), max_pos(c_max_pos) {
                pinMode(dir, OUTPUT);
                pinMode(st, OUTPUT);
                pinMode(en, OUTPUT);

                pinMode(end, INPUT_PULLUP);

                digitalWrite(en, 1);
            };

        void move(Direction rdir) {
            digitalWrite(dir, rdir);
            digitalWrite(en, 0);

            digitalWrite(st, 1);
            delay(MOV_DELAY);
            digitalWrite(st, 0);
            delay(MOV_DELAY);

            digitalWrite(en, 1);
        }

        bool move_mm(Direction rdir, coord_t dist_mm) {
            // if (rdir == CCW && this->pos >= max_pos 
            //     || rdir == CW && this->pos <= 0) return false;

            if (rdir == CCW) this->pos++;
            else this->pos--;

            digitalWrite(dir, rdir);
            digitalWrite(en, 0);

            for (coord_t j = 0; j < dist_mm; j++) {
                for (uint8_t i = 0; i < TICS_TO_MM; i++) {
                    digitalWrite(st, 1);
                    delay(MOV_DELAY);
                    digitalWrite(st, 0);
                    delay(MOV_DELAY);
                }
            }

            digitalWrite(en, 1);

            return true;
        }

        bool final_mot() {
            return !digitalRead(end);
        }
    };
    

    uint16_t pos_x, pos_y, pos_z;
    
    MovementHelper() : motor_x(PIN_DIR, PIN_ST, PIN_EN_X, PIN_BTN_X, MAX_POS_X),
                       motor_y(PIN_DIR, PIN_ST, PIN_EN_Y, PIN_BTN_Y, MAX_POS_Y),
                       motor_z(PIN_DIR, PIN_ST, PIN_EN_Z, PIN_BTN_Z, MAX_POS_Z),
                       pos_x(0), pos_y(0), pos_z(0) {};

    MovementHelper(MovementHelper& other) = delete;
    MovementHelper operator=(MovementHelper& other) = delete;

public:
    DRV8822_IF motor_x, motor_y, motor_z;
    static MovementHelper* get_instance();

    bool move(const Motor&, const Direction&, const coord_t);

    bool move(const Motor&, const coord_t);

    bool move(const Point&);

    void origin();

    bool final_x();
    bool final_y();
    bool final_z();
};