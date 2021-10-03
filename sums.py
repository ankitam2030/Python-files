def sumOfSquares(n):
    return n*(n+1)*(2*n+1)/6


def squareOfSum(n):
    return pow(n*(n+1)/2,2)


print(squareOfSum(100) - sumOfSquares(100))
