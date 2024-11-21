def add(Num_1,Num_2):
      sum = Num_1 + Num_2
      return sum

def sub(Num_1,Num_2):
      minus = Num_1 - Num_2
      return minus

def mult(Num_1,Num_2):
      multi = Num_1 * Num_2
      return multi

def div(Num_1,Num_2):
      div = Num_1/Num_2
      return div

def is_Operation(V):
     while True:
          Operation = input(V)
          if Operation.isdigit():                                                  
               return int(Operation)
          else:
               print("You fool choose a digit")

def is_num(text):
    while True:
      num = input(text)
      if num.replace(".","",1).isdigit():
        return int(num)
      else:
        print("no")

print("CASIO")
print("OPERATION")
print("1.Add \n2.Sub \n3.Mult \n4.Div \n0.Exit")
Operation = is_Operation("Choose an Operation ")
if(Operation == 0):
     print("CASIO")
else:
      Num_1 = is_num("Enter Num_1 ")
      Num_2 = is_num("Enter Num_2 ") 
      if(Operation == 1):
            print(Num_1, "+", Num_2, "=", add(Num_1,Num_2))
      elif(Operation == 2):
            print(Num_1, "-", Num_2, "=", sub(Num_1,Num_2))
      elif(Operation == 3):
            print(Num_1, "*", Num_2, "=", mult(Num_1,Num_2))
      elif(Operation == 4):
            if(Num_2 == 0):
                  print("Math Error")
            else:
                  print(Num_1, "/", Num_2, "=", div(Num_1,Num_2))
      else:
            print("Invalid operation")