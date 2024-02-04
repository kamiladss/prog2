s=input()
nums = [int(num) for num in s.split()]

def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            print("True")
            return
        
    print("False")
                    
has_33(nums)
    