# Physical Training Helper Based on Electromyography and Acceleration-orientation Data

## Authors: Yanchen CHENG, Xiangwei MENG (Contributing equally)

## Abstract
With the development and progress of society, people are more and more inclined to exercise at home, or indoor sports. When you exercise alone or at home, you need an objective feedback to track your performance and point out if you exercise correctly. Among the devices that have helped us solve this problem are step counters, as well as heartbeat and blood pressure sensors. Now, one of the methods we have developed to analyze movement is EMG. It is through specific muscle EMG signal processing, intuitive analysis of your movement. EMG signal is produced by muscle contraction, which can be analyzed to get instructions to the computer. The technique is also used in prosthetics and rehabilitation.

EMG permits to estimate the level of muscle contraction and therefore provide such information as velocity and number of repetitions, level of fatigue, load distribution across muscles. When coupled with an inertial measurement unit data (accelerations and orientation), it can become powerful information source. The goal of this project is to implement a Python based program that allows users to control the mouse cursor by contracting the muscles of their hands. A software for collecting EMG signal from EMG arm band is designed by using Python language. Through the use of EMG and IMU acquisition equipment (myo arm band), python programming language and signal processing technology to achieve such a system prototype. We can start by counting the number of repetitions of hand exercises, such as push ups, and then do more complex analysis.

## Requirements
- **OS**: Operation System(s) the project can run on
- **Languages**: Programming languages used in the project
- **Dependancies**: packages, libraries, data required for the project but defined outside of it (examples: numpy, matplotlib, rosserial)
- Python 3
- myo-python
- numpy
- scikit-learn
- scipy
- matplotlib
- keyboard
- pyserial

## Introduction
### MYO
Myo this magic wristband detects the bioelectricity changes of the muscles on the arm when the user moves, and cooperates with the physical action monitoring of the arm to do human-computer interaction. With a wristband, you can control your mobile device like a Jedi. Myo set a specific action to start the device, just like Google glass's "OK, glass", and this action is not usually done by normal people. Myo uses Bluetooth 4.0 to connect to smart devices. Now it supports Mac OS and windows. In the future, it will launch APIs adapted to IOS and Android for developers to further invent all kinds of fun things. In 2013, Canadian startup Thalmic Labs launched an innovative armband MYO wristband (gesture control armband). This gesture control armband can be worn above the elbow joint of any arm to detect electrical activity generated by the user's muscles. It wirelessly connects with other electronic products through low-power Bluetooth devices to sense the user's actions.
<div align=center><img width="400" src="pictures/myo01.png"/></div> 
<div align=center><img width="400" src="pictures/myo02.jpg"/></div> 

