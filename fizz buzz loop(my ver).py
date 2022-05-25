for num in range(41):
    if num % 35 == 0:
        print("fizz-buzz")
        continue

    elif num % 5 == 0:
        print("fizz")
        continue

    elif num % 7 == 0:
        print("buzz")
        continue

    print(num)