import random

Str=""

def gen_numbers(Str,counter = 0,number = 0): 
    
        number = random.randint(0,9)        
        return Str

def gen_letters(Str,counter = 0):      
        Str += chr(random.randint(97,121))        
        return Str

def gen_words(Str):
     arr = ["word","letter","sentens","world","my","rgb","loL"]
     Str +=arr[random.randint(0,6)]
     return Str

def gen_underscore(Str):
    Str+="_"
    return Str

def gen_letters_title(Str,counter = 0):      
        Str += chr(random.randint(65,90))        
        return Str

def determinant(Str):
    
    Str+="_!_"
    return Str

def gen_password():
    Str=""
    counter_lenght = random.randint(5,25)
    counter_cycle=0
    while(counter_cycle < counter_lenght):
        counter = random.randint(1,5)
        if(counter==1):
            Str = gen_numbers(Str)
        if(counter==2):
            Str = gen_letters(Str)
        if(counter==3):
            Str = gen_words(Str)
        if(counter==4):
            Str = gen_underscore(Str)
        if(counter==5):
            Str = gen_letters_title(Str)
        counter_cycle += 1
    Str = determinant(Str)
    return Str


def determinant_algotitm(Str):
    if( Str[len(Str)-1] == "_" and Str[len(Str)-3] == "_" and Str[len(Str)-2] == "!" ):
        print("Yes")
    else:
        print("No")


i=0
while(i < 20):
    str1 = gen_password()
    print(str1)
    determinant_algotitm(str1)
    i += 1