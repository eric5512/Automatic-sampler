#pragma once

#define LCD_RS 12
#define LCD_EN 11
#define LCD_D4 5
#define LCD_D5 4
#define LCD_D6 3
#define LCD_D7 2

#define LCD_NCOL 16
#define LCD_NROW 2

#include <LiquidCrystal.h>

class Screen {
private:
    LiquidCrystal lcd;
    void init();
public:
    Screen() : lcd(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7) { this->init(); };
    void cls();
    void print_wrapped(String);
    void print_line(uint8_t, String);
    void progress_bar(uint8_t, uint8_t);
};