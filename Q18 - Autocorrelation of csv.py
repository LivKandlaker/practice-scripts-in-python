import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import xlabel, ylabel, grid, title

excel_9 = pd.read_csv(r'C:\Users\qndlq\Downloads\scope_14.csv')
print(type(excel_9))
excel_9.dropna(subset = ['1'], inplace=True)

excel_9.dropna(subset = ['x-axis'], inplace=True)

excel_9 = excel_9.iloc[1: , :]

x9 = pd.to_numeric(excel_9['1'], downcast="float")

t9 = excel_9[['x-axis']]

tau9 = float(t9.iat[2, 0]) - float(t9.iat[1, 0])

record9 = len(t9)

fig, ax9 = plt.subplots(sharex=True)

ax9 = matplotlib.pyplot.acorr(x9, maxlags=400)
ax9 = grid(True)
ax9 = title('the tau is = '+ str(tau9) + ' , there are '+ str(record9) + 'records')
ax9 = xlabel("Lag")
ax9 = ylabel("RX")

plt.show()

