import matplotlib.pyplot as plt

group1 = [20,10,40,30,50]
group2 = [70,60,90,80,100]
group3 = [120,110,140,130,150]

# Plotting box plot

plt.boxplot([group1, group2, group3], labels=["Team 1", "Team 2", "Team 3"])

plt.title("Team")

plt.show()