def incremental_while_loop():
    i = 0
    while i < 5:
        print("Data Science -> ", i)
        i = i + 1  # incremental while loop


def decremental_while_loop():
    i = 5
    while i >= 1:
        print("Data Science -> ", i)
        i = i - 1


def nested_while_loop():
    i = 1
    while i <= 5:
        print("Data Science -> ", i)
        j = 1
        while j <= 4:
            print("Technology -> ", j)
            j = j + 1
        i = i + 1
        print()


def nested_while_loop_2():
    # lets use while loop using some numbers
    i = 1
    while i <= 2:
        j = 0
        while j <= 2:
            print(i * j, end=" ")
            j += 1
        print()
        i += 1

def nested_while_loop_3():
    # lets use while loop using some numbers
    i = 1
    while i <= 4:
        j = 0
        while j <= 3:
            print(i * j, end=" ")
            j += 1
        print()
        i += 1


# decremental_while_loop()
# incremental_while_loop()
# nested_while_loop()
# nested_while_loop_2()
nested_while_loop_3()
