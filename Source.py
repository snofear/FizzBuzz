def FizzBuzz():
    max = int(input("Select a number between 1 and 100.\n"))
    for number in range (1, max+1):
        if number % 3== 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)




if __name__ == "__main__":
    FizzBuzz()