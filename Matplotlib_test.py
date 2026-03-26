# Matplotlib: Is use for data vizualization 
# 2: if you want to convert data in vizual 
# 3: its a graph 
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [10, 20, 30, 40]

# plt.plot(x, y)

# plt.title("Line Graph")
# plt.xlabel("X Values")
# plt.ylabel("Y Values")

# plt.show()

# /******************************************************

# import matplotlib.pyplot as plt

# products = ["Laptop", "Mobile", "Tablet", "Headphones"]
# sales = [50, 120, 30, 80]


# plt.bar(products, sales)

# plt.title("Product Sales Graph")
# plt.xlabel("Products")
# plt.ylabel("Units Sold")


# plt.show()

# /************************************************************/*

import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Tablet", "Headphones"]
sales_2000 = [50, 120, 30, 80]
sales_2026 = [57, 130, 50, 100]


plt.plot(products, sales_2000, marker='o')
plt.plot(products, sales_2026, marker='o')
plt.title("Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.grid()
plt.legend()

plt.show()                                      