def gener(n):
    for i in range(n,-1,-1):
        yield i
        
n=int(input())
for i in gener(n):
    print(i)