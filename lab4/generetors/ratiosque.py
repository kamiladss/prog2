def gener(a,b):
    for i in range(a,b+1):
        yield i*i
        
a=int(input())
b=int(input())
for i in gener(a,b):
    print(i)