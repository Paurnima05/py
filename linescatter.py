
import matplotlib.pyplot as plt
# Sample data
x_values = [1, 2, 3, 4, 5, 6]
y_values = [2, 4, 5, 4, 6, 7]

plt.figure(figsize=(6,4))
plt.scatter(x_values, y_values)
plt.title("Scatter Plot Example")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()


# Sample data
x_line = [1, 2, 3, 4, 5, 6]
y_line = [3, 5, 7, 6, 8, 10]

plt.figure(figsize=(6,4))
plt.plot(x_line, y_line, marker='s')
plt.title("Line Graph Example")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.show()