import matplotlib.pyplot as plt

sno = [1,2,3,4,5]
labels = ["Tejas", "Dipti", "Vaish","Khushi", "Om"]
colors = ["royalblue", "lightgreen", "red", "yellow" , "green"]

plt.figure(figsize=(4,4))
plt.pie(sno, labels=labels, colors=colors, startangle=140, autopct="%1.1f%%")

plt.show()