// DigiMouse test and usage documentation
// CAUTION!!!! This does click things!!!!!!!!
// Originally created by Sean Murphy (duckythescientist)
#include <DigiMouse.h>


enum states {BEGIN, CLICK, MOTION};
char buf = '\n';
states state = BEGIN;

void setup() {
  Serial.begin(9600);
  DigiMouse.begin(); //start or reenumerate USB - BREAKING CHANGE from old versions that didn't require this
}

void loop() {
  if (Serial.available()) {
    buf = Serial.read();
    switch (state){
      case BEGIN:
        if (buf == 0) {
          state = MOTION;
        }
        else if (buf == 1) {
          state = CLICK;
        }
        break;
        
      case MOTION:
        
        break;

      case CLICK:
        char button = Serial.read();
        char action = Serial.read();
        if (button == 0){              // left button
          if (action == 0) {           // press
            DigiMouse.setButtons(1<<0); // left click
          }
          else if (action == 1) {      // release
            DigiMouse.setButtons(0);   // release
          }
        }
        break;
    }
    }
  
  // If not using plentiful DigiMouse.delay(), make sure to call
  // DigiMouse.update() at least every 50ms
  
  // move across the screen
  // these are signed chars
  DigiMouse.moveY(10); //down 10
  DigiMouse.delay(500);
  DigiMouse.moveX(20); //right 20
  DigiMouse.delay(500);
  DigiMouse.scroll(5);
  DigiMouse.delay(500);
  
  // or DigiMouse.move(X, Y, scroll) works
  
  // three buttons are the three LSBs of an unsigned char
  DigiMouse.setButtons(1<<0); //left click
  DigiMouse.delay(500);
  DigiMouse.setButtons(0); //unclick all
  DigiMouse.delay(500);

  //or you can use these functions to click
  DigiMouse.rightClick();
  DigiMouse.delay(500);
  DigiMouse.leftClick();
  DigiMouse.delay(500);
  DigiMouse.middleClick();
  DigiMouse.delay(500);

  //for compatability with other libraries you can also use DigiMouse.move(X, Y, scroll, buttons)
}
