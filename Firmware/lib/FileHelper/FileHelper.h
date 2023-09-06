#pragma once

#define SD_TX 15
#define SD_RX 8
#define SD_CK 10
#define SD_SS 13

#include <SPI.h>
#include <SD.h>

bool init_SD();
File get_root();
bool get_movement_file(File*);
bool create_results_file(File*);