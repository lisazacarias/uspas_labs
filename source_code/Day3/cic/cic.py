import matplotlib.pyplot as plt
import numpy as np
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
    """
    B polynomial
    
    (1 - z^(-RM))^N
    (1 - z^(-R))^2
    (1 - z^(-R)) * (1 - z^(-R))
    1 - z^(-R) - z^(-R) + z^(-2R)
    1 - 2z^(-R) + z^(-2R)
    R = 115 -> 1 - 2z^(-115) + z^(-230)
    """
    b = [0 for _ in range(2 * R + 1)]
    b[0] = 1
    b[R] = -2
    b[2 * R] = 1
    print(b)
    
    """
    A polynomial

    (1 - z^(-1))^N
    (1 - z^(-1))^2
    (1 - z^(-1)) * (1 - z^(-1))
    1 - z^(-1) - z^(-1) + z^(-2)
    1 - 2z^(-1) + z^(-2)
    """
    a = [1, -2, 1]
    
    (w, h) = freqz(b=b, a=a, fs=fs)
    plt.plot(w, 20 * np.log10(abs(h)))
    plt.title(f"wave_samp_per = {wave_samp_per}")
    
    plt.show()


if __name__ == "__main__":
    main()
