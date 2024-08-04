#two (three) pointers pattern
#Topic
#An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5. Given an integer n, return the nth ugly number.

def nthUglyNumber(n):
    ans = [0]*n
    ans[0] = 1
    #2,3,5
    index = [0,0,0]

    for i in range(1,n):
        ans[i] = min(ans[index[0]]*2,ans[index[1]]*3,ans[index[2]]*5)
        if ans[i] == ans[index[0]]*2: index[0] += 1
        if ans[i] == ans[index[1]]*3: index[1] += 1
        if ans[i] == ans[index[2]]*5: index[2] += 1
    
    return ans[-1]

n = 10
print(nthUglyNumber(n))