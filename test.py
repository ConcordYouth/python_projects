import matplotlib.pyplot as plt

d = [167.234, 123.234, 632.342, 342.521]

plt.hist(d, bins=4, color="c", edgecolor="k")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("First Histogram")
plt.show()
