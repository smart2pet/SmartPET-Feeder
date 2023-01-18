# SmartPET Feeder
***Please completely read this README. Else you will got many trouble.***
[![CodeQL](https://github.com/smart2pet/SmartPET-Feeder/actions/workflows/codeql.yml/badge.svg)](https://github.com/smart2pet/SmartPET-Feeder/actions/workflows/codeql.yml)  
The open-source, easy-to-use feeder
![Logo](./doc/logo.png "Logo")

## Installation:

### Requirements:
#### For Raspberry Pi:
+ A Raspberry Pi with Raspberry Pi OS (of course).
+ A touchscreen
+ A outer shell (recommand because the pet may break the machine.)
#### For Espressif ESP32:
+ A Espressif ESP32 module.
#### For Other Hardware:
+ A stepper motor that is fit the size of motor in 3D model and a A4988 stepper motor driver. If you can't got the motor fit that, you can also change the model to fit your motor. 
+ The platform of the feeder (You can 3D-print it out. The file is at `other/SmartPET Feeder.obj`)
+ Some wires and power supply.
### Install:
#### For Raspberry Pi:
+ Use `bash raspberry_pi/install.sh` to install the program.
#### For Espressif ESP32:
+ Please use PlatformIO to open the project and upload it to the device.

### Usage
#### Quick Start
+ To use, please follow the instruction.
+ Note that we need setup both esp32 and raspberry pi. 

#### Model Training
+ Don't use my model. You may train your own model because the motor was different. Before training, please look at the comments in `other/train.py` and follow the instruction of the comment. And you need to run `python other/train.py` to train your model.
+ You must convert .h5 hdf5 format to the .tflite tensorflow lite format and replace `raspberry_pi/src/model.tflite` to your model.

#### ESP32 Usage
+ You can use it by write s(rounds); to the serial.

#### Web API Usage
+ Feed: POST /api/food JSON input: {"weight": $your feeding weight}
+ Add plan: POST /api/plan JSON input: {
                                       "time_h": $hour,
                                       "time_m": $minutes,
                                       "weight": $weight
                                       }
+ Delete plan: DELETE /api/plan JSON input:{
                                           "time_h": $hour,
                                           "time_m": $minutes,
                                           }

#### Mobile APP Usage
+ I developed a mobile app (Now just in Android bring it in iOS later). It was simple for now. If you can contribute, 
please contribute to it. Project Address: https://github.com/smart2pet/SmartPETFeederMobile.git. 
## Contributing:
+ We accept and welcome contributes. You can create an issue for reporting bugs. But it's better to solve them by yourself. You just need to 
create an issue for some bugs that you can't resolve or you want to make some new functions. 
+ For more details, please look at CONTRIBUTING.md.

## License
+ This project was licensed under GPL v3.0 license. For more detail, please look at the LICENSE file.

