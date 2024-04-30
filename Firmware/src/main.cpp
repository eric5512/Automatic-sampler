#include <MovementHelper.h>

extern "C" {
  void setup();
  void loop();
}

MovementHelper *mh = MovementHelper::get_instance();

void setup() {
  mh->origin(); // Get all the motors to 0 position

  // if (mov.automatic)
  //   automatic_movement();
  // else
  //   manual_movement();

  // delay(2000);

  mh->move(MOT_X, CW, 399);
  mh->move(MOT_Y, CW, 10);
}

void loop() {}