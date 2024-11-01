## set vaiable number to value
number = 1
## cereate while loop comparing to set number
## check number to see if divisible by given number
## output desired word
while number <= 100:
    if number % 3 == 0 and number % 5 == 0:
       print("FizzBuzz")
    elif number % 3 == 0:
       print("Fizz")
    elif number % 5 == 0:
       print("Buzz")
    else:
       print(number)
## update variable by 1 ubtil loop is finished       
    number = number + 1