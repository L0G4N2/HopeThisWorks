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
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"

using namespace vex;

int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();
  Motor11.setVelocity(50, percent);
  while (true) {
    wait(20, msec);
    if (Controller1.ButtonA.pressing()) {
      Motor11.spinFor(forward, 180, degrees);
    }
    else if (Controller1.ButtonB.pressing()) {
      Motor11.spinFor(reverse, 180, degrees);
    }
    
  }
}
