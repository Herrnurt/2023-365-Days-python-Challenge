#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 23:23:50 2023

@author: boladipo
"""

## Voice Recorder in Python


# pip install sounddevice

# pip install scipy




# import required modules


import sounddevice

from scipy.io.wavfile import write


# sample_rate
fs = 44100



# Ask to enter the recording time


second = int(input("Enter the Recording Time in second: "))
print("Recording....\n")

record_voice = sounddevice.rec(int(second * fs), samplerate = fs, channels =2)

sounddevice.wait()

write("MyRecording.wav", fs, record_voice)
print("recording is done Please Check your folder to listen to recodring")