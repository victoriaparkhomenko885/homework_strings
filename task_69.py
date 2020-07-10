def max_local(text, max_loc=0, counter=0, max_lenght_words_pos=0):
    for x in text:
        if max_loc < len(x):
            max_loc = len(x)
            max_lenght_words_pos = counter
        counter += 1
    return max_lenght_words_pos


def min_local(text, counter=0, min_lenght_words_pos=0):
    min_local = len(text[0])
    for x in text:
        if min_local > len(x):
            min_local = len(x)
            min_lenght_words_pos = counter
        counter += 1
    return min_lenght_words_pos


text = input("Input str with words: ")
text = text.split()


max_lenght_words_pos = 0
min_lenght_words_pos = 0


max_lenght_words_pos = max_local(text)
min_lenght_words_pos = min_local(text)


line_t = text[max_lenght_words_pos]
text[max_lenght_words_pos] = text[min_lenght_words_pos]
text[min_lenght_words_pos] = line_t
text_output = ""
for x in text:
    text_output += x 


print(text_output)