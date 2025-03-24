def CheckPrime(number):
    check=True
    if number < 2:
        check= False
    elif number % 2 == 0 and number > 2:
        check= False
    else:
        for i in range(2, int(number/2)):
            if number % i == 0:
                check= False
            else:
                check= True
    return check

num = int(input("Enter a number: "))
if CheckPrime(num):
    print("%d is a prime number." % num)
else:
    print("%d is not a prime number." % num)
