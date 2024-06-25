import matplotlib.pyplot as plt

data = [1,4,7,8,52,1,4,78,5,23,6,9,8,7,41,1]


# Bins -> Its a Group of Data of a given number's

plt.hist(data, bins=5, color='lightblue', edgecolor='green')


plt.title("Data")
plt.xlabel('X-label')
plt.ylabel('Y-label')

plt.show()