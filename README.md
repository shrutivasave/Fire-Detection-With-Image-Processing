# Fire-Detection-With-Image-Processing
## PREFACE
In recent times, there have been several instances of fires all across the world. The collateral
damage caused by these incidents negatively impact humans as well as nature. Due to this, the
need for application for fire detection has increased in recent years.
Traditional fire detection systems utilize light, heat and gas sensors, each with their own
strengths and drawbacks. However, there are several situations where these systems are
impractical to implement, either due to cost, power or other practical reasons.
## PROPOSED SETUP (PROJECT OBJECTIVE)
Through this course research project, we aim to construct a fire detection system based on
image processing techniques which can be implemented in existing surveillance devices like
CCTV, wireless camera and UAVs.
## SOFTWARE TECHNOLOGY
We have chosen to implement our fire detection algorithm using the python programming
language. The Open Computer Vision library is utilized as it provides straightforward and
convenient methods for all the procedures in our algorithm. We generate a Custom HAAR
Cascade Classifier trained using 1600 images, obtained from ImageNet.
## ALGORITHM
The first step is to obtain our training images. We use ImageNet to download 1000 “positive”
images (images containing fire) and 1700 “negative” images (images not containing fire).
The next step is to generate a Custom Haar Cascade Classifier. This process extracts features
from positive and negative images and creates an XML file, which is used later in the process.
Although this can be done in the command line interface with Open Computer Vision, ding so is
extremely tedious and hence we employ a program known as Cascade Trainer GUI to construct
the file.
![Cascade Trainer GUI](https://github.com/ollyollyupnfree/Fire-Detection-With-Image-Processing/blob/main/GUI.JPG)
Cascade Trainer GUI
Meanwhile, we also create a python program to accept live video feed from an attached
camera. Built using Open Computer Vision functions, this script will be able to execute
operations on individual frames while still delivering real time results.
After obtaining the Custom Haar Cascade Classifier file, we integrate it into our python
program. The module compares each frame of the video using our classifier, and when a fire is
detected, a variety of alarms can be triggered, ranging from visual to audio.
