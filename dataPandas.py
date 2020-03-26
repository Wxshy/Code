import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/samue/Documents/datasets/brazil_covid19.csv')

stateDataFrame = df[df['state'] == 'Rio de Janeiro']

rioCases = stateDataFrame['cases']

rioDates = stateDataFrame['date'] + ' ' + stateDataFrame['hour']

x = rioDates.to_numpy()
y = rioCases.to_numpy()



plt.plot(x, y)
plt.show()