With the development of detection technology and signal processing methods, it has become one of the hot issues in biomedical and medical circles to use sEMG instead of needle electrode EMG in the comprehensive clinical nondestructive diagnosis. The sEMG of human body is very weak and easy to be disturbed, and it is difficult to measure. How to collect and extract sEMG effectively has become one of the key technologies in SEMG application. According to the neurophysiological knowledge, muscle action potential will produce a potential difference of -90mv to 30mV, because the human body is the poor conductor of electricity (1mΩ the peak value of about 1mV can be obtained from the patch electrode of the body surface. According to the literature, the interference signals of very low frequency (close to DC) and high frequency are often mixed in sEMG, while the effective spectrum of EMG signals is distributed between 10-500hz. Therefore, the signal detected from the patch electrode needs to be processed by high pass filtering (straight processing), high magnification, low-pass filtering (filtering out high frequency interference) and other signal conditioning processes.
<div align=center><img width="400" src="pictures/myo03.jpg"/></div> 
<div align=center><img width="400" src="pictures/myo04.jpg"/></div> 
<div align=center><img width="800" src="pictures/myo05.jpg"/></div> 

### Generating principle of EMG signal
The formation principle of physiological layer model: To better simulate the EMG model, we need to further understand the production process of EMG. The specific process can be described as follows: when the muscle is stimulated, an action potential (IAP) will be generated in the cell membrane, and the action potential will be generated at the neuromuscular junction and conduct along the muscle fiber to both sides of the muscle. In the process of conduction, single fiber action potential (SEAP) is produced on a single muscle fiber. The same motor unit is composed of many fibers, which is called motor unit (MU). After a series of electrical activities of tissue structure, it produces motor unit action potential (MUAP), which is filtered by a series of volume conductors such as muscle, fat and skin, final detection on skin surface.
<div align=center><img width=800" src="pictures/emg01.png"/></div> 

MUAP waveform: MU is composed of SEAP of all muscle fibers of the same motor unit superimposed on the skin surface. It contains a motor neuron and all the muscle fibers it innervates. Its range is a circular area in this paper, but the distribution of Mu spacing is not consistent. Motor units are always recruited in increasing order of α-motor neuron size. There is a positive correlation between the recruitment order of a single MU, peak amplitude and twitch tension, AKA "normal recruitment sequence" or "orderly recruitment". The recruitment and firing frequency (rate coding) of the motor unit mainly depends on the size of the force and the speed of contraction. The number of MU recruited and its average firing frequency determine the electrical activity in the muscle, that is, the same factors determine muscle strength. Therefore, a direct relationship between electromyography (EMG) and applied force can be expected. In human muscle, such as fiber type, these relationships are difficult to quantify, so it is difficult to build realistic models based on conditional probability model of parameters. Therefore, the simplest method is to make these parameters statistically independent. For the same mu, the waveform detected by the electrode moving step size of 10 mm each time is shown in Fig. 5. It can be determined from the figure that the muscle fiber which can affect the EMG signal detected by the surface electrode in practice should be very close to the detection electrode.
<div align=center><img width=800" src="pictures/emg05.png"/></div> 

Before the simulation of motor unit action potential waveform, it is necessary to study the characteristics of motor unit recruitment and release. The motor unit of neuromuscular is closely related to the stimulation of muscle in the process of recruitment and release, and the control mode of motor unit is different for different muscle groups.
The surface EMG signal can be measured with wet electrodes and dry electrodes. Commonly used wet electrodes need to add conductive electrolyte gel or sponge between the electrode and the skin, but they can provide high-quality surface EMG signals. Wet electrodes usually require shaving or wiping treatment on the skin surface, which can reduce skin electrode impedance and movement artifacts. However, wet electrodes may not be suitable for long-term use at the surface EMG interface, because the drying of the conductive gel can cause irritation and cause skin discomfort, and potentially cause skin allergies and inflammation. However, modern dry electrodes do not require conductive gel and skin pretreatment, and can still achieve signal quality comparable to wet electrodes. Therefore, dry electrodes may be more suitable for surface EMG interfaces
When the muscle is stimulated, the Mu is activated when the input stimulation reaches its own recruitment threshold. According to the experimental statistics, the threshold RTE of Mu in biceps brachii obeys the exponential distribution, as shown in the formula.
<div align=center><img width=200" src="pictures/emg04.png"/></div> 

### MAV
MAV(mean absolute value) describes the proportional control of the force and speed feedback power hook, the speed control when allowing free movement and the force control when grasping. The features used are amplified, rectified and smoothed electrode signals. The MAV of two pairs of electrodes were compared, and the differential signal was used to turn on and off the prosthetic hand. In order to reduce the output noise, a backlash generator is introduced.
In addition, Fougner proposed a linear mapping function. The angle estimation is tested and compared with MLP network. A much simpler linear mapping function is almost as good as MLP networks. Together with ANN, support vector machine (SVM), locally weighted projection regression (LWPR) and physiology based model (PBM), Ziai tested a similar solution (called ordinary least squares linear regression) for torque estimation. Compared with other more complex estimators, linear mapping has the characteristics of short training time and good effect.
An important part of the training of prosthetic control system is to combine the training data sets in an appropriate way. We have seen that in the clear classification version of pattern recognition, the composition of training data is very important for robustness. In the case of proportional control, there is no reason to believe that training data is not so important. Of course, the training set of proportional control should contain continuous movement, that is, not just rest and maximum contraction. If only the on / off action is trained, the system may finally realize the on-off control.
For the system with proportional control at the same time, unless some interpolation method is used, the training data must contain simultaneous motion.
<div align=center><img width=400" src="pictures/mav01.png"/></div> 

### IMU signal acquisition system
1.IMU signal acquisition system takes arm and FPGA as the core, realizes high-precision time through GPS and high stability crystal, collects real-time data of 3-axis accelerometer and 3-axis gyroscope through high-precision AD conversion module, and finally outputs high-precision sensor data with time stamp, which lays a solid foundation for the realization of POS system. 
The main functions of IMU signal acquisition system are high-precision time acquisition and data acquisition of gyroscope and accelerometer. The system combines GPS, high stability quartz crystal, FPGA as the core, combined with effective algorithm to produce high-precision time (precision up to ±10uS). At the same time, the output signals of gyroscope (three-axis), accelerometer (three-axis) and other sensors are collected by FPGA and AD conversion module. The gyroscope and accelerometer are digitized and filtered. Finally, the data with time stamp and output of each sensor are quickly uploaded to the upper computer according to the set time interval for further processing.

2.Planning: The whole hardware system is composed of arm, FPGA, three-axis gyroscope, three-axis accelerometer, GPS and other sensor units, power management module, flash and SDRAM, and single board computer. FPGA mainly receives the digital signals of gyroscope and accelerometer after AD conversion, encoder and GPS signals to complete the output data acquisition of high-precision clock and sensor. Arm stores the data signal collected by FPGA and receives the high-precision time pulse output by FPGA. After stamping the sensor signal with high-precision time stamp, it quickly uploads it to the single board computer through USB or UART. The single board computer outputs the position, time and attitude information after a series of processing such as Kalman filter.
<div align=center><img width=400" src="pictures/imu01.png"/></div> 
IMU is mostly used in motion control equipment, such as cars and robots. It is also used in the situation of precise displacement calculation with attitude, such as inertial navigation equipment of submarine, aircraft, missile and spacecraft. Therefore, in general, IMU should be installed on the center of gravity of the object to be measured.

## Architecture
<div align=center><img width=600" src="pictures/flowchart.png"/></div> 

## Examples
### Installation and setup
#### 1. Install Anaconda. 
Download a Python 3.7 Anaconda from the [official site](https://www.anaconda.com/products/individual) and install it. Use default installation options.
#### 2. Install MyoConnect. 
Install MyoConnect from the provided setup file: [Windows](https://www.dropbox.com/s/2dfv0gpqq0c2qrp/Myo_Connect_Installer.exe?dl=0), [MacOS](https://www.dropbox.com/s/ua43z9n2rib4hv3/MyoConnect.dmg?dl=0).
To connect and use the armband, please follow the official tutorial within MyoConnect.
Later, to set up MyoConnect for a comfortable work, run it, then right-click on its icon in task bar, select **Preferences**, and uncheck all options in all tabs. Then, right-click on icon again, select **Application Manager** and uncheck all options here too.
#### 3. Create a new python 3.8 virtual environment (explained for Anaconda).
On Windows, open **anaconda prompt**. On MacOS, run **Terminal**. Run the following commands and accept the changes:
```
conda create --name myo python=3.8 pip
```
Now activate the environment that we have just created (its name is '**myo**'):
```
conda activate myo
```
Note: please remember that any time you want to run this project from a new command/terminal window, you need to activate this environment again.
#### 4. Install *myo-python* package
Install it from from our fork on Github. To do so, in command line, with 'myo' environment activated, run:
```
pip install https://github.com/smetanadvorak/myo-python/tarball/master
```
#### 5. Setup the *fm_myo_barebones* package
[Download](https://github.com/smetanadvorak/fm_myo_barebones/tarball/master)
this project and put it in an appropriate directory on your disk. In command window, navigate to this project's folder and run:
```
pip install -e .
```
#### 6. Set up MyoConnect
This should be done only once at the beginning of your working session:
- Insert MYO's Bluetooth dongle in your USB port.
- Run MyoConnect, right-click on its icon in task bar, select **Armband Manager** ....
- Approach the dongle with your armband. It should automatically get paired with MyoConnect.
- In MyoConnect, press 'Ping' to make sure that it is not connected to some other armband nearby. Your armband should vibrate in response to the ping.

#### 7. Setup the environment and run the code
Open **Anaconda Prompt** (Windows) or **Terminal** (MacOS) and activate the 'myo' environment:
```
conda activate myo
```
Navigate to the folder with this package, then to ./examples/streaming and run a test script:
```
python streaming.py
```
If everything is installed correctly, a matplotlib figure should appear with the EMG signals being traced in real time. This and other examples can be stopped by either pressing **ctrl-c** (MacOS) or **shift-c** (Windows).phy-based Mouse Pointer Control with Python

### Run the codes
Back to this folder,
```
python mav.py
```
