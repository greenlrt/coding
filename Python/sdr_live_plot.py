from rtlsdr import RtlSdr
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.4e6 # Hz
#sdr.center_freq = 96.7e6    # Hz  
sdr.center_freq = 100.7e6   # Hz
sdr.freq_correction = 60    # PPM
sdr.gain = 'auto'

fig = plt.figure()
graph_out = fig.add_subplot(1, 1, 1)

def animate(i):
    graph_out.clear()
    samples = sdr.read_samples(128*1024)
    # use matplotlib to estimatee and plot the PSD
    graph_out.psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6,
                    Fc=sdr.center_freq/1e6)

try:
    ani = animation.FuncAnimation(fig, animate, interval=10)
    plt.show()
except KeyboardInterrupt:
    pass
finally:
    sdr.close()
