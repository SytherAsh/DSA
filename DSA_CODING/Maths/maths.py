import math
def prime(n):
    if n==0 or n==1:
        return False
    print(int(math.sqrt(n)))
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            return False
    return True
# print(prime(156))
def Seive(n):
    n=100
    arr=[1]*n
    for i in range(2,int(math.sqrt(n))):
        if prime(i):
            for j in range(i*i,n,i):
                arr[j]=0
    print(arr)

def primeN(arr,n):
    if n==0 or n==1:
        return 0

    arr=[1]*(n)
    arr[0]=arr[1]=0
    for i in range(2,int(math.sqrt(n))+1):
        if arr[i]:
            for j in range(i*i,n,i):
                arr[j]=0
    return sum(arr)

def GCD(a,b):
    print(a,b)
    if b==0:
        return a
    return GCD(b,a%b)
# print(GCD(10,15))
# print(GCD(15,10))

def LCM(a,b):
    return a*b//GCD(a,b)
# print(LCM(10,15))

def exp(a,b):
    res=1
    while b>0:
        if(b%2==1):
            res=res*a
        a=a*a
        b=b//2
    return res
# print(exp(2,3))

def DTB(d):
    res=0
    exp=0
    
    while d>0:
        res+=(d%2)*(10**exp)
        d=d//2
        exp+=1
    return res

def BTD(b):
    res=0
    exp=0
    
    while b>0:
        res+=(b%10)*(2**exp)
        b=b//10
        exp+=1
    return res
# print(DTB(10))

# s="abc"
# v=list(map(str,s))
# print(v)

# s="12345"
# l=list(map(int,s))
# print(type(l[0]))

# c="1 2 3 4 5 6 7 "
# ct=map(int,c.split())
# print(list(ct))
nums = [1,2,3]

def permuate(ind,arr,ans):
    if ind==len(arr):
        ans.append(arr)
        return
    
    for i in range(ind,len(arr)):
        arr[ind],arr[i]=arr[i],arr[ind]
        permuate(ind+1,arr,ans)
        arr[ind],arr[i]=arr[i],arr[ind]  # backtrack
# print("Permutations:")
ans = []
# permuate(0, nums, ans)
# print(ans)

arr=[1,2,3,4,5,7,6]
ind=3
print(arr)
print(arr[:ind])
print(arr[:ind:-1])

val=reversed(arr[ind+1:])
print(arr[:ind]+list(val))