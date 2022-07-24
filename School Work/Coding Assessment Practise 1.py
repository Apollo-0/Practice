#Currency Converter
import time

print("WELCOME TO THE MONEY CONVERTER!!")
print()
time.sleep(1)
print("We convert: Dollars, Euros, and Pounds!")
time.sleep(0.5)
print("Give it a try!")
print()
time.sleep(2)


while True:
    print("""
    Select:
    '£' To convert to British Pounds
    'E' To convert to Europian Euros
    '$' To convert to American Dollars
    """)
    print()
    time.sleep(0.5)

    selection = input("You have selected: ")
    print()
    time.sleep(0.5)

    if selection == '£':
        print("You have selected to convert to 'Pounds'")
        time.sleep(0.5)
        print("Please input your starter currency from the following:")
        time.sleep(0.5)
        opt = input("'Euros' OR 'Dollars': ")
        print()
        time.sleep(1)

        if opt == 'Euros' or 'euros':
            print("You are currently converting from 'Euros' to 'Pounds'")
            print()
            time.sleep(1)
            amount = float(input("Enter your amount here: "))
            time.sleep(0.5)
            print("This is your amount!")
            time.sleep(1)
            total = 1.18 * amount
            total = round(total, 2)
            print(total)
            break

        if opt == 'Dollars' or 'dollars':
            print("You are currently converting from 'Dollars' to 'Pounds'")
            print()
            time.sleep(1)
            amount = float(input("Enter your amount here: "))
            time.sleep(0.5)
            print("This is your amount!")
            time.sleep(1)
            total = 1.20 * amount
            total = round(total, 2)
            print(total)
            break