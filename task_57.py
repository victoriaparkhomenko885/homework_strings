import random

line = ""


def gen_numbers(txt, counter=0, number=0):
    number = random.randint(0, 9)
    return line


def gen_letters(line, counter=0):
    line += chr(random.randint(97, 121))
    return line


def gen_words(line):
    arr = ["word", "letter", "sentens", "world", "my", "rgb", "loL"]
    line += arr[random.randint(0, 6)]
    return line


def gen_underscore(line):
    line += "_"
    return line


def gen_letters_title(line, counter=0):
    line += chr(random.randint(65, 90))
    return line


def determinant(line):
    line += "_!_"
    return line


def gen_password():
    line = ""
    counter_lenght = random.randint(5, 25)
    counter_cycle = 0
    while counter_cycle < counter_lenght:
        counter = random.randint(1, 5)
        if counter == 1:
            line = gen_numbers(line)
        if counter == 2:
            line = gen_letters(line)
        if counter == 3:
            line = gen_words(line)
        if counter == 4:
            line = gen_underscore(line)
        if counter == 5:
            line = gen_letters_title(line)
        counter_cycle += 1
    line = determinant(line)
    return line


def determinant_algotitm(line):
    if line[len(line)-1] == "_" and line[len(line)-3] == "_" and line[len(line)-2] == "!":
        print("Yes")
    else:
        print("No")


x = 0
while x < 20:
    line1 = gen_password()
    print(line1)
    determinant_algotitm(line1)
    x += 1   