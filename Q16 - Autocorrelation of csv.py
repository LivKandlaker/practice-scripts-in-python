import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import xlabel, ylabel, grid, title

excel_3 = pd.read_csv(r"C:\Users\qndlq\Downloads\scope_7.csv")
excel_4 = pd.read_csv(r"C:\Users\qndlq\Downloads\scope_8.csv")
excel_5 = pd.read_csv(r"C:\Users\qndlq\Downloads\scope_9.csv")

excel_3.dropna(subset = ['1'], inplace=True)
excel_4.dropna(subset = ['1'], inplace=True)
excel_5.dropna(subset = ['1'], inplace=True)

excel_3.dropna(subset = ['x-axis'], inplace=True)
excel_4.dropna(subset = ['x-axis'], inplace=True)
excel_5.dropna(subset = ['x-axis'], inplace=True)

excel_3 = excel_3.iloc[1: , :]
excel_4 = excel_4.iloc[1: , :]
excel_5 = excel_5.iloc[1: , :]

x3 = pd.to_numeric(excel_3['1'], downcast="float")
x4 = pd.to_numeric(excel_4['1'], downcast="float")
x5 = pd.to_numeric(excel_5['1'], downcast="float")

t3 = excel_3[['x-axis']]
t4 = excel_4[['x-axis']]
t5 = excel_5[['x-axis']]

tau3 = float(t3.iat[2, 0]) - float(t3.iat[1, 0])
tau4 = float(t4.iat[2, 0]) - float(t4.iat[1, 0])
tau5 = float(t5.iat[2, 0]) - float(t5.iat[1, 0])

record3 = len(t3)
record4 = len(t4)
record5 = len(t5)

fig, ax3 = plt.subplots(sharex=True)

ax3 = matplotlib.pyplot.acorr(x3, maxlags=100)
ax3 = grid(True)
ax3 = title('the tau is = '+ str(float(tau3)) + ' , there are '+ str(record3) + 'records')
ax3 = xlabel("Lag")
ax3 = ylabel("RX")

fig, ax4 = plt.subplots(sharex=True)
ax4 = matplotlib.pyplot.acorr(x4, maxlags=400)
ax4 = grid(True)
ax4 = title('the tau is = '+ str(tau4) + ' , there are '+ str(record4) + 'records')
ax4 = xlabel("Lag")
ax4 = ylabel("RX")

fig, ax5 = plt.subplots(sharex=True)

ax5 = matplotlib.pyplot.acorr(x5, maxlags=400)
ax5 = grid(True)
ax5 = title('the tau is = '+ str(tau5) + ' , there are '+ str(record5) + 'records')
ax5 = xlabel("Lag")
ax5 = ylabel("RX")

plt.show()

