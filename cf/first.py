# t = int(input())
# for _ in range(t):
#     a, b, c = map(int, input().split())
#     total = a + b + c
#     if total % 3 == 0:
#         target = total // 3
#         if target >= a and target >= b and target <= c:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("NO")

t= int(input())
for _ in range(t):
    n= int(input())
    a= list(map(int, input().split()))
    prefix=[0]*n
    prefix[0]=a[0]
    for i in range(1,n):
        prefix[i]=max(prefix[i-1],a[i])
    
    suff=[0]*(n+1)
    for i in range(n-1,-1,-1):
        suff[i]=suff[i+1]+a[i]
    
    ans=[]
    for k in range(1,n+1):
        best=suff[n-k]
        if n-k-1>=0:
            best=max(best,suff[n-k+1]+prefix[n-k-1])
        ans.append(best)
    
    print(*ans)

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    alice = -1
    bob = -1

    for i in range(n):
        if s[i] == 'A':
            alice = max(alice, i + 1)  # card numbers are i+1
        else:
            bob = max(bob, i + 1)

    if alice > bob:
        print("Alice")
    else:
        print("Bob")
