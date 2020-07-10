text_one = input("Input your one str: ")
text_two = input("Input your two str: ")
text_output = ""
counter = 0
len_coincidences = 0

for x in text_one:
    if x == text_two[0]:
        while text_one[counter+len_coincidences] == text_two[len_coincidences]:
            len_coincidences += 1
        break
    text_output += x
    counter += 1


counter = counter + len_coincidences
while counter < len(text_one):
    text_output += text_one[counter]
    counter += 1


print(text_output)