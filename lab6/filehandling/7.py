with open('C:\\Users\\Lenovo\\Desktop\\PP2\\lab6\\alphabetfiles\\A.txt','r') as firstfile, open('C:\\Users\\Lenovo\\Desktop\\PP2\\lab6\\alphabetfiles\\A2.txt','a') as secondfile: 
    for line in firstfile: 
             secondfile.write(line)