s = "Hello World"
u = sum(1 for c in s if c.isupper())
l = sum(1 for c in s if c.islower())
print("Upper case:", u, "\nLower case:", l)