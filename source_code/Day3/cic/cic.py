import matplotlib.pyplot as plt
import numpy as np
from numpy import exp
from scipy.signal import freqz

# wave_samp_per is the total decimation factor
wave_samp_per = 5
cic_period = 23
R = cic_period * wave_samp_per
M = 1
N = 2
fs = 115e6  # Hz


def main():
    fig, axs = plt.subplots()
    b = [1, -2 * exp(R), exp(R)]
    a = [1, -2, 1]
    (w, h) = freqz(b=b, a=a)
    f = w * fs / (2 * np.pi)
    h_db = 20 * np.log10(np.abs(h))
    h_phase = np.angle(h) * 180 / np.pi
    print(h_phase)
    axs.set_title('Frequency Response')
    axs.semilogx(f, h_db)
    plt.show()


if __name__ == "__main__":
    main()
