#A[n] - długości samochodów, które stoją w kolejce do promu. Prom ma dwa pasy (lewy i prawy każdy długości l). Należy wyznaczyć,
#które samochody powinny pojechać na który pas, żeby na promie zmieściło się najwięcej aut. Auta wjeżdżają w takiej kolejności, jak w tablicy A.
#zwraca max ile się aut zmieści

def rek(i,l1,l2,arr):                                       #i to ilość aut rozpatrywanych, dlatego w indeksach odejmujemy 1
    if i == 0:
        return 0

    maks = 0
    if l1 >= arr[i-1]:
        maks = rek(i-1,l1-arr[i-1],l2,arr)+1                #dodajemy albo do jednej albo do drugiej linii
    if l2 >= arr[i-1]:
        maks = max(maks,rek(i-1,l1,l2-arr[i-1],arr)+1)

    return maks

def dinamics(l1,l2,arr):
    n = len(arr)
    DB = [[[0 for _ in range(l2+1)] for _ in range(l1+1)] for _ in range(n+1)]  #3 wymiary bo ilość aut i 2 pozostałe na długość linii

    for i in range(l1+1):
        DB[0][i][l2] = 1                #jedynki to oznaczają pojawienie się takiej opcji

    for i in range(l2+1):
        DB[0][l1][i] = 1
    
    i = 1                               #zlicza ilość aut

    while i < n+1:
        flag = False
        for j in range(l1+1):
            for k in range(l2+1):       #Idziemy po l1 i l2
                if DB[i-1][j][k]:       #Czy i-1 j k jest 1
                    if j >= arr[i-1]:
                        DB[i][j-arr[i-1]][k] = 1    #flag ustawiamy na True i na samym końcu dodajemy jedynkę, jeżeli gdzieś się pojawiło
                        flag = True
                    if k >= arr[i-1]:
                        DB[i][j][k-arr[i-1]] = 1
                        flag = True
        
        if not flag:                            #jeśli nie to break
            break
        i += 1
    return i-1

c=[3,5,5,5]
print(rek(len(c),9,9,list(reversed(c))))
print(dinamics(9,9,c))

