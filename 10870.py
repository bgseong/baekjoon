import sys
li=[0,1]
n=int(sys.stdin.readline())

while len(li)-1 < n:
    li.append(li[len(li)-2]+li[len(li)-1])
print(li[n])
