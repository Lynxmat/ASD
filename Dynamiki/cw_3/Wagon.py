def max_wage(W,K):
    n = len(W)
    W.sort()
    t = W[0]
    to_spare = K%t  #kiedy optymalnie skończyć
    left = K
    cargos = []
    curr_i = n-1    #idziemy od końca
    while left>to_spare and curr_i >= 0:
        while W[curr_i] > left:     #szukamy takiego który jest mniejszy od left
            curr_i -= 1
        left -= W[curr_i]           #odejmujemy
        cargos.append(W[curr_i])
        curr_i -= 1
    return cargos