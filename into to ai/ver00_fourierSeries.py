import numpy as np
import matplotlib.pyplot as plt


def square_wave(t, frequency, amplitude = 1.0):
    return amplitude*(1+ np.sign(np.sin(2*np.pi*frequency*t)))/2