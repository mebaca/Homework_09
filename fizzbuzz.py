print("FizzBuzz")

x = int(input("Select a number between 1 and 100 "))

for y in range (1, x+1):
    if y % 3  == 0 and y % 5 == 0:
        print("fizzbuzz")
    elif y % 3 == 0:
        print("fizz")
    elif y % 5 == 0:
        print("buzz")
    else:
        print(y)

