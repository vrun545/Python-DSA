import collections
def bfs(adj_lst, nVertices, start_pg, end_pg):
        queue = collections.deque()
        visited =[False for i in range(nVertices+1)]
        cnt = 0
        queue.append(start_pg)
        visited[start_pg] = True
        n = len(adj_lst)
        d = []
        for i in range(n+1):
            d.append(-1)
        d[start_pg] = 0
        while queue:
            v = queue.popleft()
            visited[v] = True
            for nbr in adj_lst[v]:
                if visited[nbr] != 1:
                    queue.append(nbr)
                    d[nbr] = d[v] + 1

        if d[end_pg] == -1:
            return -1
        else:
            return d[end_pg]


nVertices = int(input())
adj_lst = {}
lst = []
k = 0
for i in range(nVertices):
    l1 = list(map(int, input().split()))
    lst.append(l1)
for i in range(1,nVertices+1):
    adj_lst[i] = lst[i-1]

start_pg, end_pg = map(int, input().split())

ans = bfs(adj_lst, nVertices,start_pg,end_pg)
if ans != -1:
    print(ans, end="")
else:
    print(-1, end="")