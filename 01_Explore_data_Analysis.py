import numpy as np
import pandas as pd

excessData = pd.read_csv(r'./Datasets/ETH-USD.csv')

# print(excessData)


# print(excessData.head())
# print(excessData.tail())
# print(excessData.info())
# print(excessData.describe())
# print(excessData.shape)


# 1. To Delete Firt Column
# print(excessData.drop(["Date"], axis=1, inplace=True))
# print(excessData.head())

# 2. Unique
# print(excessData['Date'].unique())

