import sys

n=int(sys.stdin.readline())

for _ in range(n):
    l=list(map(int,sys.stdin.readline().split()))
    l.sort()
    print(l[-3])
