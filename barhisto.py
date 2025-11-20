import matplotlib.pyplot as plt

# Sample data (replace with your own)
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 24, 36, 18, 12]

plt.bar(categories, values, color='pink', edgecolor='black')
plt.title("Bar Graph")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()


import numpy as np

# Sample data (replace with your own)
data = np.random.randn(1000)  # 1000 random values (normal distribution)

plt.hist(data, bins=20, color='pink', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value Ranges")
plt.ylabel("Frequency")
plt.show()
 