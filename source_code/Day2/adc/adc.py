import matplotlib.pyplot as plt
import numpy as np
import scipy.signal

FS = 115e6


def main():
    data = {}
    for key in [f"adc{i}" for i in range(1, 9)]:
        data[key] = np.loadtxt(f"{key}_dat.txt")
    
    (f, S) = scipy.signal.periodogram(data["adc8"], FS, scaling='density')
    plt.semilogy(f, S)
    plt.xlabel('frequency [Hz]')
    plt.ylabel('PSD [V**2/Hz]')
    plt.show()


if __name__ == "__main__":
    main()
