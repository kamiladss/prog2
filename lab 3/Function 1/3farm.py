"""print("heads?")
h=int(input())
print("legs?")
l=int(input())
"""
h=35
l=94

def solve(nh, nl):
    rabbits=(nl-2*nh)/2
    chickens=nh-rabbits
    print(int(rabbits), int(chickens))
    
solve(h, l)