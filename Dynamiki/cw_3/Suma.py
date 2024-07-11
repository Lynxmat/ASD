#Dana jest posortowana tablica n liczb, chcemy wyznaczyć liczbę x taką, że suma różnic bezwględnych |A[i] - x| dla i od 0 do n-1
#jest minimalna. Jaka jest złożoność obliczeniowa, czemu algorytm jest poprawny?

#Odpowiedź: Złożoność to O(1). Algorytm jest poprawny, bo element o indeksie n//2 jest najbliżej środka: dla nieparzystej długości
#to idealnie środkowy element, dla parzystej jeden ze środkowych. Bierzemy element możliwie środka, bo każde przesunięcie liczby o y powoduje
#wzrost sum dla elementów w kierunku przeciwnym do przesunięcia, a spadek dla elementów w kierunku zgodnym - dlatego względem elementu środkowego,
#jak się przesuniemy od niego to nowa suma będzie nie mniejsza.