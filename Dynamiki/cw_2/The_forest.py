#Las rosnący na osi liczbowej (pozycje od 0 do n-1, n drzew). Dla każdego i znamy zysk c_i. Chcemy uzyskać maksymalny zysk, ale nie można ścinać 
#dwóch drzew z rzędu.

def rek(i,c):
    if i == 0:
        return c[0]                 #pierwsze ścinamy bo chcemy mieć jak największy zysk
    if i == 1:
        return max(c[0],c[1])       #Tutaj bierzemy maxa z pierwszego i drugiego lasu

    return max(rek(i-1,c),rek(i-2,c)+c[i])     #I analizujemy czy ścinamy poprzednie, czy obecne i i-2 las

def rek_memory(i,c,values):
    if values[i] is not None:
        return values[i]
    if i == 0:
        return c[0]
    if i == 1:
        return max(c[0],c[1])

    return max(rek(i-1,c),rek(i-2,c)+c[i])

def dinamics(c):
    n = len(c)
    values = [0 for _ in range(n)]

    values[0] = c[0]
    values[1] = max(c[0],c[1])

    for i in range(2,n):
        values[i] = max(values[i-1],values[i-2]+c[i])
    
    return values[n-1]





c = [2,3,5,7]
n = len(c)
values = [None]*n
print(rek(n-1,c))
print(rek_memory(len(c)-1,c,values))
print(dinamics(c))
