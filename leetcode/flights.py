from queue import PriorityQueue

#There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there 
#is a flight from city fromi to city toi with cost pricei.
#You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, 
#return -1.


def convert(arr,n):
    graph = [[] for _ in range(n)]

    for fr,to,cost in arr:
        graph[fr].append((to,cost))
    
    return graph

def f(n, flights, src, dst, k):
    flights = convert(flights,n)
    dis = [[float('inf')]*(k+2) for _ in range(n)]  #Ile stopów do dyspozycji zostąło (+2 bo nie wliczamy start i stop)
    dis[src][k+1] = 0
    pq = PriorityQueue()
    pq.put((0,src,k+1)) #dis,point,stops

    while not pq.empty():
        cost,point,stops = pq.get()
        if point == dst:
            return cost
        if stops == 0:
            continue
                
        for element,wage in flights[point]:
            new_dis = cost + wage
            if dis[element][stops-1] > new_dis:
                dis[element][stops-1] = new_dis
                pq.put((new_dis,element,stops-1))

    return -1

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

print(f(n, flights, src, dst, k))