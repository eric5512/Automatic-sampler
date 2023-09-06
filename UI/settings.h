#ifndef SETTINGS_H
#define SETTINGS_H

#include <QSettings>

class Settings {
public:
    void read_file();
    void write_file();
    static Settings* instance();

    Settings(Settings &other) = delete;
    void operator=(const Settings &) = delete;
private:
    Settings();
    ~Settings();
    static Settings* instance_;
    QSettings* settings_;
    int parts_x_;
    int parts_y_;
    int parts_z_;
};

#endif // SETTINGS_H
