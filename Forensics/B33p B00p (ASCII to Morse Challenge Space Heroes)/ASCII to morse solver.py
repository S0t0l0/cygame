import os
import sys
import wavio
import numpy as np
from scipy.signal import butter, sosfiltfilt, hilbert

# function to create a bandpass filter using Butterworth filter
def butter_bandpass(low_freq, high_freq, fs, order=5):
    nyq = 0.5 * fs
    low = low_freq / nyq
    high = high_freq / nyq
    sos = butter(order, [low, high], btype='band', output='sos')
    return sos

# function to apply a bandpass filter to a signal
def bandpass_filter(d, low, high, fs, order=5):
    sos = butter_bandpass(low, high, fs, order=order)
    y = sosfiltfilt(sos, d)
    return y

# function to implement sliding window technique
def sliding_window(d, window_size):
    return np.convolve(d, np.ones(window_size), 'valid')

# function to decode Morse code signal from binary signal
def decode_morse_signal(signal, dot, dash, space, threshold):
    morse = ""
    i = 0
    while i < len(signal):
        if signal[i] > threshold:
            count = 0
            # count the number of samples in a signal pulse
            while i < len(signal) and signal[i] > threshold:
                count += 1
                i += 1

            # determine if the pulse is a dot or a dash
            if count < (dot + dash) / 2:
                morse += '.'
            else:
                morse += '-'
        else:
            count = 0
            # count the number of samples in a signal space
            while i < len(signal) and signal[i] <= threshold:
                count += 1
                i += 1

            # determine if the space is a word space or a character space
            if count >= space:
                morse += ' '

    return morse

# read the wav file
wav_data = wavio.read(r"C:\Users\deady\OneDrive\Desktop\capturedmessage.wav")
rate = wav_data.rate
data = wav_data.data[:, 0]

# apply bandpass filter to the signal
filtered_data = bandpass_filter(data, 190, 210, rate)

# Create an envelope of the filtered data using the Hilbert transform
envelope = np.abs(hilbert(filtered_data))
binary_signal = np.where(envelope > np.mean(envelope), 1, 0)

# calculate the duration of dot, dash, and space based on the signal rate
dot_duration = int(rate * 0.05)
dash_duration = int(rate * 0.10)
space_duration = int(rate * 0.15)

# decode the Morse code from the binary signal
morse_code = decode_morse_signal(binary_signal, dot_duration, dash_duration, space_duration, 0.5)

# convert Morse code to binary string
binary_string = morse_code.replace('-', '1').replace('.', '0')

# convert binary string to ASCII string
ascii_string = ''
for binary_char in binary_string.split():
    decimal_value = int(binary_char, 2) # Convert binary string to decimal value
    ascii_char = chr(decimal_value) # Convert decimal value to ASCII character
    ascii_string += ascii_char # Add the ASCII character to the final string

# print the ASCII string
print(ascii_string)