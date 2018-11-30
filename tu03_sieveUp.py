#algorithm implementing sieve of Erastophenes UPGRADED VERSION
#includes the measurement of execution time
#input: a positive integer n
#ouput: a list of prime numbers smaller or equal to n
import time

def sieveUp(n):
    start = time.time()
    L = []
    for j in range(2, n+1):
        L.append(j)
    listProducts = []
    for i in range(2, n+1):
        for k in range(2, n+1):
            dummy = i*k
            if dummy <= n:
                listProducts.append(dummy)
            else:
                continue
    #print(listProducts)
    primeList = list(set(L)-set(listProducts))
    end = time.time()
    print(end - start)
    return primeList


#test cases
#print(111 ,sieveUp(111))
#print(44 ,sieveUp(44))
#print(57 ,sieveUp(57))
#print(17 ,sieveUp(17))
print(1000,sieveUp(1000)) #observe the execution time
