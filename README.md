Using photonic_step_finder.py

This is a program to find the size of the cantilever displacement when the laser is tuened on
and off or the polarisation state is modulated. The steps are located by looking at the TTL signal
of the voltage given to the laser (to turn on and off) or the liquid crystal variable retarder (LCVR) to 
modulate the polarisation state. This is a square wave, 1 Hz (usually) between 0 and 5 V.

The y signal and 'phase' signal needs to be saved from the buttons by the graphs in Labview (I will
make this easier to do). Save the files for 1 run (usually 30s worth of data) in 1 folder and name each
file 'timey' for the y signal and 'timelaser' for the laser signal using whatever time is displayed
in the filename box. Name the folders whatever you have called each run (usually the time of the first
file). Save teh data with a calibration of 1 and write down the calibraiton for each folder of data.

To run the code on a folder of files for 1 run, type:
ydata, laser = data_reader('path/file', calibration)

where ydata and laser will be files that join together all the y and laser data in the correct order
to make one continuous file to analyse (you can call these whatever you like, these are the outputs of the function). 'path/file' is the location and name of the folder you want to analyse. calibration if the calibraiton for that folder of data.

Now you have calibrated data for the entire run as two files, one with the y data and one with the laser 
data. You then need to type:

find_step(ydata, laser) where ydata and laser are the files you have created using the previous function.
The average step and error will be printed to the command line output.
