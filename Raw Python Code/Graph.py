
"""Complete Graph Implementatiom Using Adjacency Matrix Along with Graph Traversal Methods 
i.e. BFS(Breadth First Search) and DFS(Depth First Search) -------------"""

from pydoc import visiblename
from collections import deque
from ast import NodeVisitor
from typing import Deque
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.AdjacencyMatrix = [[0 for i in range(nVertices)]for i in range(nVertices)]
    
    def add_Edges(self,v1,v2):
        self.AdjacencyMatrix[v1][v2] = 1
        self.AdjacencyMatrix[v2][v1] = 1
    
    def RemoveEdge(self,v1,v2):
        self.AdjacencyMatrix[v1][v2] = 0
        self.AdjacencyMatrix[v2][v1] = 0

    def DoesContainEdge(self,v1,v2):
        if self.AdjacencyMatrix[v1][v2] > 0:
            return True
        else:
            return False

    def __dfs_Helper(self, sv, visited):        # SV IS SOURCE VERTEX
        print(sv, end = ' ')
        visited[sv] = True
        for i in range(self.nVertices):
            if self.AdjacencyMatrix[sv][i] > 0 and visited[i] is False:
                self.__dfs_Helper(i,visited)

    def DFS(self):
        visited = [False for i in range(self.nVertices)]
        self.__dfs_Helper(0, visited)

    def bfs(self):
        q = deque()
        visited =[False for i in range(self.nVertices)]
        q.append(0)
        visited[0] = True
        while q:
            vtx1 = q.popleft()
            print(vtx1, end=' ')
            for i in range(self.nVertices):
                if self.AdjacencyMatrix[vtx1][i]>0 and visited[i] is False:
                    visited[i] = True
                    q.append(i)

    def __str__(self):
        return str(self.AdjacencyMatrix)


# DRIVER CODE
if __name__ == "__main__":
    g = Graph(5)
    g.add_Edges(0,1)
    g.add_Edges(1,3)
    g.add_Edges(2,3)
    g.add_Edges(0,2)
    g.add_Edges(2,4)
    print(g)
    print("The DFS Traversal of Graph =", end = " ")
    g.DFS()
    print("\nThe BFS Traversal of Graph =", end = " ")
    g.bfs()

