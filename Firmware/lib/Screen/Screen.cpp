#include <Screen.h>

void Screen::init() {
    lcd.begin(LCD_NCOL, LCD_NROW);
    uint8_t progress[][8] = {
    { 0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000},
    { 0b10000, 0b10000, 0b10000, 0b10000, 0b10000, 0b10000, 0b10000, 0b10000},
    { 0b11000, 0b11000, 0b11000, 0b11000, 0b11000, 0b11000, 0b11000, 0b11000},
    { 0b11100, 0b11100, 0b11100, 0b11100, 0b11100, 0b11100, 0b11100, 0b11100},
    { 0b11110, 0b11110, 0b11110, 0b11110, 0b11110, 0b11110, 0b11110, 0b11110},
    { 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111}};

    for(uint8_t i = 0; i <= 5; i++) 
        lcd.createChar(i, progress[i]);

    lcd.clear();
}

void Screen::cls() {
    lcd.clear();
    lcd.flush();
}

void Screen::print_wrapped(String text) {
    this->cls();
    int len = text.length();
    if (len > LCD_NCOL) {
        lcd.print(text.substring(0, LCD_NCOL));
        lcd.setCursor(0,1);
        lcd.print(text.substring(LCD_NCOL, len));
    } else {
        lcd.print(text);
    }
}

void Screen::print_line(uint8_t line, String text) {
    lcd.setCursor(0, line);
    lcd.print(text);
}

void Screen::progress_bar(uint8_t line, uint8_t progress) {
    if (progress > 100) progress = 100;

    lcd.setCursor(0, line);

    double d_end = progress*0.13;

    uint8_t end = d_end;

    uint8_t rest = (d_end-end)*5;

    for (uint8_t i = 0; i < end; i++) {
        lcd.write((uint8_t)5);
    }

    lcd.write(rest);

    for (uint8_t i = end; i < LCD_NCOL-4; i++) {
        lcd.write((uint8_t)0);
    }

    if (progress == 100) lcd.print("OK");
    else {
        if (progress < 10) lcd.write((uint8_t)0);

        lcd.print(String(progress)+"%");
    }
}