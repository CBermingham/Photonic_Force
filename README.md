Using photonic_step_finder.py

This is a program to find the size of the cantilever displacement when the laser is tuened on
and off or the polarisation state is modulated. The steps are located by looking at the TTL signal
of the voltage given to the laser (to turn on and off) or the liquid crystal variable retarder (LCVR) to 
modulate the polarisation state. This is a square wave, 1 Hz (usually) between 0 and 5 V.

The y signal and 'phase' signal needs to be saved from the buttons by the graphs in Labview (I will
make this easier to do). Save the files for 1 run (usually 30s worth of data) in 1 folder and name each
file 'timey' for the y signal and 'timelaser' for the laser signal using whatever time is displayed
in the filename box. Name the folders whatever you have called each run (usually the time of the first
file). Save the data with a calibration of 1 and write down the calibration for each folder of data.

Run the program from the command line. It will ask for the directory to analyse in a file dialog. Then it will ask for the calibration in the command line. The average step size and standard deviation will be output to the command line.

To run the code on a folder of files for 1 run, type:
ydata, laser = data_reader('path/file', calibration)
