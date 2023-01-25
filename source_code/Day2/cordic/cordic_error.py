from csv import DictReader
from math import sqrt

import numpy as np
from skimage.metrics import mean_squared_error

EXPECTED_GAIN = 1.64676


def get_rms(csvfile) -> float:
    reader = DictReader(csvfile)
    gains = []
    for row in reader:
        xin = float(row["      xin"])
        xout = float(row["     xout"])
        
        yin = float(row["      yin"])
        yout = float(row["     yout"])
        
        mag_in = sqrt(xin ** 2 + yin ** 2)
        mag_out = sqrt(xout ** 2 + yout ** 2)
        
        gains.append(mag_out / mag_in if mag_in else 0)
    rms = mean_squared_error(np.array(gains),
                             np.array([EXPECTED_GAIN
                                       for _ in range(len(gains))]))
    return rms


def main():
    print("RTOP RMS:", get_rms(open("cordic_rtop.csv")))
    print("PTOR RMS:", get_rms(open("cordic_ptor.csv")))
    
    print("RTOP DW16 RMS:", get_rms(open("rtop_dw16.csv")))
    print("PTOR DW16 RMS:", get_rms(open("ptor_dw16.csv")))
    
    print("RTOP DW21 RMS:", get_rms(open("rtop_dw21.csv")))
    print("PTOR DW21 RMS:", get_rms(open("ptor_dw21.csv")))
    
    print("RTOP NSTG10 RMS:", get_rms(open("rtop_nstg10.csv")))
    print("PTOR NSTG10 RMS:", get_rms(open("ptor_nstg10.csv")))


if __name__ == "__main__":
    main()
