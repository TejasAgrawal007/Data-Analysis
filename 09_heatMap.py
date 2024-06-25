import matplotlib.pyplot as plt
import seaborn as sea


data = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

sea.heatmap(data, annot=True)

plt.title("Data")

plt.show()