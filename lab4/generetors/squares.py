n= int(input())
gen =(i*i for i in range(n+1))
for i in gen:
    print(i)
    
    #or
    
def gener(n):
    for i in range(n+1):
        yield i*i
for i in gener(n):
    print(i)