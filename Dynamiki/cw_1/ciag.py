#suma
#F(s,k) = czy można zbudować podciąg o sumie s z pierwszych k elementów tablicy A
#F(s,k) = F(s,k-1) or F(s-A[k-1],k-1)
#F(0,k) = True, F(s,0) = False dla s > 0

def f(A,T):
    n = len(A)
    F = [[None for _ in range(n+1)] for _ in range(T+1)]

    for i in range(n+1):
        F[0][i] = True
    for i in range(1,T+1):
        F[i,0] = False
    for s in range(1,T+1):
        for k in range(1,n+1):
            if s-A[k-1] >= 0:
                f1 = F[s-A[k-1]][k-1]
            else:
                f1 = False
            f2 = F[s][k-1]
            F[s][k] = f1 or f2
    return F[T][n]
