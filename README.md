Below is an updated example of a README.md file that reflects the new functionality in your library:

---

# STTS75M2F Python Library

This is a Python library for interfacing with the **STTS75M2F** temperature sensor via the I²C bus. The library provides an easy-to-use API for reading temperature data and configuring the sensor, including advanced features such as:

- **Resolution Setting:**  
  Easily configure the sensor's measurement resolution. Supported modes include 9-bit, 10-bit, 11-bit, and 12-bit (12-bit resolution provides 0.0625°C per unit).

- **Limits & Hysteresis Configuration:**  
  - **High Limit (TOS):** Set an upper temperature limit, so when the measured temperature exceeds this limit, the sensor is set to trigger an alarm on the physical ALERT (O.S./INT) pin.
  - **Hysteresis (THYS):** Configure the hysteresis threshold which functions as a lower bound. When the temperature falls beneath this threshold, the alarm is cleared. In effect, THYS acts as the “reset” point for the alarm.

- **Fault Tolerance:**  
  The library lets you configure the sensor’s fault tolerance—i.e., the number of consecutive faulty readings required before the sensor triggers the alarm output. This is controlled by bits 4 and 3 in the configuration register. You can specify a fault tolerance value of 1, 2, 4, or 6. Higher fault tolerance can help reduce false alarms caused by transient fluctuations or noise.

- **Automatic Stabilization:**  
  On initialization, the library can automatically reset the sensor to its factory defaults and perform a series of dummy reads (with a configurable delay) so that unstable initial readings are discarded. This ensures that you start with a stable and reliable temperature measurement.

## Installation

Install the library using:

```bash
pip install stts75m2f
```

*(Ensure that you have the dependency `smbus2` installed. This library relies on the I²C interface on your platform, such as on a Raspberry Pi.)*

## Usage

Below is a sample code snippet that demonstrates the new functionality, including fault tolerance and hysteresis:

```python
import time
from stts75m2f import STTS75M2F

# Define sensor parameters (in °C)
HIGH_LIMIT = 30.0       # Upper limit (TOS) - when exceeded, the sensor will trigger the alarm via its ALERT pin.
HYSTERESIS = 25.0       # Hysteresis (THYS) - the threshold at which the alarm is cleared.
FAULT_TOLERANCE = 4     # Fault tolerance: the number of consecutive error conditions required before triggering the alarm.

# Initialize the sensor (auto stabilization: e.g., 3 dummy reads with a 1.0 second delay)
sensor = STTS75M2F(auto_stabilize=True, dummy_reads=3, stabilize_delay=1.0)

try:
    # Sensor configuration:
    # Set resolution to 12-bit (0.0625°C per bit)
    sensor.set_resolution(STTS75M2F.RESOLUTION_12BIT)
    
    # Set the upper temperature limit (TOS) and hysteresis (THYS)
    sensor.set_high_limit(HIGH_LIMIT)
    sensor.set_hysteresis(HYSTERESIS)
    
    # Set fault tolerance for the alarm (using bits 4 and 3 in the configuration register)
    sensor.set_fault_tolerance(FAULT_TOLERANCE)
    
    print("Sensor configured:")
    print(" - Resolution: 12-bit")
    print(f" - Upper limit (TOS): {HIGH_LIMIT} °C")
    print(f" - Hysteresis (THYS): {HYSTERESIS} °C")
    print(f" - Fault Tolerance: {FAULT_TOLERANCE} (consecutive errors)")
    print("-" * 50)
    
    while True:
        # Read the current temperature
        temperature = sensor.read_temperature()
        print(f"Current temperature: {temperature:.2f} °C")
        
        # Here, you can implement your control logic:
        # For example, turning on a cooling or heating device if thresholds are exceeded.
        time.sleep(5)

except Exception as e:
    print("Error:", e)

finally:
    sensor.close()
```

### Explanation

- **Initialization and Stabilization:**  
  When you create an instance of `STTS75M2F`, the sensor is automatically reset to factory defaults and stabilized using dummy reads and a delay (if `auto_stabilize=True`).

- **Resolution Setting:**  
  The method `set_resolution()` allows you to select the appropriate resolution (in this example, 12-bit).

- **Limits and Hysteresis:**  
  Use `set_high_limit()` to define the maximum temperature threshold (TOS) and `set_hysteresis()` to set the THYS value which acts as the lower threshold that clears the alarm.

- **Fault Tolerance:**  
  The `set_fault_tolerance()` method configures how many consecutive error conditions must be detected before the sensor triggers an alarm. This minimizes false alarms due to transient noise.

- **Usage Loop:**  
  The script then enters an infinite loop, reading and displaying the current temperature every 5 seconds. You can integrate your desired control logic based on temperature readings.

## Testing

The project includes unit tests:
- **Mock Tests:** Located under `tests/test_stts75m2f_mock.py` allow you to simulate I²C interactions.
- **Real Tests:** Located under `tests/test_stts75m2f_real.py` are intended for devices with the sensor connected.
