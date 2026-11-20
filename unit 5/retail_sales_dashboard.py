import csv
import os
import numpy as np
import matplotlib.pyplot as plt

filename = "retail_sales.csv"

# Create CSV file
if not os.path.exists(filename):
    data = [
        ["Jan", "Laptop", 5, 45000],
        ["Jan", "Mobile", 10, 15000],
        ["Feb", "Laptop", 3, 45000],
        ["Feb", "Mobile", 15, 15000],
        ["Mar", "Tablet", 8, 20000],
        ["Mar", "Laptop", 4, 45000],
        ["Apr", "Mobile", 12, 15000],
        ["Apr", "Tablet", 6, 20000],
        ["May", "Laptop", 7, 45000],
        ["May", "Mobile", 9, 15000],
        ["Jun", "Tablet", 10, 20000],
        ["Jun", "Laptop", 2, 45000]
    ]

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Month", "Product", "Quantity", "Price"])
        writer.writerows(data)

# Read CSV file
monthly_sales = {}
product_sales = {}
quantities = []
revenues = []

with open(filename, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        month = row["Month"]
        product = row["Product"]
        quantity = int(row["Quantity"])
        price = float(row["Price"])

        revenue = quantity * price

        monthly_sales[month] = monthly_sales.get(month, 0) + revenue
        product_sales[product] = product_sales.get(product, 0) + revenue

        quantities.append(quantity)
        revenues.append(revenue)

# Calculate statistics
if len(revenues) == 0:
    print("No sales data available.")
    raise SystemExit

sales = np.array(revenues)

print("\nRETAIL SALES REPORT")
print("-------------------")
print("Total Revenue:", sales.sum())
print("Average Revenue:", round(sales.mean(), 2))
print("Maximum Revenue:", sales.max())
print("Minimum Revenue:", sales.min())

print("\nProduct-wise Revenue:")
for product, amount in product_sales.items():
    print(product, ":", amount)

# Prepare graph data
months_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
months = [m for m in months_order if m in monthly_sales]

# Create dashboard
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(months, [monthly_sales[m] for m in months], marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.subplot(1, 3, 2)
plt.bar(product_sales.keys(), product_sales.values())
plt.title("Product-wise Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.subplot(1, 3, 3)
plt.scatter(quantities, revenues)
plt.title("Quantity vs Revenue")
plt.xlabel("Quantity")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()
