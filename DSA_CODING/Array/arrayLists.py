

# nums=[2,0,2]
# queries=[[0,2,1],[0,2,1],[1,1,3]]


nums=[2]
queries =[[0,0,6],[0,0,2],[0,0,9],[0,0,5],[0,0,10]]

# nums=[8,4]
# queries=[[0,1,5],[1,1,5],[1,1,3],[1,1,4],[0,0,3],[1,1,4],[0,1,2],[1,1,3],[1,1,1]]
def transformArray(nums, queries,k):
    dif=[0]*(len(nums)+1)
    presum=0
    for i in range(k):
        l,r,val=queries[i]
        dif[l]+=val
        dif[r+1]-=val

    for i in range(len(nums)):
        presum+=dif[i]
        if presum<nums[i]:
            return False
    # print(dif)
    # print(presum)
    return True

def maxOperations(nums, queries):
    l,r=0,len(queries)
    if (not transformArray(nums,queries,r)):
        return -1
    while l<=r:
        mid=l+(r-l)//2
        if transformArray(nums,queries,mid):
            r=mid-1
        else:
            l=mid+1
    return l    

def longestSubarray():
    arr=[2,3,5,1,9]
    sm=0
    dic={}
    k=10
    ln=0
    for i in range(len(arr)):
        sm+=arr[i]
        if sm==k:
            ln=i+1
        if (sm-k) in dic:
            ln=max(ln,i-dic[sm-k])
        dic[sm]=i
    print(dic)
    print(ln)
    
arr=[1,2,4,7,7,5]
m1,m2=0,0
l1,l2=float("inf"),float("inf")

for i in range(len(arr)):
    if arr[i]>m1:
        m2=m1
        m1=arr[i]
    elif m2<=arr[i]<m1:
        m2=arr[i]
        
    if arr[i]<l1:
        l2=l1
        l1=arr[i]
    elif l2>=arr[i]>l1:
        l2=arr[i]
print(m1,m2)
print(l1,l2)
    