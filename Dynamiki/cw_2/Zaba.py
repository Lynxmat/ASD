#Głodna żaba - żaba skacze po osi liczbowej, skacze od 0 do n-1 wyłącznie w kierunku większych liczb, ale jej energia nie może spaść poniżej zera.

def zabka(arr):
    n = len(arr)
    snacks = []
    for i in range(n):                      #zmiana formatu tablicy na indeks i wartość
        if arr[i]:
            snacks.append((i,arr[i]))
    snacks.append((n-1,0))                  #ten append jest po to, bo jakbyśmy usunęli ostatni element to, żeby był. Jeżeli będzie, to nic się nie stanie, bo wtedy dystans będzie 0

    def rek(tab,fuel=0,i=0,obiadki=0):
        if fuel < 0: return float("inf")    #co jeśli nie ma
        if i == len(tab)-1: return obiadki  #jak osiągniemy ostatni element to zwracamy ilość stopów
        dis = tab[i+1][0] - tab[i][0]       #wyliczenie dystansu między jednym a drugim
        return min(rek(tab,fuel-dis,i+1,obiadki),rek(tab,fuel-dis+tab[i][1],i+1,obiadki+1)) #albo jemy albo nie

    return rek(snacks)

def dinamics(arr):                   #jak chcemy jakiś warunek to można zrobić cnt i wyjść po osiągnięciu n-1 iteracji zewnętrznej
    n = len(arr)
    snacks = []
    for i in range(n):
        if arr[i]:
            snacks.append((i,arr[i]))
    m = len(snacks)                  #to samo co w rekurencji
    curr_energy = snacks[0][1]
    snacks[0] = (snacks[0][0],0)
    stops = 1                        #najpierw bierzemy do curr_energy wartość obiadku z pierwszego elementu i czyścimy wartość obiadku w samej tablicy
    while curr_energy<n-1:           #czas na pętle która wykonuję się aż energia nie będzie większa od n-1
        maks = 0
        maks_ind = -1
        for i in range(m):                          #szukanie będzie aż nie znajdziemy nie napotkamy zcegoś większego od curr_energy lub nie przejdziemy przez całość
            if snacks[i][0]>curr_energy: break      #a celem jest maxymalny obiadek
            if snacks[i][1] > maks:
                maks = snacks[i][1]
                maks_ind = i
        curr_energy += maks
        snacks[maks_ind]=(snacks[maks_ind][0],0)
        stops+=1                                    #następnie robimy to samo co z pierwszym punktem dla maks_ind
    return stops

A=[1,0]
print(zabka(A))
print(dinamics(A))
A=[3,0,1,4,0,2,0,5,1,0,1,0,0]
print(zabka(A))
print(dinamics(A))
A=[2,1,3,0,0,0,5,0,2,0]
print(zabka(A))
print(dinamics(A))