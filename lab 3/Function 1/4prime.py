stroke=input()
list=list(stroke.split(" "))
primelist=[]
def filter_prime(s):
    global primelist
    n=int(s)
    if int(n) > 1:
        for i in range(2,int(n/2)+1):
            if (n%i) == 0:
                break
        else:
            primelist.append(n)
    
for x in list:
    filter_prime(x)
print(primelist)