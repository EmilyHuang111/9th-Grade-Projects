totalpurchase = float(input("Enter the amount of a purchase: "))
state_sales_tax: 0.04
county_sales_tax: 0.02

county_sales_tax = totalpurchase * 0.02
state_sales_tax = totalpurchase * 0.04
total_sales_tax = totalpurchase * 0.06
Total_Bill = totalpurchase + total_sales_tax

print("\n           RECEIPT\n")
print("---------------------------------------")
print("The amount of the purchase: $%5.2f" % (totalpurchase))
print("The state sales tax:        $%5.2f" % (state_sales_tax))
print("The county sales tax:       $%5.2f" % (county_sales_tax))
print("The total sales tax:        $%5.2f" % (total_sales_tax))
print("The total bill:             $%5.2f" % (Total_Bill))
print("---------------------------------------\n")

print("Thank you for shopping with us!")
