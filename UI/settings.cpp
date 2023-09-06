#include "settings.h"

Settings* Settings::instance_ = nullptr;

Settings* Settings::instance() {
    if (instance_ == nullptr) {
        instance_ = new Settings();
    }

    return instance_;
}

Settings::Settings() {
    settings_ = new QSettings(QString("config/conf.ini"), QSettings::IniFormat);
}

Settings::~Settings() {
    delete settings_;
}
