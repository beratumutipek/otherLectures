import wfdb
import numpy as np
import matplotlib.pyplot as plt

record = [wfdb.rdrecord(f'{filenames}', sampto=360) for filenames in range(100,103)]
annotation = [wfdb.rdann(f'{filenames}','atr',sampto=360) for filenames in range(100,103)]

data = [record[x].p_signal for x in range(0,3)]
ECG1 = [data[x][:,0] for x in range(0,3)]
ECG2 = [data[x][:,1] for x in range(0,3)]

times = [(np.arange(len(ECG1[x]),dtype=float)/record[x].fs) for x in range(0,3)]

##########################################################
## FUNCTION DEFINITION

def fourier_coefficients(t, signal, num_terms):
    coeffients = []

    for n in range(num_terms):
        an = 2*np.trapz(signal*np.cos(2*np.pi*n*t),t)
        bn = 2*np.trapz(signal*np.sin(2*np.pi*n*t),t)
        coeffients.append((an, bn))

    return coeffients


def reconstruct_signal(t, coeffients):
    signal = np.zeros_like(t)
    individual_terms = []

    for n, (an, bn) in enumerate(coeffients):
        term = an * np.cos(2*np.pi*n*t) + bn*np.sin(2*np.pi*n*t)
        individual_terms.append(term)

        signal += term
    
    return signal, individual_terms

## FUNCTION DEFINITION
##########################################################

##########################################################
## MAIN CODE

num_terms = 100

coefficients = [fourier_coefficients(times[x], ECG1[x], num_terms) for x in range(0,3)]

reconstructed_signal = []
individual_terms = []
for x in range(0,3):    
    a1, b1 = reconstruct_signal(times[x],coefficients[x]) 
    reconstructed_signal.append(a1)
    individual_terms.append(b1)
    
plt.figure(figsize=(15,10))
for x in range(0,3):

    plt.subplot(3,3,1+x*3)
    plt.plot(times[x], ECG1[x], label=f'ECG1-10{x}')
    plt.title('Original Signal')
    plt.xlabel('Time')
    plt.ylabel('Amp')
    plt.legend()

    plt.subplot(3,3,2+x*3)
    for n,term in enumerate(individual_terms[x]):
        plt.plot(times[x], term)
    plt.title(f'Individual Signal-10{x}')
    plt.xlabel('Time')
    plt.ylabel('Amp')

    plt.subplot(3,3,3+x*3)
    plt.plot(times[x], reconstructed_signal[x], label=f'Our ECG1-10{x}')
    plt.title('Reconstructed Signal')
    plt.xlabel('Time')
    plt.ylabel('Amp')
    plt.legend()


plt.tight_layout()
plt.show()


## MAIN CODE
##########################################################