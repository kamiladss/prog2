from time import sleep
from math import sqrt

n = int(input())
m = int(input())
sleep(m / 1000) 
r = sqrt(n)
print(f"Square root of {n} after {m} milliseconds is {r}")