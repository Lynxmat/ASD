"""Mamy zbiór punktów X={x1,x2,...,xn} na prostej. Szukamy minimalnej liczby przedziałów jednostkowych domkniętych, żeby pokryć wszystkie punkty z X."""

def intervals(A)->int:
    A.sort()                                #sortujemy
    n=len(A)
    last_index = 0                          #index elementu ostatniego dla którego przedział jednostkowy był robiony
    res = 1                                 #ilość przedziałów
    for i in range(1,n):
        if A[i] > A[last_index] + 1:        #sprawdzamy czy rozpatrywany punkt mieści się
            res += 1
            last_index = i
    return res

def main()->None:
    A = [0.5,1.6,0.25]
    print(intervals(A))

main()