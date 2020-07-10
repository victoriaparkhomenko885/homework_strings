def palindrome(number):
    a = number[::-1]
    if number == a:
        print(number, "is palindrome")
    else:
        print(number, "is not palindrome")


x = input("Enter to check palindrome: ")
palindrome(x)
