#include <Screen.h>
#include <FileParser.h>
#include <MovementHelper.h>

#define PIN_BTN 27

extern "C" {
  void setup();
  void loop();
}

void automatic_movement();
void manual_movement();

Screen screen = Screen();

MovementHelper *mh = MovementHelper::get_instance();

Movement mov;

void setup() {
  screen.print_wrapped("Initializing...");
  
  pinMode(PIN_BTN, INPUT_PULLDOWN);

  if (!parse_movement_file(&mov)) {
    screen.print_wrapped("Error, SD not connected or mov file not found");
    while(1);
  }

  screen.print_wrapped(String("Measurement in ") + (mov.automatic ? "automatic" : "manual") + " mode");

  while(!digitalRead(PIN_BTN)); // Wait until the button is pressed

  mh->origin(); // Get all the motors to 0 position

  if (mov.automatic)
    automatic_movement();
  else
    manual_movement();

  screen.print_wrapped("Done");
}

void loop() {}

void automatic_movement() {

}

void manual_movement() {
  screen.print_line(0, "Press button to move");

  for (size_t i = 0; i < mov.num_points; i++) {
    screen.print_line(1, String(i) + '/' + String(mov.num_points) + " points");
    while(!digitalRead(PIN_BTN));
    mh->move(mov.manual_points[i]);
  }

  screen.print_wrapped("Done");
}