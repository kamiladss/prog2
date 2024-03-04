import os
path = 'C:\\Users\\Lenovo\\Desktop\\PP2\\lab6\\alphabetfiles\\for delete.txt'  

if os.path.exists(path) and os.access(path, os.W_OK):
    os.remove(path)
    print("File deleted.")
else:
    print("File does not exist or is not writable.")