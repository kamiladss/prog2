import string

alphabet = string.ascii_uppercase

for x in alphabet:
    filename ="C:\\Users\\Lenovo\\Desktop\\PP2\lab6\\alphabetfiles\\"+ x + ".txt"
    file = open(filename, "w")
    file.write("File " + x)