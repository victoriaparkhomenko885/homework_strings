counter = 1 

Str_input = input("Input your string  ")
Str_output=""

for ch in Str_input :

    if(counter % 2 == 0):
        if( ch == 'a' or ch == 'b'):
            Str_output+='c'
        else:
            Str_output+='a'
    else:
        Str_output+=ch
    counter+=1

print(Str_output)