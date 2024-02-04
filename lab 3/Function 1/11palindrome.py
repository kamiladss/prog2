def palindrome(st):
    n=len(st)
    for i in range(int((n-1)/2)):
            if st[i]!=st[n-i-1]:
                return False
    return True     
    

        
st="madam"
print(palindrome(st))