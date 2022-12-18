# SmartPET feeder

The open-source, easy-to-use feeder

## Installation:

### Requirements:
#### For Raspberry Pi:
+ A Raspberry Pi with Raspberry Pi OS (of course).
+ A touchscreen
+ A outer shell (recommanded because the pet maybe break the machine.)
#### For Espressif ESP32:
+ A Expressif ESP32 module (of course).
#### For other hardware:
+ A stepper motor and a A4988 stepper motor driver.
+ You need 3D-print or some way to make the feeder hardware (the .obj 3D file is in `hardware` directory).
+ Some wires and power supply.
### Install:
#### For Raspberry Pi:
+ Just use `bash raspberry_pi/install.sh`, and it will automatic install.
#### For Espressif ESP32:
+ Please use PlatformIO to open the project and just upload it.


## Contributing:

Open a pull request is welcome for us. But if you want to make bug fixes or major changes such as a new function, etc., please create an issue first.

## License

This project was licensed under GPL v3.0 license. For more detail, please look at the LICENSE file.