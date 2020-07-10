line = input("Input your str: ")

counter = 0
counter_open_bracket = 0
counter_close_bracket = 0
max_counter = len(line)


while True:

    if max_counter == counter:
        if counter_open_bracket > counter_close_bracket:
            print("Open brackets ", counter_open_bracket, " more than Close brackets ", counter_close_bracket)
        if counter_open_bracket < counter_close_bracket:
            print("Close brackets ", counter_open_bracket, " more than Open brackets", counter_close_bracket)
        if counter_open_bracket == counter_close_bracket:
            print("Balance maintained : ", counter_open_bracket, " == ", counter_close_bracket)
        break
    if line[counter] == '(':
        counter_open_bracket = counter_open_bracket + 1
    if line[counter] == ')':
        counter_close_bracket = counter_close_bracket + 1
    counter = counter + 1
