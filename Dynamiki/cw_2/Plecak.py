#Dwuwymiarowy problem plecakowy - wersja dyskretna, mamy wartość, wagę i wysokość przedmiotu. W - maksymalna waga, H - maks. wysokość.

def rek(weights: list,hights: list,arr: list,index: int,w: int,h: int) -> int:
    if index == 0:                              #albo bierzemy ostatni przedmiot albo nie (warunek końca) index mówi ile jeszcze jest przed rzeczą innych
        if weights[0] <= w and hights[0] <= h:
            return arr[0]
        return 0
    a = b = 0                                   #początkowo dajemy wartość 0 ponieważ weźmiemy z tych wartości maxa więc wiadomo
    a = rek(weights,hights,arr,index-1,w,h)     #a to wartość bez wzięcia obecnej rzeczy którą mamy "w łapie"
    if weights[index] <= w and hights[index] <= h:
        b = rek(weights,hights,arr,index-1,w-weights[index],h-hights[index]) + arr[index]   #jeżeli przedmiot spełnia standardy wagowe to wyliczamy b, tzn bierzemy go i wyliczamy poprzednie
    return max(a,b)                 #zwracamy maximum, bo chcemy mieć bogaty plecak


def dinamics(weights: list,hights: list,cost: list,w: int,h: int) -> int:
    n = len(cost)
    scores = [[[0 for _ in range(h+1)] for _ in range(w+1)] for _ in range(n)]

    for i in range(weights[0],w+1):
        for j in range(hights[0],h+1):
            scores[0][i][j] = cost[0]
    
    for i in range(w+1):                                    #idziemy taką kolejnością ponieważ chcemy przesuwać się ilością rzeczy najpierw a potem wysokościąi wagą
        for j in range(h+1):
            for k in range(1,n):
                scores[k][i][j] = scores[k-1][i][j]         #zapisujemy najpierw wartość bez wzięcia obecnego
                if i - weights[k] >= 0 and j - hights[k] >= 0:
                    scores[k][i][j] = max(scores[k][i][j],scores[k-1][i - weights[k]][j - hights[k]]+cost[k])   # a tu jak się warunki zgadzają to z wzięciem
    return scores[n-1][w][h]                            #zwracamy stan dla n-tej rzeczy(index n-1), o wadze pozostałej i wysokości również



def main() -> None:
    P=[1,3,2]
    weights=[4,7,6]
    heights=[5,6,3]
    print(rek(weights,heights,P,len(P)-1,12,8))
    print(dinamics(weights,heights,P,12,8))

main()