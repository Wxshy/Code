import matplotlib.pyplot as plt

import seaborn
seaborn.set(style='ticks')

from IPython.display import Audio

import numpy as np
import scipy

import mir_eval

import librosa

#y, sr = librosa.load('C:/Users/samue/Downloads/LUV-MONEY_LONGER.mp3')
y, sr = librosa.load(librosa.util.example_audio_file())

Audio(data=y, rate=sr)

plt.plot(y, sr)
