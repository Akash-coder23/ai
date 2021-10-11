import pandas as pd
import os

fn= os.getcwd();

fm=fn+"//data.csv"

data=pd.read_csv(fm)

print(data)
