#include <FileHelper.h>

#define MOV_FILE    "movement"
#define RESULT_FILE "results"

bool init_SD() {
    SPI1.setRX(SD_RX);
    SPI1.setCS(SD_SS);
    SPI1.setSCK(SD_CK);
    SPI1.setTX(SD_TX);
    return SD.begin(SD_SS, SPI1);
}

File get_root() {
    return SD.open("/");
}

bool get_movement_file(File* mov) {
    *mov = SD.open(MOV_FILE, FILE_READ);
    return !(*mov);
}

bool create_results_file(File* results) {
    *results = SD.open(RESULT_FILE, FILE_WRITE);
    return !(*results);
}