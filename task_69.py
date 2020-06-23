def Max_local_(Str,Max_local=0,counter=0,Max_lenght_words_pos=0):
    for i in Str:
        if Max_local < len(i):
            Max_local = len(i)
            Max_lenght_words_pos=counter
        counter+=1
    return Max_lenght_words_pos


def Min_local_(Str,counter=0,Min_lenght_words_pos=0):
    Min_local=len(Str[0])
    for i in Str:
        if Min_local > len(i):
            Min_local = len(i)
            Min_lenght_words_pos=counter
        counter+=1
    return Min_lenght_words_pos


Str = input("Input str with words ")
Str = Str.split()

Max_lenght_words_pos=0
Min_lenght_words_pos=0

Max_lenght_words_pos = Max_local_(Str)
Min_lenght_words_pos = Min_local_(Str)

Str_t = Str[Max_lenght_words_pos]
Str[Max_lenght_words_pos] = Str[Min_lenght_words_pos]
Str[Min_lenght_words_pos] = Str_t
Str_output=""
for i in Str:
    Str_output += i 

print(Str_output)