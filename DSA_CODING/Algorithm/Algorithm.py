from collections import deque
from collections import defaultdict


grpg={1:[2,6],2:[3,4],4:[5],6:[7,8]}
graph=defaultdict(list)

for k,v in grpg.items():
    for i in v:
        #? if default dict not used 
        # if k not in graph:
        #     graph[k]=[]  
        graph[k].append(i)
        if i not in graph:
            graph[i]=[]
print(graph)

def bfs(arr,root,visited):
    q=deque()
    visited.add(root)
    q.append(root)
    while q:
        curr=q.popleft()
        print(curr,end=" ")
        for nei in arr[curr]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
visited=set()
bfs(graph,1,visited)
# print(graph)

def dfs(graph,visited,start):
    visited.add(start)
    print(start,end=" ")
    for nei in graph[start]:
        dfs(graph,visited,nei)