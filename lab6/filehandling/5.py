fp='C:\\Users\\Lenovo\\Desktop\\university\\[f[.txt'
inpl= ["a", "b", "c", "d", "e"]
with open(fp, 'w') as file:

            for item in inpl:
                # Write the element to the file
                file.write(str(item) + '\n')
print("List successfully written to the file.")