"""
Created on Tue Nov  6 14:34:13 2018

The data was recorded using AndroSensor mobile app
The data is imported and visualized via pandas and matplotlib libraries
The code extracts and analyzes 3 pieces of information
    1. Number of Steps (2 sections)
    2. Number of Squats
    3. Number of Jumps

All features are extracted from 'features_data2,csv'

@author: anggyemmanuc
"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
DATA_FIELD = pd.read_csv("Data_task2.csv")

def peak_bounds(lower_bound, upper_bound, column, threshold):
    """Calculate peak points within given range and threshold.
        Inputs:
            lower_bound: integer, starting of data to analize (sample no.)
            upper_bound: integer, ending of data to analize (sample no.)
            column: string, name of the column in the csv file
            threshold: integer, range in amplitud to analize
        Return:
            peak: list of peaks within the given range
    """
    filtered_data = DATA_FIELD[column].iloc[lower_bound:upper_bound]
    peak, _ = find_peaks(filtered_data, height=threshold)
    return peak

ACC_X = DATA_FIELD["ACCELEROMETER X (m/s²)"]
ACC_Y = DATA_FIELD["ACCELEROMETER Y (m/s²)"]
ACC_Z = DATA_FIELD["ACCELEROMETER Z (m/s²)"]
TIME = DATA_FIELD["Time since start in ms "]

PEAKS, _ = find_peaks(ACC_Y, height=(-3, 1))
plt.figure(figsize=(10, 10))

plt.plot(TIME, ACC_X, 'g')
plt.plot(TIME, ACC_Y, 'b--')
plt.plot(TIME, ACC_Z, 'r-.')
plt.legend(loc='upper left')

plt.title("Accelerometer vs. Time")
plt.xlabel("Time (ms)")
plt.ylabel("Accelerometer Values (m/s^2)")
plt.show()

DATA_FIELD['ACC_RMS'] = np.sqrt(DATA_FIELD['ACCELEROMETER X (m/s²)']**2 + DATA_FIELD['ACCELEROMETER Y (m/s²)']**2 + DATA_FIELD['ACCELEROMETER Z (m/s²)']**2)

JUMPS = peak_bounds(0, 1488, 'ACC_RMS', 16)
NUM_JUMPS = int(len(JUMPS)/2)

WALKING_1 = peak_bounds(0, PEAKS[0], 'ACCELEROMETER Y (m/s²)', (-7, -3.5))
WALKING_1 = WALKING_1[0:-1]

SQUATS = PEAKS[0:NUM_JUMPS]
NUM_SQUADS = len(SQUATS)

WALKING_2 = peak_bounds(SQUATS[-1], JUMPS[0], 'ACCELEROMETER Y (m/s²)', (-7, -3.5))
WALKING_2 = WALKING_2[1:-1]

plt.figure(figsize=(10, 10))
plt.plot(ACC_Y)
plt.plot(PEAKS, ACC_Y[PEAKS], "x")
plt.plot(SQUATS, ACC_Y[SQUATS], "x")
plt.plot(WALKING_1, ACC_Y[WALKING_1], "x")
plt.title("Accelerometer Y vs. Time")
plt.xlabel("Time (ms)")
plt.ylabel("Accelerometer Values (m/s^2)")
plt.show()

print("\nNumber of steps during first walk:", len(WALKING_1)*2)
print("Walking time (sec): ", (TIME[WALKING_1[len(WALKING_1)-1]]-TIME[WALKING_1[0]])/1000)

print("\nNumber of squats perfornmed:", NUM_SQUADS)
print("Squats time (sec): ", (TIME[SQUATS[-1]]-TIME[SQUATS[0]])/1000)

print("\nNumber of steps during second walk:", len(WALKING_2)*2)
print("Walking time (sec): ", (TIME[WALKING_1[-1]]-TIME[WALKING_2[0]])/1000)

print("\nNumber of jumps perfornmed:", NUM_JUMPS)
print("Jumping time (sec): ", (TIME[JUMPS[-1]]-TIME[JUMPS[0]])/1000)
