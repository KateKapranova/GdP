#algorithm which decides if a number is prime
#algorithm checks if a number can be divided by anything apart from 1 and itself
def primeCheck(n):
  for i in range(2, n):
    if n % i == 0:
      return "is not prime"
  return "is prime"

#test cases:
print(7 ,primeCheck(7))
print(111 ,primeCheck(111))
print(44 ,primeCheck(44))
print(57 ,primeCheck(57))
print(17 ,primeCheck(17))
print("")


#another algorithm which decides if a number is prime
#uses the list of divisors
def primeCheck2(n):
    L = []
    for i in range(1, n+1):
        if n % i == 0:
            L.append(i)
    if len(L) == 2:  #1 is not prime by definition
        return "is prime"
    else:
        return "is not prime"

#test cases:
#print(7 ,primeCheck2(7))
#print(111 ,primeCheck2(111))
#print(44 ,primeCheck2(44))
#print(57 ,primeCheck2(57))
#print(17 ,primeCheck2(17))
