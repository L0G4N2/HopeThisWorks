/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       C:\Users\c86mj                                            */
/*    Created:      Tue Mar 25 2025                                           */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// Controller1          controller                    
// Motor11              motor         11              
// Rotation12           rotation      12              
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"

using namespace vex;

int turnPosition = 0;

void greenLight() {
  Motor11.spin(forward);
  wait(380, msec);
  Motor11.stop(hold);
}

void redLight() {
  Motor11.spin(reverse);
  wait(380, msec);
  Motor11.stop(hold);
}

int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();
  // srand(Brain.Timer.systemHighResolution());
  // int randomNumber = rand() % 5 + 1;
  Motor11.setVelocity(50, percent);
  Rotation12.setPosition(0, degrees);
  Rotation12.resetPosition();
  // switch (randomNumber) {
  //   case 1:
  //     greenLight();
  //     wait(750, msec);
  //     redLight();
  //   case 2:
  //     greenLight();
  //     wait(1000, msec);
  //     redLight();
  //   case 3:
  //     greenLight();
  //     wait(1250, msec);
  //     redLight();
  //   case 4:
  //     greenLight();
  //     wait(1900, msec);
  //     redLight();
  //   case 5:
  //     greenLight();
  //     wait(2000, msec);
  //     redLight();
  // }
  while (true) {
    wait(250, msec);
    if (Controller1.ButtonA.pressing() && (Rotation12.angle(degrees) >= 335 || Rotation12.angle(degrees) < 25)) {
      Motor11.spin(forward);
      wait(380, msec);
      Motor11.stop(hold);
    }
    if (Controller1.ButtonB.pressing() && (Rotation12.angle(degrees) >= 155 && Rotation12.angle(degrees) <= 215)) {
      Motor11.spin(reverse);
      wait(380, msec);
      Motor11.stop(hold);
    }
  }
}
