import math

import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.fftpack
from numpy import size

un_filter = pd.read_csv(r'C:\Users\qndlq\OneDrive\שולחן העבודה\unfilter.csv')
print(un_filter)

with_filter = pd.read_csv(r'C:\Users\qndlq\OneDrive\שולחן העבודה\withfilter.csv')
print(with_filter)

difference = pd.read_csv(r'C:\Users\qndlq\OneDrive\שולחן העבודה\different.csv')
print(difference)

print("Your cell is:" + un_filter.iat[3, 1])
print("Your cell is:" + with_filter.iat[3, 1])
print("Your cell is:" + difference.iat[3, 1])

a = float(un_filter.iat[3, 1])
b = float(un_filter.iat[4, 1])
print(a)
print(b)
print("---------------------------")

fs1 = 1 / (a - b)
print(fs1)

NS = 10000
Y1 = np.abs(scipy.fftpack.fft(size(un_filter)))
Y1 = Y1 * 2 / NS





