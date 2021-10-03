import math
import copy

# A function to print all prime factors of
# a given number n
def primeFactors(n):
    allPrimeFactors = [1]
    temp = n
    # Print the number of two's that divide n
    while n % 2 == 0:
        allPrimeFactors.append(2)
        n = n // 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,n+1,2):

        # while i divides n , print i ad divide n
        while n % i== 0:
            allPrimeFactors.append(i)
            n = n // i

    # Condition if n is a prime
    if len(allPrimeFactors) == 1:
        allPrimeFactors.append(temp)
    # number greater than 2
    return allPrimeFactors


# print(primeFactors(17))
def smallestMultiple(n):
    factors = []
    for i in range(3, n+1):
        temp = copy.deepcopy(factors)
        currfactors = primeFactors(i)
        print(currfactors)
        print(temp)
        for i in currfactors:
            if i in temp:
                print(i)
                temp.remove(i)
                currfactors.remove(i)

        for i in currfactors:
            factors.append(i)

    return factors


print(smallestMultiple(10))
