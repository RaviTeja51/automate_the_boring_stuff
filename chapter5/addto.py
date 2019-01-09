def addtoinventory(invent,new):
    for i in new:
      if i in invent.keys():
          invent[i] += 1
      else:
          invent[i] = 1
    return invent


def display(invent):
   for key,values in invent.items():
      print(f"{values} {key}")


if __name__ == "__main__":
    stuff = {'gold coins' : 234,'daggers' : 23,'diamond' : 78,'rope' : 1}
    new = ['gun','ruby','ruby','daggers','rope']
    display(addtoinventory(stuff,new))
    
