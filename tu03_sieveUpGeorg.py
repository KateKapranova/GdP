from math import sqrt
import time

def sieveUpG(N):
    #N = 1000
    start = time.time()
    prim = list(range(2,N))
    for i in range(2,int(sqrt(N))+1):
        if (i in prim):
            for k in range(i,int(N/i)+1):
                if i*k in prim:
                    prim.remove(i*k)

    end = time.time()
    print(end-start)

    #z=-1
    #for i in prim:
    #    z+=1
    #    if not z%10:
    #        print("\n")
        #print(i,end=',')
    return prim

print(sieveUpG(1000))
