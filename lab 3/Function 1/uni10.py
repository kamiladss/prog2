def unique(nums):
    newl=[]
    for i in nums:
            if i not in newl:
                newl.append(i)         
    return newl
        
nums=[1,2, 3,2,4,4,5]
print(unique(nums))