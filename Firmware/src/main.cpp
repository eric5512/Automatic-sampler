#include <MovementHelper.h>

#define BAUD_RATE 9600

extern "C" {
  void setup();
  void loop();
}

MovementHelper *mh = MovementHelper::get_instance();

void setup() {
  Serial.begin(BAUD_RATE); // Init serial communication

  mh->origin(); // Get all the motors to 0 position
}

void loop() {
  if (Serial.available() > 2) {
    String msg = Serial.readString();
    Motor mot;
    bool res;

    switch (msg[0]) {
      case 'X':
        mot = MOT_X;
        break;
      
      case 'Y':
        mot = MOT_Y;
        break;
      
      case 'Z':
        mot = MOT_Z;
        break;
      
      default:
        Serial.print('0');
        return;
    }

    coord_t dist;
    if (msg[1] == '+') { // If number begins with + or - the movement is relative, if not, it's absolute
      dist = msg.substring(2).toInt();
      res = mh->move(mot, CW, dist);
    } else if (msg[1] == '-') {
      dist = msg.substring(2).toInt();
      res = mh->move(mot, CCW, dist);
    } else {
      dist = msg.substring(1).toInt();
      res = mh->move(mot, dist);
    }

    Serial.print(res ? '1' : '0');
  }
}