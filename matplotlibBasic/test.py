import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


path= os.getcwd() + "\\dataSheet.csv"
data= pd.read_csv(path)

plt.suptitle("Different Plots in PYTHON")



#Scatter Plot
plt.subplot(3,2,1)
plt.scatter(data['X'], data['Y'], c="green")
plt.title("Scatter Plot")


#Line Plot
plt.subplot(3,2,2)
plt.plot(data['X'], data['Y'], c="blue")
plt.title("Line Plot")


#Dot-Line Plot
plt.subplot(3,2,3)
plt.scatter(data['X'], data['Y'], c="red")
plt.plot(data['X'], data['Y'], c="blue")
plt.title("Dot-Line Plot")


#Bar Plot Vertical
plt.subplot(3,2,4)
plt.bar(data['X'], data['Y'], color="blue")
plt.title("Bar Plot Vertical")


#Bar Plot Horizontal
plt.subplot(3,2,5)
plt.barh(data['X'], data['Y'], color="orange")
plt.title("Bar Plot Vertical")


#Pie Plot
plt.subplot(3,2,6)
x= np.array([37,23,15,25])
myLables=["APPLE", "GRAPE", "KIWI", "BANANA"]

plt.pie(x, labels=myLables)
plt.title("Pie Plot")







plt.show()




