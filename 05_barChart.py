import matplotlib.pyplot as plt

name = ["Tejas", "Dipti", "vaish", "Khushi"]
age = [23, 21, 22, 19]

plt.bar(name, age, color='lightgreen', edgecolor="black")

plt.title("Family")
plt.xlabel("Name")
plt.ylabel("Age")

plt.show()