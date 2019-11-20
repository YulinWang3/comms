#define NUMBER_OF_TESTS 40
float value = 0;
// Motor variables
#define STEPS 2048
float stepDelay = 0;

//Temp variables
float Celcius = 0.0;
float Fahrenheit = 0.0;

//Turbidity variables
float voltage, turbidity;
//

//pH variables
float pHVolt, pHValue;
void setup() {
  Serial.begin(9600);

}

void loop() {
  int i;
  for (i = 1; i < 7; i++) {
    runMotor(i);
  }
  for (i = 1; i < 7; i++) {
    runMotor(-i);
  }

  delay(2000);

  for (int i = 0; i < NUMBER_OF_TESTS; i++) {
    value = random(0, 175);
    CollectTemperature(value / 100);
    delay(100);
  }

  delay(2000);

  for (int i = 0; i < NUMBER_OF_TESTS; i++) {
    value = random(477, 798);
    CollectTurbidity(value);
    delay(100);
  }

  delay(2000);
  
  for (int i = 0; i < NUMBER_OF_TESTS; i++) {
    value = random(264, 766);
    CollectpH(value);
    delay(100);
  }

  delay(2000);
  
}




void runMotor(int speed) {
  Serial.print("The motor now has a speed of ");
  Serial.print(speed);
  Serial.println(" RPM (Rotations per minute)");
  //delay(3000);
  // Step delay is the amount of time for one full revolution of the motor.
  // 2048 steps / rev
  //
  stepDelay = 60L * 1000L * 1000L / (STEPS * abs(speed));

  if (speed > 0) {
    Serial.println("The motor is now moving clockwise");
    delay(stepDelay);
    Serial.println("The motor has now stopped.");
  }  else {
    Serial.println("The motor is now moving counter clockwise");
    delay(stepDelay);
    Serial.println("The motor has now stopped.");
  }
  delay(1000);
}

// digitalVoltage is is volts
void CollectTemperature(float digitalVoltage) {
  //Start fetching temperature
  // Convert the digital voltage to a temperature
  Celcius = (digitalVoltage - 0.500) / 0.010;
  //Convert the temperature to fahernheit
  Fahrenheit = Celcius * 9 / 5 + 32;

  // Print out the values
  Serial.print("Temperature: ");
  Serial.print(Celcius);
  Serial.print("*C  ");
  Serial.print(Fahrenheit);
  Serial.println("*F  ");
}

float ADCvoltage(float sensorVoltage) {
  return sensorVoltage * (5.0 / 1024);
}

void CollectpH(float analogVoltage) {
  pHVolt = ADCvoltage(analogVoltage);
  pHValue = -5.70 * pHVolt + 21.34; //formuala to convert voltage to a pH value
  Serial.print("pH: ");
  Serial.println(pHValue);


}

void CollectTurbidity(float analogVoltage) {
  voltage = ADCvoltage(analogVoltage);
  turbidity = (-1120.4 * (voltage + 0.3) * (voltage + 0.3)) + (5742.3 * (voltage + 0.3)) - 4352.9; //in NTU - convert the voltage to Nephelometric Turbidity unit.(0=clear; 3000= very turbid)
  if ((voltage >= 1.5) & (turbidity >= 0)) {
    Serial.println("Voltage=" + String(voltage) + " V Turbidity=" + String(turbidity) + " NTU");
  }
}
