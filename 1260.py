import sys
from collections import deque


def dfs(dic, v,visit):
    visit[v]=1
    print(v,end=" ")
    if v in dic.keys():
        for i in dic[v]:
            if visit[i] == 0:
                dfs(dic,i,visit)



def bfs(dic, v,visit):
    li=deque([v])
    while li:
        a=li.popleft()
        visit[a] = 1
        print(a, end=" ")
        if a in dic.keys():
            for i in dic[a]:
                if visit[i] == 0 and i not in li:
                    li.append(i)




n,m,v=map(int,sys.stdin.readline().split())
dic={}
visit=[0]*(n+1)
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    try:
        dic[a].append(b)
        dic[a]=sorted(dic[a])
    except:
        dic[a] = [b]
    try:
        dic[b].append(a)
        dic[b] = sorted(dic[b])
    except:
        dic[b] = [a]

dfs(dic,v,visit)
visit=[0]*(n+1)
print("")
bfs(dic,v,visit)

