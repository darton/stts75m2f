# STTS75M2F Python Library

This is a Python library for interfacing with the STTS75M2F temperature sensor using the I2C protocol. The library allows for easy reading of temperature data from the sensor.

## Features

- Read temperature data from the STTS75M2F sensor
- Simple and easy-to-use API

## Requirements

- Python 3.6 or higher
- smbus2 library

## Installation

You can install the library using pip:

```bash
pip install stts75m2f
```

## Usage

```
from stts75m2f import STTS75M2F

# Initialize the sensor
sensor = STTS75M2F()

# Read temperature data
temperature = sensor.read_temperature()

print(f"Temperature: {temperature:.2f} °C")

```
