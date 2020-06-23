str_one = input("Input your one str ")
str_two = input("Input your two str ")
str_output=""
counter=0
len_coincidences=0

for i in str_one:
    if(i == str_two[0]):
        while(str_one[counter+len_coincidences] == str_two[len_coincidences]):
            len_coincidences+=1        
        break
    str_output+=i
    counter+=1



counter = counter + len_coincidences
while(counter < len(str_one)):
    str_output+=str_one[counter]
    counter+=1

print(str_output)