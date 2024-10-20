# SmartPi DHT Sensor Package

The `smartpi_dht` package provides a direct interface for reading data from DHT11/DHT22 temperature and humidity sensors connected to a Smart Pi One (or Raspberry Pi). This package interacts directly with GPIO registers, without relying on external libraries like `RPi.GPIO` or `Adafruit_DHT`. It also includes additional utility functions for logging, validation, and formatting sensor data.

## Features

- Read temperature and humidity from DHT11 or DHT22 sensors.
- Continuous sensor readings with customizable intervals.
- Utility functions for validation and logging.
- No external library dependencies.

---

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Uninstallation](#uninstallation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Continuous Reading](#continuous-reading)
- [Wiring Instructions](#wiring-instructions)
- [Utilities](#utilities)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Requirements

- Smart Pi One or Raspberry Pi.
- DHT11 or DHT22 sensor.
- Python 3.6+.
- Jumper wires and a 10kΩ resistor.

---

## Installation

To install the `smartpi_dht` package, follow these steps:

1. **Ensure Python 3 is installed on your system**:

   If Python is not already installed, you can install it using:

   ```bash
   sudo apt-get install python3 python3-pip
   ```

2. **Download and install the `smartpi_dht` package**:

   Clone the package repository:

   ```bash
   git clone https://github.com/adnroboticsfr/smartpi_dht.git
   cd smartpi_dht
   ```

   Then install the package using `pip`:

   ```bash
   pip3 install .
   ```

---

## Uninstallation

To remove the package, run the following command:

```bash
pip3 uninstall smartpi_dht
```

---

## Usage

After installation, you can easily use the `smartpi_dht` package in your Python scripts.

### Basic Usage

Here’s a simple example of reading temperature and humidity once:

```python
from smartpi_dht import DHTSensor

# Initialize the sensor (DHT22 on GPIO4)
sensor = DHTSensor(sensor_type="DHT22", pin=4)

# Read temperature and humidity once
temperature, humidity = sensor.read()

# Check if the reading was successful
if temperature is not None and humidity is not None:
    print(f"Temperature: {temperature:.1f}°C, Humidity: {humidity:.1f}%")
else:
    print("Failed to retrieve data from the sensor")
```

### Continuous Reading

You can continuously read the sensor data at a set interval (e.g., every 2 seconds):

```python
from smartpi_dht import DHTSensor

# Initialize the sensor (DHT22 on GPIO4)
sensor = DHTSensor(sensor_type="DHT22", pin=4)

# Start continuous reading (reads every 2 seconds)
sensor.read_continuous(interval=2)
```

---

## Wiring Instructions

### DHT11/DHT22 Sensor Pinout

- **VCC**: Connect this to the 3.3V or 5V pin of the Smart Pi One.
- **GND**: Connect this to the GND pin of the Smart Pi One.
- **DATA**: Connect this to a GPIO pin (e.g., GPIO4).
- **10kΩ Resistor**: Place the pull-up resistor between the data pin and the VCC pin for stable readings.

### Example Wiring Diagram

(Include a wiring diagram here, if available)

---

## Utilities

The package includes useful utility functions located in `utils.py` for logging, validation, and formatting sensor data.

### Logging and Validation Example

```python
from smartpi_dht import DHTSensor
from smartpi_dht.utils import log_sensor_reading

# Initialize the sensor (DHT22 on GPIO4)
sensor = DHTSensor(sensor_type="DHT22", pin=4)

# Read and log the sensor data
temperature, humidity = sensor.read()
log_sensor_reading(temperature, humidity)
```

This function will validate the readings and log the data in a user-friendly format. Invalid readings (e.g., out-of-range values) will be flagged in the logs.

---

## Troubleshooting

- **No Data from Sensor**: Ensure the wiring is correct and that the pull-up resistor is placed between the data pin and VCC.
- **Incorrect Readings**: Verify that you have selected the correct sensor type (`DHT11` or `DHT22`) when initializing the `DHTSensor` object.
- **Permissions Issue**: If you encounter permissions issues accessing the GPIO pins, try running the Python script with `sudo`:

  ```bash
  sudo python3 your_script.py
  ```

- **Timing Issues**: The DHT sensor uses precise timing. If you experience unreliable readings, check that the system is not overloaded or experiencing high CPU usage.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```


