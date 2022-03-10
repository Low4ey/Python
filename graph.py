class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def add_edge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def bfs(self,vertex):
        visited=[vertex]
        queue=[vertex]
        while queue:
            dvertex=queue.pop(0)
            print(dvertex)
            for adjvertex in self.gdict[dvertex]:
                if adjvertex not in visited:
                    visited.append(adjvertex)
                    queue.append(adjvertex)
    
    def dfs(self,vertex):
        visited=[vertex]
        queue=[vertex]
        while queue:
            dvertex=queue.pop()
            print(dvertex)
            for adjvertex in self.gdict[dvertex]:
                if adjvertex not in visited:
                    visited.append(adjvertex)
                    queue.append(adjvertex)




customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
               }
graph=Graph(customDict)
graph.dfs("a")
