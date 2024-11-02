class RetailItem:
  def __init__(self, item_description, units_in_inventory, price, cost):
   
    self.__item_description = item_description
    self.__units_in_inventory = units_in_inventory
    self.__price = price
    self.__cost = cost
   
  def set_item_description(self,item_description):
    self.__item_description = item_description
  def set_units_in_inventory(self,units_in_inventory):
    self.__units_in_inventory = units_in_inventory
  def set_price(self, price):
    self.__price = price
  def set_cost(self,cost):
    self.__cost = cost

 
  def get_item_description(self):
    return self.__item_description
  def get_units_in_inventory(self):
    return self.__units_in_inventory
  def get_price(self):
    return self.__price
  def get_cost(self):
    return self.__cost
   
  def down(self,item):
    item -= 1
  def up(self, item):
    item += 1
   
  def __str__(self):
    return (f"The item is {self.__item_description}. You have {self.__units_in_inventory} units in inventory. It costs {self.__cost}")
   
  def buy(self, current, tax, item):
    current += tax * item.__price
   
  def __del__(self):
    print("The part has been removed.")
    
