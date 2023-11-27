import wfdb
import numpy as np
import matplotlib.pyplot as plt
import pywt

record = [wfdb.rdrecord(f'{filenames}', sampto=360) for filenames in range(100,103)]
annotation = [wfdb.rdann(f'{filenames}','atr',sampto=360) for filenames in range(100,103)]

data = [record[x].p_signal for x in range(0,3)]
ECG1 = [data[x][:,0] for x in range(0,3)]
ECG2 = [data[x][:,1] for x in range(0,3)]

wavelet = 'db4'
level = 5

signal_length = [len(ECG1[x]) for x in range(0,3)]

coeffs1 = [pywt.wavedec(ECG1[x],wavelet,level=level) for x in range(0,3)]
coeffs2 = [pywt.wavedec(ECG2[x],wavelet,level=level) for x in range(0,3)]

time_values = []

for x in range(0, 3):
    temp_list = []
    
    for coef in coeffs1[x]:
        temp_list.append(np.linspace(0,signal_length[x], len(coef), endpoint=False))
    
    time_values.append(temp_list)


timesRealECG = [np.arange(len(ECG1[x]),dtype=float) for x in range(0,3)]

# visualize the wavelet coefficient

plt.figure(figsize=(15,10))
for x in range(0,3):
    plt.subplot(3,2,1+2*x)
    plt.plot(timesRealECG[x],ECG1[x], label=f'Real ECG1-10{x}')

    for i, coef in enumerate(coeffs1[x]):
        plt.plot(time_values[x][i],coef + i*2,label=f'Level{i}')

    plt.title(f'Wavelet Coeffients - ECG1-10{x}')
    plt.legend()

    plt.subplot(3,2,2+2*x)
    plt.plot(timesRealECG[x],ECG2[x], label=f'Real ECG1-10{x}')

    for i, coef in enumerate(coeffs2[x]):
        plt.plot(time_values[x][i],coef + i*2,label=f'Level{i}')

    plt.title(f'Wavelet Coeffients - ECG2-10{x}')
    plt.legend()

plt.tight_layout()
plt.show()
