import matplotlib.pyplot as plt
import seaborn as sea

x = [11,21,3,45,5]
y = [61,7,81,19,10]


plt.plot(x, y, marker='o', linestyle='--', color='yellow')

plt.title("Academy")
plt.xlabel("Students")
plt.ylabel("Tuator")


plt.show()