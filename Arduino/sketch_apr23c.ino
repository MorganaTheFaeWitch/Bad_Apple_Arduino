#include "badapple.h"
#include "Arduino_LED_Matrix.h"

ArduinoLEDMatrix LEDMatrix;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  LEDMatrix.loadSequence(BadApple);
  LEDMatrix.begin();
  LEDMatrix.play(true);
}

void loop() {
  // put your main code here, to run repeatedly:
}
