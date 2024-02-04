
import math
def volumeSphere(r):
    V=float(4/3*math.pi*pow(r,3))
    print(V)

r=float(input())
volumeSphere(r)