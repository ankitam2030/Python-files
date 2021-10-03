import math

allPythagoreanTriplets = []

def findPythagoreanTriplets(limit):
    c,m = 0,2
    global allPythagoreanTriplets

    while c < limit:
        for n in range(1, m):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            allPythagoreanTriplets.append([a,b,c])
            if a + b + c == limit:
                return [a, b, c]

        m += 1


product = 1
for i in findPythagoreanTriplets(1000):
    product *= i

print(product)
