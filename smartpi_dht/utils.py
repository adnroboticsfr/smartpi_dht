import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_reading(temperature, humidity):
    if temperature is None or humidity is None:
        logging.error("Invalid readings: Temperature or Humidity is None")
        return False
    if not (-40 <= temperature <= 80):
        logging.error(f"Temperature out of range: {temperature}°C")
        return False
    if not (0 <= humidity <= 100):
        logging.error(f"Humidity out of range: {humidity}%")
        return False
    return True

def format_reading(temperature, humidity):
    return f"Temperature: {temperature:.1f}°C, Humidity: {humidity:.1f}%"

def log_sensor_reading(temperature, humidity):
    if validate_reading(temperature, humidity):
        logging.info(format_reading(temperature, humidity))
    else:
        logging.warning("Invalid sensor data received.")
