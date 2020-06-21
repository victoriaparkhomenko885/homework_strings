import random

counter = 0
number = 0
check = False
Str=""

while(counter<5):
    number = random.randint(-8,8)
    if(number % 2 == 0):
       Str += str(number)
    else:
       Str += str(number+1)        
    if(number == 8 or number == 7):
      check = True
    counter+=1

while(counter<10):  
    Str += chr(random.randint(97,121))
    counter+=1

if(check):
   Str += "AB" 
else:
   Str += "XY"

print(Str)
