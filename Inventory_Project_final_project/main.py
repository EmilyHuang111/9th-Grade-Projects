from RetailItem import *
from CashRegister import *
from random import randint
import pickle
import os
import copy

# Create a dictionary or load an existing dictionary file
inventory = {}
if os.path.exists("inventory.pickle"):
  inventory = pickle.load(open("inventory.pickle", "rb"))
  
soldItems = {}
if os.path.exists("soldItems.pickle"):
  soldItems = pickle.load(open("soldItems.pickle", "rb"))

# Create a menu for login
def login_menu():
  while (True):
    print()
    print("Are you the customer or the owner?")
    print("1: Owner.\n")
    print("2: Customer.\n")
    print("3: Exit.\n")
    userChoice = input("Please enter your selection (1,2,3):")

    if userChoice == "1":
      owner_menu()
      print("Your file has been successfully saved.")
    if userChoice == "2":
      print()
      print("Welcome to the store!")      
      customer_menu()
    if userChoice == "3":
      break
    if userChoice != "1" and userChoice != "2" and userChoice != "3":
      print(
        "Your choice does not exist. Please type in the correct choice. \n")


# Create a menu for owner
menu_option = ("1", "2", "3", "4", "5", "6", "7", "8")


def owner_menu():
  while (True):
    print()
    print("------------------ Menu ---------------- \n")
    print("1: Enter a part to your inventory.\n")
    print("2: Remove a part from your inventory.\n")
    print("3: Add or reduce part quantity.\n")
    print("4: Get selling price for a part.\n")
    print("5: Get purchase cost for a part.\n")
    print("6: Show current inventory.\n")
    print("7: Show revenue & profit report.\n")
    print("8: Save and Exit.\n")
    print()
    ownerChoice = input(
      "Please type 1, 2, 3, 4, 5, 6, 7, and 8 to select one of the above options. "
    )

    if ownerChoice == "1":
      item = input("What is the part you want to add to the inventory? ")
      count = input("How many " + item +
                    "'s would you like to add to the inventory? ")
      price = input("How much is the selling price for the part? $")
      cost = input("How much is the purchase price for the part? $")
      part = RetailItem(item, count, price, cost)
      inventory[item] = part

    if ownerChoice == "2":
      if inventory == {}:
        print("There are no parts to remove from the inventory.")
      else:
        item = input(
          "Please enter the exact name of the part you want to remove. ")
      if item in inventory:
        del inventory[item]
      else:
        print("That part is not in the inventory.")

    if ownerChoice == "3":
      print("Let's change the quantity of a part.\n")
      item = input("What is the part you want to change its quantity? ")
      part = inventory[item]
      quantity = part.get_units_in_inventory()
      print("Current quantity of the part is " + quantity)
      new_quantity = input("Enter the new quantity for the part: ")
      part.set_units_in_inventory(new_quantity)

    if ownerChoice == "4":
      item = input("What item would you like to check the selling price? ")
      if item in inventory:
        price = inventory[item].get_price()
        price = float(price)
      print("The selling price of the part is " + "$" + "{:.2f}".format(price))

    if ownerChoice == "5":
      item = input("What item would you like to check the purchase cost? ")
      if item in inventory:
        cost = inventory[item].get_cost()
        cost = float(cost)
      print("The purchase cost of the part is " + "$" + "{:.2f}".format(cost))

    if ownerChoice == "6":
      print("See below for current inventory.\n")
      show_inventory()
      print()
    if ownerChoice == "7":
      print("See below for revenue & profit report.\n")
      show_revenue()
      print()

    if ownerChoice == "8":
      # Save dictionary to a pickle file
      with open("inventory.pickle", "wb") as file:
        pickle.dump(inventory, file, pickle.HIGHEST_PROTOCOL)  
      print("The file has been successfully saved.\n")  
      break

    if ownerChoice !="1" and ownerChoice !="2" and ownerChoice !="3" and ownerChoice !="4" \
       and ownerChoice !="5" and ownerChoice !="6" and ownerChoice !="7" and ownerChoice !="8":
      print(
        "Your choice does not exist. Please type in the correct choice. \n")


def show_inventory():
  if inventory == {}:
    print("There is no part in the inventory.")
  else:
    print("Name\t\t\t quantity\t purchase cost\t selling price")
    for item in inventory:
      description = inventory[item].get_item_description()
      description = description.ljust(5)
      quantity = inventory[item].get_units_in_inventory()
      price = inventory[item].get_price()
      price = float(price)
      cost = inventory[item].get_cost()
      cost = float(cost)
      print(description + "\t\t\t\t" + str(quantity) + "\t\t\t" + "$" +
            "{:.2f}".format(cost) + "\t\t\t" + "$" + "{:.2f}".format(price))


