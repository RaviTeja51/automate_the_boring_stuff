def displayInventory(invent):
   print("Inventory:")
   for key,value in invent.items():
     
       print(f"{value} {key}")
if __name__ == "__main__":
   stuff = {'rope' : 12,'coins' : 500,'medicine' : 45,'weapon kit' : 34}
   displayInventory(stuff)


