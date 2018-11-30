#algorithm which finds all prime numbers which are smaller or equal to the input

def primeCheck(n):
  for i in range(2, n):
    if n % i == 0:
      return 0 #not prime
  return 1  #prime

def primeListUp(n):
    ListOfPrimes = []
    for i in range(2, n+1):
        prime = primeCheck(i)
        if prime == 1:
            ListOfPrimes.append(i)
    return ListOfPrimes


#without help function
def primeList(n):
    ListOfPrimes = []
    for i in range(n, 0, -1):
        dummyL = []
        for j in range(n, 0, -1):
            if i % j == 0:
                dummyL.append(j)
        if len(dummyL) == 2 or len(dummyL) == 1:
            ListOfPrimes.append(i)
    return ListOfPrimes

#test cases
print(111 ,primeListUp(111))
print(44 ,primeListUp(44))
print(57 ,primeListUp(57))
print(17 ,primeListUp(17))
