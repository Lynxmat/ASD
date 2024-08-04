#Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
#Za pomocą stosu (implementacja za pomocą tablicy)

def removeKdigits(num, k):
    n = len(num)
    stack = [num[0]]

    if k >= n:
        return "0"

    
    #Wyrzucamy liczbę gdy następna jest mniejsza
    for i in range(1,n):
        while len(stack)>0 and stack[-1] > num[i] and k > 0:
            k -= 1
            stack.pop()
        stack.append(num[i])
    
    #Wyrzucamy 0 z przodu
    while len(stack) > 0 and stack[0] == '0':
        stack.pop(0)

    #spisujemy do stringa (for jest taki, bo jest przypadek że będą na przykład same liczby, które się sobie równają)
    ans = ""
    for i in range(len(stack)-k):
        ans += stack[i]

    #Jak nic nie ma to 0
    if len(ans) == 0:
        return "0"
    
    return ans

num = "1432219"
k = 3

print(removeKdigits(num, k))
        
        
