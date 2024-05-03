import queue

def bfs(nVertices,adj_List,start,final):
        q = queue.Queue()
        visited =[False for i in range(nVertices)]
        q.put(start)
        visited[0] = True
        while q:
            u = q.get()
            print(u)
            for i in range(nVertices):
                if adj_List[u][i]>0 and visited[i] is False:
                    visited[i] = True
                    q.put(i)

if __name__ == "__main__":

    nVertices = int(input())
    adj_List = {}
    i = 0
    t = nVertices

    while t-i>0:
        pass

    bfs(nVertices, adj_List, start, final)
    while t>0:
        l1 = list(map(int,input().split()))
        t -= 1