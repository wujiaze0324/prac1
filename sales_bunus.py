"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
while sales < 1000 and sales > 0:
    bunus = 1/10 * sales
    print("your bonus is", bunus)
if sales >= 1000:
    bunus = 3 / 20 * sales
    print("your bonus is", bunus)
else:
    sales = float(input("Enter sales: $"))
