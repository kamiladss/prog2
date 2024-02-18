import math
n=int(input())
l=int(input())

res=int(n*l*l/4*(1/math.tan(math.pi/n)))
print("Input number of sides:", n)
print("Input the length of a side:", l)
print("The area of the polygon is:", res)
