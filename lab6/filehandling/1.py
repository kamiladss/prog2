import os
directs=[]
fils=[]
path = 'C:\\Users\\Lenovo\\Desktop\\university'
print("Directories")
for x in os.listdir(path):
    if os.path.isdir(os.path.join(path, x)):
        directs.append(x)
print(directs)   
print("Files")
for x in os.listdir(path):
    if os.path.isfile(os.path.join(path, x)):
        fils.append(x)
print(fils)
for root, dirs, files in os.walk(path):
    for dir in dirs:
        print(os.path.join(root, dir))
    for file in files:
        print(os.path.join(root, file))