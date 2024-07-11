"""Problem stacji benzynowych - jedziemy z miasta A do miasta B, A jest na pozycji 0, B na pozycji n-1. Spalanie 1l/1km, w baku
mieści się L litrów. Na niektórych pozycjach są stacje benzynowe. a) chcemy, by łączna liczba tankowań była minimalna. b) chcemy minimalnego
kosztu, każda stacja ma cenę za 1l, w każdej stacji możemy tankować dowolną ilość paliwa. c) jak w b), ale musimy tankowac do pełna. """

from queue import PriorityQueue

def min_tank(stations,L)->tuple: #a
    n = len(stations)
    far = [0]                               #Tutaj mamy listę, gdzie dokonaliśmy tankowań
    tanks = 1                               #ilość (1 bo pierwsze tankowanie na starcie)
    position = 0                            #nasz psełdo iterator
    while position < n-L:                   #wykonujemy aż dopuki odległość do końca nie jest mniejsza od L
        prev = position
        position += L
        while not stations[position]:       #idziemy najpierw co L, a potem jeżeli tam nie ma stacji to szukamy wcześniejszej stacji. Można zrobić warunek, że jak wrócimy do stacji poprzedniej to return -1
            position -= 1
            if position == prev:
                return -1
        far.append(position)
        tanks += 1
    return tanks,far

def min_cost(cost,b,e)->int: #c
    min_ind=len(cost)
    min_val=float('inf')
    for i in range(b,e+1):                      #przedział od b do e
        if cost[i] and cost[i] <= min_val:
            min_val=cost[i]
            min_ind=i
    return min_ind


def full_tank_min_cost(stations,cost,L)->int:
    n = len(cost)
    money = cost[0] * L
    i = 1
    while i < n-L:
        min_ind = min_cost(cost,i,min(i+L-1,n-1))       #to min w środku jest na wypadek wyjścia poza tablicę
        money = (min_ind-i+1)*cost[min_ind]
        i = min_ind+1
    return money

#podpunkt b trzeba rozpatrzeć dynamicznie



def main()->None:
    stations=[1,0,1,0,1,0,0,1,0,0]
    costs=[5,0,3,0,1,0,0,4,0,0]
    L=4
    print(min_tank(stations,L))
    print(full_tank_min_cost(stations,costs,L))

main()