import os

def checkp(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        
        print("Path exists")
        print("Filename is", filename)
        print("Directory is", directory)
        
    else:
        print("Path does not exist.")


path = 'C:\\Users\\Lenovo\\Desktop\\university\\[f[.txt'
checkp(path)