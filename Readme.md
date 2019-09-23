# RPi Tank

Coding of the control system for a model tank with **Raspberry Pi**. 
The project is divide into 4 sections:

> 1. __Keyboard Controlled RPi tank with _Remote Desktop Connection_ into the Raspberry Pi.__
> 2. __Keyboard Controlled RPi tank with _Network Sockets_.__
> 3. __RPi Tank video streaming via _Network Sockets_ and _http_.__
> 4. __Line following RPi tank using **OpenCV**.__

## LineFollowing in ACTION!🤖:joystick:

<img src="readmeImages/tank.gif" height="500" width="375">

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you'll need in terms of Software and Hardware and how to install them:

### Harware required

- ***1. Raspberry Pi (Model 3 onwards recommended)***	
- ***2. MotoZero PCB***
- ***3. Power Supply (5V Power Bank)***
- ***4. Pi Camera Module V2***

### Libraries

The list of libraries that are required are stated below:

```
1. GPIOZERO Library - A simple interface to GPIO devices with Raspberry Pi.

  pip install gpiozero
  
2. Pynput Library - Keyboard event handling Library for Tank's controls.
  
  pip install pynput
  
3. Pi Camera - This package provides a pure Python interface to the Raspberry Pi camera module for Python 2.7 (or above) or Python 3.2 (or above).  

  pip install picamera
  
4. OpenCV - Unofficial pre-built OpenCV packages for Python.

  pip install opencv-python
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the RPi Tank:

***The final setup of the RPi tank looks something like*** :arrow_double_down:

![](readmeImages/finalTank.jpg)

***Sample Tracks for RPi Tank*** :arrow_double_down:

<img src="readmeImages/Track.jpg" width="650">

### :arrow_forward: Executing Programmes associated.

_Follow the script execution cycle below:_

**1. Sprint 1 - Raspberry Pi and Tank/**  
  - &emsp; &emsp; `cursesRobot.py`: _Remote Desktop Connect_ to the Pi and run the script on the Pi terminal as<br /> 
   &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;  &emsp; &emsp;  curses module only runs on terminal window. This establishes <br /> 
   &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;  &emsp; &emsp;keyboard RPi Tank controls.
  
**2. Sprint 2 - RPi controlled tank via Sockets/**    
  - &emsp; &emsp; `pynputRobotClient.py`: Socket client program that runs on the RPi.<br /> 
  - &emsp; &emsp; `pynputRobotClient.py`: Socket server program that runs on the Local Machine ready for keyboard inputs.<br /> 
     
**3. Sprint 3 - PiCamera and OpenCV/**  
  - &emsp; &emsp;  `robotCameraClient.py`: Socket client program that runs on the RPi for live video streaming.<br /> 
  - &emsp; &emsp; `robotCameraServer.py`: Socket server program that runs on the Local Machine Playing streamed video.<br /> 
  - &emsp; &emsp;  **httpCamera/**  
      &emsp; &emsp;  &emsp; &emsp; `httpCamer.py`: Run the script to create the http server on the Pi. Now on the Local Machine<br /> 
      &emsp;&emsp; &emsp;&emsp; &emsp; &emsp; &emsp; &emsp;  &emsp; &emsp;search for Pi's IP and the video stream will be available on the webpage. <br /> 
  
**4. Sprint 4 - Line following RPi Tank/**   
  - &emsp; &emsp; `lineRobotClient.py`: Socket client program for line Following RPi tank.<br /> 
  - &emsp; &emsp; `lineRobotServer.py`: Socket server program for line Following RPi tank.<br /> 
      
## Built With

* [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) - OS for Raspberry Pi
* [Python](https://www.python.org/) - Primary Programming Language.
* [PyCharm](https://www.jetbrains.com/pycharm/) - The IDE used for Develpment and the _Recommended._

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
