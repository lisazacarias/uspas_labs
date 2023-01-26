import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import linregress


def main():
    dac_data = np.loadtxt("dacwf.txt")
    amp_data = np.loadtxt("awf.txt")
    time_data = np.loadtxt("twf.txt")
    
    # Scaling from ms to s
    time_data = time_data * 1e-3
    
    phase_data = np.loadtxt("pwf.txt")
    
    fig, raw_ax = plt.subplots()
    raw_ax.plot(time_data, amp_data)
    raw_ax.plot(time_data, phase_data)
    
    ax2 = raw_ax.twinx()
    ax2.plot(time_data[1:], dac_data)
    
    for idx_0, dac_val in enumerate(dac_data):
        if dac_val <= 0:
            break
    
    amp_data = amp_data[idx_0:]
    time_data = time_data[idx_0:]
    phase_data = phase_data[idx_0:]
    
    end_decay = len(amp_data) - 1
    
    # Find where the amplitude decays to "zero"
    for end_decay, amp in enumerate(amp_data):
        if amp < 10:
            break
    
    amp_data = amp_data[:end_decay]
    time_data = time_data[:end_decay]
    phase_data = phase_data[:end_decay]
    
    fig, decay_ax = plt.subplots()
    decay_ax.plot(time_data, amp_data)
    decay_ax.plot(time_data, phase_data)
    
    max_phase = max(phase_data)
    min_phase = min(phase_data)
    
    for max_idx, phase in enumerate(phase_data):
        if phase == max_phase:
            break
    
    time_data = time_data[max_idx:]
    phase_data = phase_data[max_idx:]
    
    for min_idx, phase in enumerate(phase_data):
        if phase == min_phase:
            break
    
    time_data = time_data[:min_idx]
    print(time_data)
    phase_data = phase_data[:min_idx]
    print(phase_data)
    
    m = linregress(time_data, phase_data).slope
    print(m)
    print((phase_data[-1] - phase_data[0]) / (time_data[-1] - time_data[0]))
    
    fig, slope_ax = plt.subplots()
    slope_ax.plot(time_data, phase_data)
    
    plt.show()


if __name__ == "__main__":
    main()
