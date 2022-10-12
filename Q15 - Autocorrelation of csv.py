import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import xlabel, ylabel, grid, title

excel_1 = pd.read_csv(r'C:\Users\qndlq\Downloads\scope_5.csv')
excel_2 = pd.read_csv(r'C:\Users\qndlq\Downloads\scope_6.csv')

excel_1.dropna(subset=['1'], inplace=True)
excel_2.dropna(subset=['1'], inplace=True)
excel_1.dropna(subset=['x-axis'], inplace=True)
excel_2.dropna(subset=['x-axis'], inplace=True)
excel_1 = excel_1.iloc[1:, :]
excel_2 = excel_2.iloc[1:, :]

# x1 = excel_1[['1']]
# x2 = excel_2[['1']]

x1 = pd.to_numeric(excel_1['1'], downcast="float")
x2 = pd.to_numeric(excel_2['1'], downcast="float")

t1 = excel_1[['x-axis']]
t2 = excel_2[['x-axis']]

tau1 = float(t1.iat[2, 0]) - float(t1.iat[1, 0])
tau2 = float(t2.iat[2, 0]) - float(t2.iat[1, 0])

record1 = len(t1)
record2 = len(t2)

fig, ax1 = plt.subplots(sharex=True)

ax1 = matplotlib.pyplot.acorr(x1, maxlags=60)
ax1 = grid(True)
ax1 = title('the tau is = '+ str(tau1) + ' , there are '+ str(record1) + 'records')
ax1 = xlabel("Lag")
ax1 = ylabel("RX")

fig, ax2 = plt.subplots(sharex=True)
ax2 = matplotlib.pyplot.acorr(x2, maxlags=100)
ax2 = grid(True)
ax2 = title('the tau is = '+ str(tau2) + ' , there are '+ str(record2) + 'records')
ax2 = xlabel("Lag")
ax2 = ylabel("RX")

fig, ax3 = plt.subplots(sharex=True)
ax3 = plt.hist(x2, bins = 30)

plt.show()

