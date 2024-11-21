#year = 2024
#print(year)
#print("We are in" ,year)
#month = "November"
#print("We are in" ,month)

#word = "My Name is Suzy"
#print(word)
#print("We are in" ,year)
#print("print(we are in +30)")

#Mango_P = 1000
#Banana_P = 1500
#N_Mango = 3
#N_Banana = 5
#Amt_Mango = Mango_P * N_Mango
#Amt_Banana = N_Banana * Banana_P
#print("Total Amount Spend =" ,Amt_Mango + Amt_Banana)

#Year = int(input("Enter a year"))
#if Year % 4 == 0:
 #if Year % 100 == 0:
  #if Year % 400 == 0:
    #print("A Leap year")
  #else :
   #print("Not a leap year")
 #else :
  #print("A Leap year")
#else :
 #print("Not a Leap year")

year = int(input("enter year"))
if(year%4==0 or year%100==0 and year%400==0):
 print("yes")
else :
 print("no")