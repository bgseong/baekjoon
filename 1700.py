import sys

n,k=map(int,sys.stdin.readline().split())

li=list(map(int,sys.stdin.readline().split()))

multi=[0]*n
count=0

for i in range(k):
    if li[i] in multi:
        pass
    elif 0 in multi:
        multi[multi.index(0)] = li[i]
    else:
        if i<k-1:
            tmp=set(multi)&set(li[i+1:])
        else:
            tmp=[]
        if tmp:
            imp=set(multi)&set(tmp)
            if len(imp) == len(multi):
                maxi = max(imp, key=lambda x:li[i+1:].index(x))
                multi[multi.index(maxi)] = li[i]
                count+=1
            elif imp:
                a=set(multi)-set(imp)
                multi[multi.index(list(a)[0])] = li[i]
                count+=1
        else:
            multi[0]=li[i]
            count+=1
print(count)



