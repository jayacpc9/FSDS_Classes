def odd_or_even():
    x = int(input("Enter a number: "))
    r = x % 2
    if r == 0:
        print("Even number")
    else:
        print("Odd Number")


def nested_if_condition():
    x = int(input("Enter a number: "))
    r = x % 2
    if r == 0:
        print("Even numbers")
        if (x > 5):
            print("number greater than 5")
        else:
            print("number less than 5")
    else:
        print("Odd number")


def multiple_if_elif_condition():
    x = int(input("Enter a number: "))
    if x == 1:
        print("number 1")
    elif x == 2:
        print("number 2")
    elif x == 3:
        print("number 3")
    elif x == 4:
        print("number 4")
    elif x == 5:
        print("number 5")

# odd_or_even()
# nested_if_condition()
# multiple_if_elif_condition()



