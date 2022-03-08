from rtlsdr import RtlSdr
import matplotlib.pyplot as plt
import numpy as np

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.4e6 # Hz
#sdr.center_fres = 96.7e6    # Hz  
sdr.freq_correction = 60    # PPM
sdr.gain = 'auto'

for i in range(70, 130, 2):
    sdr.center_freq = i*1e6 #Hz
    samples = sdr.read_samples(256*1024)
    # use matplotlib to estimatee and plot the PSD
    plt.psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)

sdr.close()

plt.xlabel('Frequency (MHz)')
plt.ylabel('Relative power (dB)')
plt.show()
