import random

counter = 0
number = 0
check = False
text = "44828adfrtHP"


while counter < 5:
    number = random.randint(-8, 8)
    if number % 2 == 0:
        text += str(number)
    else:
        text += str(number+1)
    if number == 8 or number == 7:
        check = True
    counter += 1


while counter < 10:
    text += chr(random.randint(97, 121))
    counter += 1

if check:
   text += "AB"
else:
   text += "XY"


print(text)
