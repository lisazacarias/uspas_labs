from csv import DictReader
from math import sin

import matplotlib.pyplot as plt
import scipy.signal


def main():
    with open('ph_acc.csv') as csvfile:
        reader = DictReader(csvfile)
        times = []
        phases = []
        sines = []
        for row in reader:
            time_str = row["Time [ns]"]
            time = float(time_str) * 1e-9
            times.append(time)
            phase = float(row["phase_acc"])
            phases.append(phase)
            sines.append(sin(phase))
        
        # plt.plot(times, sines)
        (f, S) = scipy.signal.periodogram(sines, 1 / (times[1] - times[0]), scaling='density')
        plt.semilogy(f, S)
        plt.xlabel('frequency [Hz]')
        plt.ylabel('PSD [V**2/Hz]')
        plt.show()


if __name__ == "__main__":
    main()