def show_revenue():
  if soldItems == {}:
    print("There is nothing sold at this time.")
  else:
    items_sold = {}
    print("Transactions: ")
    print("Transaction ID\t\t    Sale \t             Profit")
    for transacID in soldItems:
      transaction = soldItems[transacID]
      transaction_revenue = 0
      transaction_profit = 0      
      for (item, quantity, price, cost) in transaction.get_data():
        if (item, price, cost) not in items_sold:
          items_sold[(item, price, cost)] = int(quantity)
        else:
          items_sold[(item, price, cost)] += int(quantity)
        transaction_revenue += (float(quantity)) * (float(price))
        transaction_profit += (float(quantity)) * (float(price) - float(cost))        
        print(str(transacID) + "\t\t\t\t" + "$" + "{:.2f}".format(transaction_revenue) + "\t\t\t\t" + "$" + "{:.2f}".format(transaction_profit))

    print()
    total_sum = 0
    total_sum1 = 0    
    print("Items Sold: ")
    print("Name\t\t\t quantity\t selling price \t     cost")
    for (item, price, cost), quantity in items_sold.items():
      print(item + "\t\t\t\t" + str(quantity) + "\t\t\t" + "$" +
            "{:.2f}".format(float(price)) + "\t\t\t" + "$" +"{:.2f}".format(float(cost)))
      total_sum += float(price) * float(quantity)
      total_sum1 += (float(price) - float(cost)) * float(quantity)      

    print(f"Total Store Revenue: ${total_sum:.2f}" )
    print(f"Total Store Profit: ${total_sum1:.2f}" )

# Create a menu for customer
def customer_menu():
  checkout = CashRegister()
  while (True):
    print()
    print("------------------ Menu ---------------- \n")
    print("1: Choose an item and add it to cart.\n")
    print("2: Remove an item from cart.\n")
    print("3: View Cart.\n")
    print("4: Clear Cart.\n")
    print("5: Check out and print receipt.\n")
    print("6: Save and Exit.\n")
    print()
    customerChoice = input(
      "Please type 1, 2, 3, 4, 5 and 6 to select one of the above options. ")

    if customerChoice == "1":
      if inventory == {}:
        print("Unfortunately there is no item available in the store. Please come back again.")
      else:
        show_items()
        item = input("What is the item you want to add to your cart? ")
        if item in inventory:
          count = input("How many " + item +
                      "'s would you like to add to the cart? ")
          price = inventory[item].get_price()
          cost = inventory[item].get_cost()          
          checkout.purchase_item_quantity(item,count,price,cost)
        else:
          print("Unfortunately, that item is not in the inventory.")
      
    if customerChoice == "2":
      if len(checkout.get_items()) != 0:
        checkout.show_items()
        item = input("What is the item you want to remove from your cart? ")
        if item in checkout.get_items():
          checkout.remove_items(item)  
        else:
          print("That item is not in the cart. ")
      else:
        print("There is nothing in the cart to remove.")

    if customerChoice == "3":
      print("Let's view the cart.\n")
      if len(checkout.get_items()) != 0:
        checkout.show_items()
      else:
        print("There is nothing in the cart to show.")
    if customerChoice == "4":
      print("Let's clear the cart.\n")
      if len(checkout.get_items()) != 0:
        checkout.clear()
      else:
        print("There is nothing in the cart to clear.")
    if customerChoice == "5":
      print("Let's check out and print receipt.\n")
      if len(checkout.get_items()) != 0:
        show_receipt(checkout)
      else:
        print("There is nothing in the cart to checkout.")

    if customerChoice == "6":
      # Save dictionary to a pickle file
      with open("soldItems.pickle", "wb") as file:
         pickle.dump(soldItems, file, pickle.HIGHEST_PROTOCOL)
      print("The file has been successfully saved.\n")  
      break

    if customerChoice !="1" and customerChoice !="2" and customerChoice !="3" and customerChoice !="4" \
       and customerChoice !="5":
      print(
        "Your choice does not exist. Please type in the correct choice. \n")


def show_items():
    print("Name\t\t\t quantity\t selling price")
    for item in inventory:
      description = inventory[item].get_item_description()
      description = description.ljust(5)
      quantity = inventory[item].get_units_in_inventory()
      price = inventory[item].get_price()
      price = float(price)
      print(description + "\t\t\t\t" + quantity + "\t\t\t" + "$" +
            "{:.2f}".format(price))

def random_with_N_digits(n):
  range_start = 10**(n - 1)
  range_end = (10**n) - 1
  return randint(range_start, range_end)


def show_receipt(checkout):
    print("Name\t\t\t quantity\t selling price")
    i = 0
    sum = 0
    transactionID = random_with_N_digits(10)
    for item in checkout.get_items():
      quantity = checkout.get_quantity()[i]
      quantity = int(quantity)
      price = checkout.get_price()[i]
      price = float(price)
      sum = sum + quantity * price
      part = inventory[item]
      old_quantity = part.get_units_in_inventory() 
      old_quantity = int(old_quantity)
      new_quantity = old_quantity - quantity
      if new_quantity == 0:
        del inventory[item]
      else:
        part.set_units_in_inventory(str(new_quantity))
      print(item + "\t\t\t\t" + str(quantity) + "\t\t\t" + "$" +
            "{:.2f}".format(price))
      i = i + 1
      
    print("Subtotal: " + "$" + "{:.2f}".format(sum))
    print("Total w/ 7% Sales Tax:  " + "$" + "{:.2f}".format(sum * 1.07) + "\n")
    print("Thank you for shopping with us.")
    soldItems[transactionID] = copy.deepcopy(checkout)

login_menu()
