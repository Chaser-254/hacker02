def factorial(n):

    return 1 if (n==1 or n==0) else n * factorial(n-1);
#Driver code
    num = 5;
    print("factorial of", num,"is", factorial(num))


def factorial(n):
    if n<0:
        return 0

    elif n==0 or n==1:
        return 1
    else:
        fact = 1
        while(n>1):
            fact *= n
            n-=1
            return fact

num = 5;
print("Factorial of", num, "is", factorial(num))

import math
def factorial(n):
    return(math.factorial(n))

num = 5
print("Factorial of", num, "is", factorial(num))