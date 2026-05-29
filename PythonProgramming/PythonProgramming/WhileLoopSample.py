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


# decremental_while_loop()
# incremental_while_loop()
nested_while_loop()
