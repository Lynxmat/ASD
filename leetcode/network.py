"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, 
a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the 
time it takes for a signal to travel from source to target.
We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for 
all the n nodes to receive the signal, return -1.
"""

from queue import PriorityQueue

def networkDelayTime(times,n,k):
    INF = float('inf')
    arr = [[] for _ in range(n)]
    for u,v,wage in times:
        arr[u-1].append((v-1,wage))

    t = [INF for _ in range(n)]
    t[k-1] = 0
    pq = PriorityQueue()
    pq.put((0,k-1))   #(time,point)

    while not pq.empty():
        point = pq.get()[1]
        for element in arr[point]:
            new_time = t[point]+element[1]
            if new_time < t[element[0]]:
                t[element[0]] = new_time
                pq.put((new_time,element[0]))

    return -1 if INF in t else max(t)

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(networkDelayTime(times,n,k))