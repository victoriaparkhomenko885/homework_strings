Str_input = input("Input your str ")
Str_output=""

for i in Str_input :
    if (i == 'a'):
        Str_output+='A'
    if (i == 'b'):
        Str_output+='B'
    if(i!='a' and i!='b'):
          Str_output+=i

print(Str_output)