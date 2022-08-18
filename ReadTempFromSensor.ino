/*
    using chinese clone of arduino nano
    MPU6050 sensor hooked up to arduino nano over i2c bus
    arduino nano hooked up to PC via USB cable
*/

#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() 
{
  Serial.begin(115200);

  while(!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G))
  {
    Serial.println("sensor disconnected");
    delay(500);
  }
}

void loop()
{
  float temp = mpu.readTemperature();

  //Serial.print(" Temp = ");
  Serial.println(temp);
  //Serial.println(" *C");
  
  delay(60000);
}
