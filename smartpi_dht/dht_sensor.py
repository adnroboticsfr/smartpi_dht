import Adafruit_DHT
import time

class DHTSensor:
    def __init__(self, sensor_type="DHT22", pin=4):
        """
        Initialize the sensor.
        :param sensor_type: Sensor type ("DHT11" or "DHT22").
        :param pin: GPIO pin to which the sensor is connected.
        """
        self.sensor = Adafruit_DHT.DHT22 if sensor_type == "DHT22" else Adafruit_DHT.DHT11
        self.pin = pin

    def read(self):
        """
        Reads the temperature and humidity from the sensor.
        :return: A tuple (temperature, humidity), or (None, None) if reading fails.
        """
        humidity, temperature = Adafruit_DHT.read(self.sensor, self.pin)
        if humidity is not None and temperature is not None:
            return temperature, humidity
        else:
            return None, None

    def read_continuous(self, interval=2):
        """
        Continuously reads the temperature and humidity from the sensor at a set interval.
        :param interval: Time in seconds between readings.
        """
        try:
            while True:
                temp, humidity = self.read()
                if temp is not None and humidity is not None:
                    print(f"Temp={temp:.1f}°C  Humidity={humidity:.1f}%")
                else:
                    print("Failed to retrieve data from the sensor")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Terminating sensor reading.")
