def fact(n):
    if n==0:
        return 1
    return fact(n-1)*n
# print(fact(5))

def pascal(rowIndex):
        res=[1]
        for i in range(rowIndex):
            next_row=[0]*(len(res)+1)
            for j in range(len(res)):
                next_row[j]+=res[j]
                next_row[j+1]+=res[j]
            res=next_row
        return res
def triangle(num):
    nums=list(map(int,num))
    # print(nums)
    while len(nums)>1:
        res=[0]*(len(nums)-1)
        for i in range(1,len(nums)):
            res[i-1]=(nums[i]+nums[i-1])%10
        # print(res)
        nums=res
    return nums
# print(triangle("12345"))
n=6
def pascal(n):
    res=[]
    ans=1
    res.append(ans)
    # print(1,end=" ")
    for i in range(1,n):
        ans*=(n-i)
        ans=ans/(i)
        # print(int(ans),end=" ")
        res.append(int(ans))
    return res
temp=[]
for i in range(n):
    temp.append(pascal(i+1))
print(temp)