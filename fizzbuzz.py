#fizz buzz challenge 
#if a number is divisible by 3 print(fizz)
#if a number is divisible bt 5 print(buzz)
#if a number is divisble by both 3 & 5 print(fizzbuzz)
#fizz buzz challenge 
choice = int(input("Enter you're number of choice: "))
def fizzbuzz(choice):

 for num in range (0, choice):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    
    else:
        print(num)

fizzbuzz(choice)
