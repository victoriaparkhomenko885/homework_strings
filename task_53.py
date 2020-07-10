text_input = input("Input your str: ")
text_output = ""

for s in text_input :
    if s == 'a':
        text_output += 'A'
    if s == 'b':
        text_output += 'B'
    if s!='a' and s!='b':
        text_output += s


print(text_output)