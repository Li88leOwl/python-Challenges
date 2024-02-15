#fizz buzz challenge 
#if a number is divisible by 3 print(fizz)
#if a number is divisible bt 5 print(buzz)
#if a number is divisble by both 3 & 5 print(fizzbuzz)
for num in range (0, 10000):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    
    else:
        print(num)
