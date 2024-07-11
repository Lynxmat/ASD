#Mamy zbiór zadań T={t1,t2,...,tn}. Każde zadanie ti ma dodatkowo deadline d(ti) oraz zysk g(ti) [liczby naturalne]. Każde zadanie
#zabiera jednostkę czasu, zaczynamy w chwili 0. Uwaga - zysk liczymy tylko wtedy, gdy zdążymy  przed terminem! Szukamy doboru zadań, żeby zysk
#był maksymalny. Pomysł: idziemy od końca i wybieramy najbardziej opłacalne zadanie. Sortujemy malejąco po deadline, można np.
#wykorzystać max_heap.

#zadanie 3
def tasks(G,D):
    n = len(G)
    oplacalnosc = []

    for i in range(n):
        oplacalnosc.append((G[i]/D[i],D[i],G[i]))      #D != 0
    
    oplacalnosc.sort()
    oplacalnosc.reverse()

    dzien = 1
    iterator = 0
    koniec = max(D)
    rezultat = 0

    while dzien <= koniec and iterator < n:
        while oplacalnosc[iterator][1] < dzien:
            iterator += 1
        
        rezultat += oplacalnosc[iterator][2]
        iterator += 1
        dzien += 1
    
    return rezultat

#testy
gains=[10,6,7,5,3,1]
deadlines=[4,2,3,4,2,1]
print(tasks(gains,deadlines))
gains=[8,6,12,5,9,4]
deadlines=[8,5,4,4,6,2]
print(tasks(gains,deadlines))
gains=[10,4,6,7,11,5,3,8,1,2]
deadlines=[1,2,1,2,1,2,1,2,1,2]
print(tasks(gains,deadlines))
gains=[10,4,6,7,6]
deadlines=[1,1,1,1,5]
print(tasks(gains,deadlines))