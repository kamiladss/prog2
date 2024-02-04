print("How many Fahrenheit?")
a = float(input())

def convertFToC(F):
    C = (5 / 9) * (F - 32)
    print(C)

convertFToC(a)
