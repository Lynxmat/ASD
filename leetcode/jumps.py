"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your 
maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""

def canJump(nums):
    n = len(nums)
    is_posible = [False for _ in range(n)]
    is_posible[0] = True

    for i in range(n-1):
        if not is_posible[i] or nums[i] == 0: continue
        
        for j in range(i+1,i+nums[i]+1):
            if j >= n:
                return True
            is_posible[j] = True
    
    return is_posible[n-1]

print(canJump([3,2,1,0,4]))