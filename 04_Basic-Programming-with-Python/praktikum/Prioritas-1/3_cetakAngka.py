for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print(i ** 2)
    elif i % 5 == 0:
        print(i ** 3)
    else:
        print(i)
