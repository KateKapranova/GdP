def decToBin(n):
  bin = '' #leerer String
  while n > 0:
    bin = str(n % 2) + bin
    n = n // 2
  return int(bin)

print(decToBin(15))
print(decToBin(25))
print(decToBin(70))
