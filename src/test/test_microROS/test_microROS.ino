#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPU6050 mpu;

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    delay(10); // Wait for serial port to connect. Needed for native USB
  }

  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }

  Serial.println("MPU6050 Found!");

  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  Serial.print("AccelX: "); Serial.print(a.acceleration.x); Serial.print(", ");
  Serial.print("AccelY: "); Serial.print(a.acceleration.y); Serial.print(", ");
  Serial.print("AccelZ: "); Serial.print(a.acceleration.z); Serial.print(", ");
  Serial.print("GyroX: "); Serial.print(g.gyro.x); Serial.print(", ");
  Serial.print("GyroY: "); Serial.print(g.gyro.y); Serial.print(", ");
  Serial.print("GyroZ: "); Serial.print(g.gyro.z);
  Serial.println();

  delay(100);
}
