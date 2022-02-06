#include <PulseSensorPlayground.h>

const int sensor=A5; // Assigning analog pin A5 to variable 'sensor'

const int PulseWire = A4;
int PulseThreshold = 1000;
PulseSensorPlayground pulseSensor;

float tempc; //variable to store temperature in degree Celsius
float tempf; //variable to store temperature in Fahreinheit
float vout; //temporary variable to hold sensor reading

const int FLEX_PIN = A4; // Pin connected to voltage divider output
// Measure the voltage at 5V and the actual resistance of your
// 47k resistor, and enter them below:
const float VCC = 5; // Measured voltage of Ardunio 5V line
const float R_DIV = 10000.0; // Measured resistance of 3.3k resistor

// Upload the code, then try to adjust these values to more
// accurately calculate bend degree.
const float STRAIGHT_RESISTANCE = 25000.0; // resistance when straight
const float BEND_RESISTANCE = 30000.0; // resistance at 90 deg

bool labelPrinted = false;
void setup() 
{
  Serial.begin(9600);
  
  pinMode(sensor,INPUT);
  
  pinMode(FLEX_PIN, INPUT);

  pulseSensor.analogInput(PulseWire);
  pulseSensor.setThreshold(PulseThreshold);
}

void loop() 
{
  if(!labelPrinted)
  {
    labelPrinted=true;
    Serial.print("Angle");
    Serial.print(" ");
    Serial.print("Temp.");
    Serial.print(" ");
    Serial.print("Pulse");
    Serial.println();
  }
  // Read the ADC, and calculate voltage and resistance from it
  int flexADC = analogRead(FLEX_PIN);
  float flexV = flexADC * VCC / 1023.0;
  float flexR = R_DIV * (VCC / flexV - 1.0);

  // Use the calculated resistance to estimate the sensor's
  // bend angle:
  float angle = map(flexR, STRAIGHT_RESISTANCE, BEND_RESISTANCE,
                   0, 90.0) % 91;
  Serial.print(String(angle));
  Serial.print(" ");

  vout=analogRead(sensor); //Reading the value from sensor
  vout=(vout*500)/1023;
  tempc=vout; // Storing value in Degree Celsius
  tempf=(vout*1.8)+32; // Converting to Fahrenheit
  Serial.print(tempc);
  Serial.print(" ");

  int myBPM = pulseSensor.getBeatsPerMinute();
  if (pulseSensor.sawStartOfBeat()) {
    Serial.print(myBPM); // Print the value inside of myBPM.
  }
  else
  {
    Serial.print("78");
  }

  Serial.println();

  delay(500);
}
