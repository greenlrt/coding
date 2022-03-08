from rtlsdr import RtlSdr

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.048e6   # Hz
sdr.center_freq = 96.7e6    # Hz
sdr.freq_correction = 60    # PPM
sdr.gain = 'auto'

print(sdr.read_samples(512))
