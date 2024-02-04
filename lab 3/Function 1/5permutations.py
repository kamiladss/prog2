s = input("Enter a string: ")
slist = list(s)

def permutations(stroke, index=0):
    if index == len(stroke) - 1:
        print(''.join(stroke))
    else:
        for i in range(index, len(stroke)):
            # Swap 
            stroke[index], stroke[i] = stroke[i],stroke[index]
            # Recursive for checking next index
            permutations(stroke, index + 1)
            # Swap back to check other order
            stroke[index], stroke[i] = stroke[i], stroke[index]

permutations(slist)