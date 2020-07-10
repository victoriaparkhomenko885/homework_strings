counter = 1 

text_input = input("Input your string:  ")
text_output = ""

for even in text_input :
    if counter % 2 == 0:
        if even == 'a' or even == 'b':
            text_output += 'c'
        else:
            text_output += 'a'
    else:
        text_output += even
    counter += 1


print(text_output)