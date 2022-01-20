x = 10
oddlist = []
evelist = []
print("Please type in ten numbers")


while(x != 0):
  inp = int(input("Enter a number: "))
  x = x - 1
  if (inp % 2 != 0)
    oddlist.append(inp)
  elif (inp % 2 == 0)
    evelist.append(inp)
    
    
if (len(oddlist) == 0):
  print("There were no odd numbers entered!")
  
else:
  oddlist.sort()
  
  print("The largest odd number from the input is: ", oddlist[-1])
