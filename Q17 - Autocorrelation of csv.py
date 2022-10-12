import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import xlabel, ylabel, grid, title

excel_6 = pd.read_csv(r"C:\Users\qndlq\Downloads\scope_10.csv")
excel_7 = pd.read_csv(r"C:\Users\qndlq\Downloads\scope_11.csv")
excel_8 = pd.read_csv(r"C:\Users\qndlq\Downloads\scope_12.csv")

excel_6.dropna(subset = ['1'], inplace=True)
excel_7.dropna(subset = ['1'], inplace=True)
excel_8.dropna(subset = ['1'], inplace=True)

excel_6.dropna(subset = ['x-axis'], inplace=True)
excel_7.dropna(subset = ['x-axis'], inplace=True)
excel_8.dropna(subset = ['x-axis'], inplace=True)

excel_6 = excel_6.iloc[1: , :]
excel_7 = excel_7.iloc[1: , :]
excel_8 = excel_8.iloc[1: , :]

x6 = pd.to_numeric(excel_6['1'], downcast="float")
x7 = pd.to_numeric(excel_7['1'], downcast="float")
x8 = pd.to_numeric(excel_8['1'], downcast="float")

t6 = excel_6[['x-axis']]
t7 = excel_7[['x-axis']]
t8 = excel_8[['x-axis']]

tau6 = float(t6.iat[2, 0]) - float(t6.iat[1, 0])
tau7 = float(t7.iat[2, 0]) - float(t7.iat[1, 0])
tau8 = float(t8.iat[2, 0]) - float(t8.iat[1, 0])

record6 = len(t6)
record7 = len(t7)
record8 = len(t8)

fig, ax6 = plt.subplots(sharex=True)

ax6 = matplotlib.pyplot.acorr(x6, maxlags=100)
ax6 = grid(True)
ax6 = title('the tau is = '+ str(float(tau6)) + ' , there are '+ str(record6) + 'records')
ax6 = xlabel("Lag")
ax6 = ylabel("RX")

fig, ax7 = plt.subplots(sharex=True)
ax7 = matplotlib.pyplot.acorr(x7, maxlags=400)
ax7 = grid(True)
ax7 = title('the tau is = '+ str(tau7) + ' , there are '+ str(record7) + 'records')
ax7 = xlabel("Lag")
ax7 = ylabel("RX")

fig, ax8 = plt.subplots(sharex=True)

ax8 = matplotlib.pyplot.acorr(x8, maxlags=400)
ax8 = grid(True)
ax8 = title('the tau is = '+ str(tau8) + ' , there are '+ str(record8) + 'records')
ax8 = xlabel("Lag")
ax8 = ylabel("RX")

plt.show()

