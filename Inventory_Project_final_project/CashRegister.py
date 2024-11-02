from RetailItem import *
class CashRegister:
  def __init__(self):
    self.__items=[]
    self.__quantity=[]
    self.__price=[]
    self.__cost=[]

  def purchase_item_quantity(self,retail_item,quantity,price,cost):
    self.__items.append(retail_item)    
    self.__quantity.append(quantity)
    self.__price.append(price)    
    self.__cost.append(cost)       
    print(quantity + " " + retail_item + " has been added.")

  def get_items(self):
    return self.__items

  def get_quantity(self):
    return self.__quantity

  def get_price(self):
    return self.__price

  def get_cost(self):
    return self.__cost
  
  def get_data(self):
    return zip(self.__items, self.__quantity, self.__price, self.__cost)
  
  def get_total(self):
    total = 0
    i = 0
    for item in self.__items:
      total = total + float(self.__quantity[i]) * float(self.__price[i])
      i = i + 1
    return total

  def remove_items(self,remove_item):
    i = 0
    for item in self.__items:
      if item == remove_item :
        self.get_items().remove(remove_item)
        del self.get_quantity()[i]
        del self.get_price()[i]   
        del self.get_cost()[i]          
        print("The item," + item + " has been removed from the cart.")  
      i = i + 1
   
  def clear(self):
    self.__items=[]
    print("The cart has been cleared.")     
    
  def show_items(self):
    print("\nDescription\t\t\tQuantity\t\t\t\tPrice\n")
    i = 0
    for item in self.__items:
      quantity = self.__quantity[i]
      price = self.__price[i]
      price = float(price)    
      print(item + "\t\t\t\t" + quantity + "\t\t\t\t\t\t" + "$" +
            "{:.2f}".format(price))
      i = i + 1

    
    




  




  
    
    




  
