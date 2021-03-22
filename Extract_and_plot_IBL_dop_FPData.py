import numpy as np
from numpy import save
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

file_location = "/Volumes/witten/Alex/Data/Subjects/fip_13/2021-03-08/001/alf/"
trial_num = 100

#Fluo Times 
load_fluo = np.load(file_location + "_ibl_fluo.times.npy")
df_fluo = pd.DataFrame(load_fluo)

#Load Trial intervals 
load_intervals = np.load(file_location + "_ibl_trials.intervals.npy")
timestamps  = pd.DataFrame(load_intervals, columns=['start','stop'])

#FrameRate Conversion 
length_of_fluo = len(load_fluo)
End_of_recording = timestamps['stop'].tail(1)
FR_conv = length_of_fluo / End_of_recording

#Trial interval variable 
start_point = int(timestamps['start'].iloc[trial_num] * FR_conv)
stop_point = int(timestamps['stop'].iloc[trial_num] * FR_conv)

#DLS fluo data
load_DLS = np.load(file_location + "_ibl_trials.DLS.npy")
df_DLS = pd.DataFrame(load_DLS)

#DMS fluo data 
load_DMS = np.load(file_location + "_ibl_trials.DMS.npy")
df_DMS = pd.DataFrame(load_DMS)

#NAcc fluo data 
load_NAcc = np.load(file_location + "_ibl_trials.NAcc.npy")
df_NAcc = pd.DataFrame(load_NAcc)

#GoCue Times
load_cueTimes = np.load(file_location + "_ibl_trials.goCue_times.npy")
cue_Time = pd.DataFrame(load_cueTimes)
cue_point = int(cue_Time[0].iloc[trial_num] * FR_conv)

#Response Times
load_responseTimes = np.load(file_location + "_ibl_trials.response_times.npy")
response_Time = pd.DataFrame(load_responseTimes)
response_point = int(response_Time[0].iloc[trial_num] * FR_conv)

#Feedback Times 
load_feedbackTimes = np.load(file_location + "_ibl_trials.feedback_times.npy")
feedback_Time = pd.DataFrame(load_feedbackTimes)
feedback_point = int(feedback_Time[0].iloc[trial_num] * FR_conv)

#Movement Times 
load_movementTimes= np.load(file_location + "_ibl_trials.firstMovement_times.npy")
movement_Time = pd.DataFrame(load_movementTimes)
movement_point = int(movement_Time[0].iloc[trial_num] * FR_conv)

plt.plot(df_DLS.iloc[start_point:stop_point], label='DLS')
plt.plot(df_DMS.iloc[start_point:stop_point], label='DMS')
plt.plot(df_NAcc.iloc[start_point:stop_point], label ='NAcc')
plt.axvline(cue_point, color = 'g', linestyle='--', label='GoCue')
plt.axvline(movement_point, color = 'r', linestyle='--', label='MoveTime')
#plt.axvline(response_point)
plt.axvline(feedback_point, color = 'b', linestyle='--', label='Feedback')
plt.legend()



