/*
  Analog input, analog output, serial output
 
 Reads an analog input pin, maps the result to a range from 0 to 255
 and uses the result to set the pulsewidth modulation (PWM) of an output pin.
 Also prints the results to the serial monitor.
 
 The circuit:
 * potentiometer connected to analog pin 0.
   Center pin of the potentiometer goes to the analog pin.
   side pins of the potentiometer go to +5V and ground
 * LED connected from digital pin 9 to ground
 
 created 29 Dec. 2008
 modified 9 Apr 2012
 by Tom Igoe
 
 This example code is in the public domain.
 
 */

// These constants won't change.  They're used to give names
// to the pins used:
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
const int analogOutPin = 9; // Analog output pin that the LED is attached to

int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)
int i = 0;
void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600); 
}
//91.5
void loop() {
  while(i > 112500000){}
  int sample1 = (map(analogRead(analogInPin), 0, 1023, 0, 255) > 91);
  delay(0.5);
  int sample2 = (map(analogRead(analogInPin), 0, 1023, 0, 255) > 91);
  if(sample1 > sample2){
    Serial.print("0");
    i++;
  }
  else if(sample1 < sample2){
    Serial.print("1");
    i++;
  }
  delay(0.5);
  // wait 2 milliseconds before the next loop
  // for the analog-to-digital converter to settle
  // after the last reading:             
}
