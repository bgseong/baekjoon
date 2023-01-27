import sys
from collections import deque

n=int(sys.stdin.readline())
li=[[] for _ in range(n+1)]
visit=[0]*(n+1)
m=int(sys.stdin.readline())
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    li[a].append(b)
    li[b].append(a)


def bfs(maps,visit):
    count=0
    li=deque([1])
    visit[1] = 1
    while li:
        x=li.popleft()
        for i in maps[x]:
            x_i=i
            if x_i< n+1 and x_i>0:
                if visit[x_i] == 0:
                    li.append(x_i)
                    visit[x_i] = 1
                    count+=1
    return count
print(bfs(li,visit))


