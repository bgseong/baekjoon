import sys
n=int(sys.stdin.readline())
s=list(map(int,sys.stdin.readline().split()))

k=list(map(int,sys.stdin.readline().split()))

maxi=-1e9
mini=1e9

def dfs(depth,total,plus,minus,multiple,divide):
    global maxi, mini
    if depth == n:
        maxi=max(maxi,total)
        mini=min(mini,total)
        return
    if plus:
        dfs(depth + 1, total + s[depth], plus - 1, minus, multiple, divide)
    if minus:
        dfs(depth + 1, total - s[depth], plus, minus-1, multiple, divide)
    if multiple:
        dfs(depth + 1, total * s[depth], plus, minus, multiple-1, divide)
    if divide:
        dfs(depth + 1, int(total / s[depth]), plus, minus, multiple, divide-1)

dfs(1,s[0],k[0],k[1],k[2],k[3])
print(maxi)
print(mini)
