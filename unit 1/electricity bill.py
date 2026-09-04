# Electricity Bill Generator

name = input("Enter customer name: ")
units = float(input("Enter electricity units consumed: "))

if units <= 100:
    amount = units * 2
elif units <= 200:
    amount = (100 * 2) + ((units - 100) * 3)
elif units <= 300:
    amount = (100 * 2) + (100 * 3) + ((units - 200) * 5)
else:
    amount = (100 * 2) + (100 * 3) + (100 * 5) + ((units - 300) * 7)

fixed_charge = 50
total = amount + fixed_charge

print("\n========== ELECTRICITY BILL ==========")
print("Customer Name :", name)
print("Units Consumed:", units)
print("Energy Charge :", amount)
print("Fixed Charge  :", fixed_charge)
print("Total Bill    :", total)
print("======================================")
