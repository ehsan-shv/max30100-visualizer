A Python-Flask and SocketIO-based app for real-time visualization of MAX30100 sensor data in the browser, displaying heart rate and SpO2 measurements with interactive charts.

## How to run:

1.  Download the [MAx30100 lib](https://github.com/oxullo/Arduino-MAX30100) in the Arduino IDE and upload the minimal example to your Arduino board.
2.  Close the Arduino IDE, install the required Python dependencies, and then run the Python application:

```bash
	python app.py
```

4.  Open `http://127.0.0.1:8000` in your browser.

## How Max30100 works:

The MAX30100 is a compact sensor module designed for pulse oximetry and heart rate monitoring. It operates by emitting light from two LEDs—one red and one infrared—into the skin. A photodetector measures the intensity of light that is reflected back or transmitted through the tissue. The red light is more sensitive to oxygenated blood, while the infrared light responds to changes in blood volume.

By analyzing the variations in light absorption, the sensor can determine heart rate and blood oxygen saturation (SpO2). These measurements rely on the periodic changes caused by the heart's pumping action, which alters the blood volume in the vessels.

The module communicates with a microcontroller via the I2C protocol, offering ease of integration into various systems. It also features low power consumption, making it suitable for wearable devices. Proper calibration, signal filtering, and temperature compensation are essential to ensure accurate readings, as noise and environmental factors can affect the sensor's performance.
