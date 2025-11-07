class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict:", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


# routes = [
#     ("Mumbai","Pune"),
#     ("Mumbai", "Surat"),
#     ("Surat", "Bangaluru"),
#     ("Pune","Hyderabad"),
#     ("Pune","Mysuru"),
#     ("Hyderabad","Bangaluru"),
#     ("Hyderabad", "Chennai"),
#     ("Mysuru", "Bangaluru"),
#     ("Chennai", "Bangaluru")
# ]

# routes = [
#     ("Mumbai", "Paris"),
#     ("Mumbai", "Dubai"),
#     ("Paris", "Dubai"),
#     ("Paris", "New York"),
#     ("Dubai", "New York"),
#     ("New York", "Toronto"),
#     ("Toronto", "Toronto"),
    
# ]

# route_graph = Graph(routes)
# route_graph.get_paths("Mumbai", "New York")
# start = "Mumbai"
# end = "New York"


# print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
# print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))

# start = "Dubai"
# end = "New York"

# print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
# print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))


import collections
route={
    (1,2),
    (1,6),
    (2,3),
    (2,4),
    (3,3),
    (4,5),
    (5,5),
    (6,7),
    (6,8),
    (7,5),
    (8,8)
    
}
# route_graph=Graph(route)


#! DFS
# visited=set()
# def dfs(graph,visited,start):
#     visited.add(start)
#     print(start,end=" ")
#     for neighbour in graph[start]:
#         if neighbour not in visited:
#             dfs(graph,visited,neighbour)

# dfs(route_graph.graph_dict,visited,start)

#! BFS
import collections
def bfs(graph, start):
    que=collections.deque()
    visited = set()
    que.append(start)
    visited.add(start)
    while que:
        curr=que.popleft()
        for nei in graph[curr]:
            if nei not in visited:
                visited.add(nei)
                que.append(nei)
        print(curr, end=" ")
# bfs(route_graph.graph_dict, 1)



