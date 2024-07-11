#f(x) = min F(x-t)+1

def change(x,M,mem):
    if x == 0:
        return 0
    if x in mem:
        return mem[x]
    best = float("inf")
    for t in M:
        if t <= x:
            tmp = change(x-t,M,mem)+1
            if tmp<best:
                best = tmp
    mem[x] = best
    return mem[x]