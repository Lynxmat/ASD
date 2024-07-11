#Każdy klocek to przedział <a;b>. Dany jest ciąg n klocków, klocki spadają w takiej kolejności, w jakiej są w ciągu. Szukamy min.klocków do usunięcia, 
#żeby każdy kolejny klocek mieścił się w całości w tym, który spadł tuż przed nim.

from random import randint

def upper(el,t):
    return el[0] >= t[0] and el[1] <= t[1]  #To sprawdza, czy warunek zadania spełniony, czy usuwamy

def blocks(arr):
    n = len(arr)
    tab = [-1 for _ in range(n)]        #ilość usuniętych elementów
    top = [None for _ in range(n)]      #przedział obowiązujący
    return block_tower(arr,tab,top,n-1) 

def block_tower(arr,tab,top,i):         #rekurencja z zapamiętywaniem
    if i == 0:
        top[i] = arr[i]                 #obecny przedział
        tab[i] = 0                      #ustawiamy usunięte elementy na 0
        return 0
    if tab[i] == -1:                    #wykonujemy kiedy nie ma wartości ustawionej
        min_take = float('inf')         #ile jest przed naszym elementem elementów od j do i + to co daje minimum do j
        b = float('inf')
        for j in range(i):              #przechodzimy przez poprzedników
            b = block_tower(arr,tab,top,j)+(i-j-1)  #maksymalny możliwy od j do i
            if upper(arr[i],top[j]) and b < min_take:   #bierzemy min z tych b
                min_take = b
        tab[i] = min(block_tower(arr,tab,top,i-1)+1,min_take,i) #wartość funkcji to minimum z tego co wyliczyliśmy i wartość dla poprzednika + 1
        if tab[i] == block_tower(arr,tab,top,i-1)+1:  #jeżli to drugie to przedział jest taki jak poprzednie
            top[i] = top[i-1]
        else:                                         #to obecny przedział         
            top[i] = arr[i]
    return tab[i]                                     #zwracamy tego gadadka tzn ilość usuniętych bloków

def dynamic(arr):
    n = len(arr)
    tab = [-1 for _ in range(n)]
    top = [None for _ in range(n)]
    tab[0] = 0
    top[0] = arr[0]

    for i in range(1,n):                            #rekurencja wykona się n-2 raza więc zastępujemy ją pętlą i idziemy od lewej do prawej tutaj
        min_take=float('inf')
        b=float('inf')
        for j in range(i):
            if upper(arr[i],top[j]):
                b = tab[j]+(i-j-1)                  #bazujemy na tablicy
                if b < min_take:
                    min_take = b
        tab[i] = min(tab[i-1]+1,min_take) #czy potrzeba tu i?
        if tab[i] == tab[i-1]+1: 
            top[i] = top[i-1]
        else:
            top[i] = arr[i]
    return tab[i]

 

arr = [(randint(1+2*i,100),randint(101,200-2*i)) for i in range(50)]
print(blocks(arr))
print(dynamic(arr))