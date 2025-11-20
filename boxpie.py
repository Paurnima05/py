import matplotlib.pyplot as plt
# ---------- BOX PLOT EXAMPLE ----------
# Sample data
box_data = [22, 25, 27, 30, 32, 35, 40, 42, 45, 50, 55, 70]

plt.figure(figsize=(6,4))
plt.boxplot(box_data)
plt.title("Box Plot Example")
plt.xlabel("Data Set")
plt.ylabel("Values")
plt.show()

categories = ["Apples", "Bananas", "Cherries", "Dates"]
values = [30, 25, 20, 25]

plt.figure(figsize=(6,4))
plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.title("Fruit Distribution")
plt.show()