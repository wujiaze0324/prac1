total = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number")
    number = int(input("Number of items: "))
for i in range(number):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9  # apply 10% discount of total
print("Total price for ", number, " items is $", total)