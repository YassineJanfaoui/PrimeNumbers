divisor = 1
number = int(input())

if number == 1:
    print("1 isn't a prime number")
elif number == 0:
    print("0 isn't a prime number")

while divisor < number:
    divisor += 1
    if number % divisor == 0 and number != divisor:
        print("this number isn't prime")
        break
    if number == divisor and number % divisor == 0:
        print("this number is prime")
