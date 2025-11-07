
#!dijkstra

import heapq
import collections

arr={
    (0,1,4),
    (0,2,4),
    (1,2,2),
    (2,3,3),
    (2,4,1),
    (2,5,6),
    (3,5,2),
    (4,5,3)
}
graph=collections.defaultdict(list)
for i in arr:
    s,e,w=i
    graph[s].append((e, w))
    graph[e].append((s, w))
    
def dijkstra(graph, start):
    minHeap=[(0,start)]
    parent={node:node for node in graph}
    print(parent)
    dist={node : float('inf') for node in graph}
    dist[start]=0
    while minHeap:
        dis,node =heapq.heappop(minHeap)
        print(f"Current Node: {node}, Current Distance: {dis}")
        for adjNode,adjDist in graph[node]:
            print(f"Checking adjacent node: {adjNode}, Distance: {adjDist}")
            if dis+adjDist<dist[adjNode]:
                dist[adjNode]=dis+adjDist
                heapq.heappush(minHeap,(dist[adjNode],adjNode))
                parent[adjNode]=node
                print(f"Updated distance for node {adjNode}: {dist[adjNode]}, Parent: {node}")
        print(f"Node: {node}, Distance: {dist[node]}")
    print("Final Distances:", dist)
    print("Parent Mapping:", parent)

    n=5
    print("5",end=" ")
    while n>0:
        print(parent[n], end=" ") 
        n=parent[n]
    # return dist, parent

print(graph)
dijkstra(graph, 0)

