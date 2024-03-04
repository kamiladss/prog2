str1=input()
s = ''.join(char.lower() for char in str1)

if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
