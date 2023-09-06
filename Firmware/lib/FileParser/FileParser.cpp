#include "FileParser.h"

bool parse_movement_file(Movement *mov) {
    File file;
    char buffer[240];

    get_movement_file(&file);

    file.readBytes(buffer, 1);

    if (*buffer == 0) {
        mov->automatic = 0;
        
        file.readBytes(buffer, sizeof(uint8_t));
        mov->num_points = *buffer;

        file.readBytes(buffer, sizeof(uint32_t)*mov->num_points*3);
        for (size_t i = 0; i < mov->num_points; i++) {
            mov->manual_points[i].x = *(((uint32_t*)buffer)+i*3);
            mov->manual_points[i].y = *(((uint32_t*)buffer)+i*3+1);
            mov->manual_points[i].z = *(((uint32_t*)buffer)+i*3+2);
        }
        
    } else {
        mov->automatic = 1;
        file.readBytes(buffer, sizeof(uint32_t)*3);
        mov->num_points_x = *(((uint32_t*)buffer));
        mov->num_points_y = *(((uint32_t*)buffer)+1);
        mov->num_points_z = *(((uint32_t*)buffer)+2);
    }

    file.close();
    return false;
}