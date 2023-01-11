import sys
n=int(sys.stdin.readline())

for _ in range(n):
    k=int(sys.stdin.readline())
    ans=""
    while k > 0:
        ans+=str(k%2)
        k=k//2
    for i, j in enumerate(ans):
        if j=="1":
            print(i,end=" ")
    print("")
