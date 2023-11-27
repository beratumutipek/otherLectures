import wfdb
import numpy as np
import matplotlib.pyplot as plt

record = [wfdb.rdrecord(f'{filenames}', sampto=360) for filenames in range(100,103)]
annotation = [wfdb.rdann(f'{filenames}','atr',sampto=360) for filenames in range(100,103)]

data = [record[x].p_signal for x in range(0,3)]
ECG1 = [data[x][:,0] for x in range(0,3)]
ECG2 = [data[x][:,1] for x in range(0,3)]

times = [(np.arange(len(ECG1[x]),dtype=float)/record[x].fs) for x in range(0,3)]

#########################################################
## FUNCTION DEFINITION


def plot_time_series(signal, time_points, title):
    plt.plot(time_points,signal)
    plt.title(title)
    plt.xlabel('Time (sec)')
    plt.ylabel('Amp')
    plt.grid(True)


def discrete_fourier_transform(signal, sampling_frequency):
    N = len(signal)
    k = np.arange(N)
    n = k.reshape(N,1)
    W = np.exp(-2j * np.pi * k * n / N)
    frequencies = k * sampling_frequency / N
    return frequencies, np.dot(W,signal)

def plot_discrete_fourier_transform(signal, sampling_frequency, title):
    frequencies, fourier_transform = discrete_fourier_transform(signal, sampling_frequency)

    positive_freq_indices = (frequencies >= 0) & (frequencies <= 500)
    plt.plot(frequencies[positive_freq_indices], np.abs(fourier_transform[positive_freq_indices]))
    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid(True)


## FUNCTION DEFINITION
##########################################################

##########################################################
## MAIN CODE
plt.figure(figsize=(15,10))
for x in range(0,3):
    samplingFrequency = record[x].fs



    plt.subplot(3,2,1+2*x)
    plot_time_series(ECG1[x], times[x], f'Times Series Data ECG-10{x}')

    plt.subplot(3,2,2+2*x)
    plot_discrete_fourier_transform(ECG1[x], samplingFrequency,f'DFT Coefficients ECG-10{x}')



plt.tight_layout()
plt.show()
## MAIN CODE
##########################################################