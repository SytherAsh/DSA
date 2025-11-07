print("START")

# arr=[1,2,3,4,5]
def koko(piles,hr):
    import math
    def help(piles,hr):
        cnt=0
        for i in range(len(piles)):
            cnt+=math.ceil(piles[i]/hr)
        return cnt

    l,r=1,max(piles)
    ans=max(piles)
    while l<=r:
        mid=l+(r-l)//2
        if help(piles,mid)<=hr:
            ans=min(ans,mid)
            r=mid-1
        else:
            l=mid+1
    print("l",l,"r",r)
    print("ans",ans)

    return ans
arr=[3,6,7,11]
# print(koko(arr,8))

def pivot(arr):
    l,r=0,len(arr)-1
    cnt=0
    while l<r:
        mid=l+(r-l)//2
        if arr[mid]>arr[mid+1]:
            l=mid+1
            cnt+=1
            
        else:
            r=mid
    if cnt>1:
        return -1    
    return(l,r) 
def Peak():
    arr=[4,5,6,1,2,3]

    l,r=0,len(arr)-1
    while l<r:
        mid=l+(r-l)//2
        print("mid",mid,"arr[mid]",arr[mid],"arr[mid+1]",arr[mid+1])
        if arr[mid]<arr[mid+1]:
            l=mid+1
        else:
            r=mid
        print("mid",mid,"l",l,"r",r)
    print(l)
# pivot(arr)    

def searchSorted(arr): 
    l,r=0,len(arr)-1
    tar=2
    while l<=r:
        mid=l+(r-l)//2
        if arr[l]<=arr[mid]:
            if arr[l]<=tar<=arr[mid]:
                r=mid-1
            else:
                l=mid+1
        else:
            if arr[mid]<=tar<=arr[r]:
                l=mid+1
            else:
                r=mid-1    
    print(l)
def MinSorted(arr):
    l,r=0,len(arr)-1
    lst=arr[l]
    ind=0
    while l<=r:
        m=l+(r-l)//2
        if arr[l]<=arr[m]:
            
            # lst=min(lst,arr[l])
            if arr[l]<lst:
                lst=arr[l]
                ind=l
            print("l",l,"m",m,"r",r,"lst",lst)
            l=m+1
        else:
            # lst=min(lst,arr[m])
            if arr[m]<lst:
                lst=arr[m]
                ind=m
            print("l",l,"m",m,"r",r,"lst",lst)
            r=m-1
    print(lst)
    print(ind)
# MinSorted([3,4,5,1,2])

def help(arr,high):
    std=1
    pg=0
    mxpg=0
    for i in range(len(arr)):
        if pg+arr[i]<=high:
            pg+=arr[i]
        else:
            std+=1
            pg=arr[i]
        # mxpg=max(mxpg,pg)
        # print(std,pg)
    return std 
def book():
    m=[25,46,28,49,24]
    n=4
    l=max(m)
    r=sum(m)   

    while l<=r:
        mid=l+(r-l)//2
        std=help(m,mid)
        print(mid,std)
        if std>n:
            l=mid+1
        else:
            r=mid-1
            
        print(l,r) 
    print("final",l,r)
# book()


def canplace(arr,dist,n):
    cnt=1
    last=arr[0]
    
    for i in range(len(arr)):
        if arr[i]-last>=dist:
            cnt+=1
            last=arr[i]
    if cnt>=n:
        return True
    else:
        return False
def Aggressivecow():
    cows=[0,3,4,7,10,9]
    n=4
    cows=sorted(cows)
    for i in range(1,cows[-1]-cows[0]):
        if canplace(cows,i,n):
            continue
        else:
            print(i-1)
            break

    l,r=1,cows[-1]-cows[0]

    while l<=r:
        mid=l+(r-l)//2
        if canplace(cows,mid,n):
            l=mid+1
        else:
            r=mid-1 
    print(l,r)

arr=[1,2,3,4,5,6]



def findKRotation(arr):
    l,r=0,len(arr)-1

    # while l<=r:
    #     m=l+(r-l)//2
    #     if arr[m+1]>arr[m]:
    #         r=m-1
    #     else:
    #         l=m+1
    # return l
    
    while l<r:
        m=l+(r-l)//2
        if arr[m+1]<arr[m]:
            l=m+1
        else:
            r=m
    return l
    
    
# nums=[4,5,6,7,0,1,2]
# nums=[1,2,3,4,5,6]
# print(findKRotation(nums))

nums=[1,2,3,3,4,4,5,5]
tar=4
l,r=0,len(nums)-1

while l<=r:
    m=l+(r-l)//2
    if nums[m]>=tar:
        r=m-1
    else:
        l=m+1
print("first",l)
        
l,r=0,len(nums)-1

while l<=r:
    m=l+(r-l)//2
    if nums[m]>tar:
        r=m-1
    else:
        l=m+1
print("last",l-1)
        