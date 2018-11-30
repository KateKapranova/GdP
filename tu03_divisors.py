#algorithm to calculate divisors of an integer
#input: an integer
#output: list of divisors

def divisor(n):
    L = []
    for i in range(1, n+1):
        if n % i == 0:
            L.append(i)
    return L

#test cases
print(divisor(7))
print(divisor(8))
print(divisor(111))
print(divisor(57))
