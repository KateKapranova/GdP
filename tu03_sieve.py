#algorithm implementing sieve of Erastophenes (naive approach)
#includes the measurement of execution time
#input: a positive integer n
#ouput: a list of prime numbers smaller or equal to n
import time

def sieve(n):
    start = time.time()
    L = []
    for j in range(2, n+1):
        L.append(j)
    listProducts = []
    for i in range(2, n+1):
        for k in range(2, n+1):
            dummy = i*k
            listProducts.append(dummy)
            #print(listProducts)
    #set arithmetic: difference between two sets (with appropriate casting)
    primeList = list(set(L)-set(listProducts))
    end = time.time()
    print(end - start)
    return primeList

#test cases
#print(111 ,sieve(111))
#print(44 ,sieve(44))
#print(57 ,sieve(57))
#print(17 ,sieve(17)) #observe only this output for aufgabe2(b)
print(1000,sieve(1000)) #observe the execution time
