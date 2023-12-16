#GENERATE TILL N PRIME NUMBER

l = True
while l == True:
    n = int(input("Generate prime till the number: "))
    for i in range(2, n + 1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)


#generate first n numbers
l = True
while l == True: 
    n = int(input("Enter the number of primes you want: "))
    i = int(2)
    while n != 0:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
            n -= 1
        i += 1
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)


#if n is a prime number
l = True
while l == True:
    is_prime = bool(1)
    n = int(input("Enter a number: "))
    if n == 1 or n == 0:
        print(n, "is neither prime nor composite.")
    elif n>1:
        i = int(2)
        while i < n/2:
            if n % i == 0:
                is_prime = bool(0)
                break
            else:
                i += 1
        if is_prime:
            print(n, "is a prime number.")
        else:
            print(n, "is not a prime number.")
        l = input("Do you want to run the program again? (y/n): ")
        if l == "y":
            l = bool(1)
        else:
            l = bool(0)
