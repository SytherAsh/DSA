import heapq

class MedianFinder:

    def __init__(self):
        self.small,self.large=[],[]


    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-1*num)

        if(self.small and self.large and (-1*self.small[0])>self.large[0]):
            val=-1*heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        if len(self.small)>len(self.large)+1:
            val=-1*heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        
        if len(self.large)>len(self.small)+1:
            val=heapq.heappop(self.large)
            heapq.heappush(self.small,-1*val)

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -1*self.small[0]
        if len(self.small)<len(self.large):
            return self.large[0]
        return (-1*self.small[0]+self.large[0])/2

# # Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# param_2 = obj.findMedian()
# print(param_2)
# obj.addNum(3)
# param_2 = obj.findMedian()
# print(param_2)
def kClosest(points, k):
    points =[[68,97],[34,-84],[60,100],[2,31],[-27,-38],[-73,-74],[-55,-39],[62,91],[62,92],[-57,-67]]

    k = 5
    cnt=0
    maxHeap = []
    for x,y in points:
        dist=x*x+y*y
        if cnt<k:
            heapq.heappush(maxHeap,[-1*dist,x,y])
            cnt+=1
        else:
            dist2,x2,y2=heapq.heappop(maxHeap)
            dist2=-1*dist2
            if dist<=dist2:
                heapq.heappush(maxHeap,[-1*dist,x,y])
            else:
                heapq.heappush(maxHeap,[-1*dist2,x2,y2])

        print(maxHeap)
    ls=[]
    for x,y,z in maxHeap:
        ls.append([y,z])
    print(ls)
    d
def topKFrequent(nums, k): 
    stones = [2,7,4,1,8,1]
    maxHeap=[-1*i for i in stones]
    heapq.heapify(maxHeap)


    while len(maxHeap)>1:
        stone1=heapq.heappop(maxHeap)
        stone2=heapq.heappop(maxHeap)
        if stone1!=stone2:
            heapq.heappush(maxHeap,stone1-stone2)
    if len(maxHeap)==0:
        print(0)
    else:
        print(-1*maxHeap[0])
def kthSmallest(matrix, k):
    grid = [[5,3,7],[8,2,6]]
    limits = [2,2]
    k = 3

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j]=grid[i][j]*-1
    minheap=[]
    ans=[]
    for i in range(len(grid)):
        minheap=grid[i]
        heapq.heapify(minheap)    
        for j in range(limits[i]):
            ans.append(heapq.heappop(minheap))
    print(minheap)
    ans.sort()
    res=0
    for i in range(k):
        res+=(ans[i]*-1)
    print(res)

import heapq

nums1 = [4,2,1,5,3]
nums2 = [10,20,30,40,50]
k = 2

dic={}
n=len(nums1)
answer=[0]*n

index=sorted([(nums1[i],nums2[i],i) for i in range(n)])

print(index)

minheap=[]
sumheap=0
j=0

for val,num2,ind in index:
    print(val,num2,ind)
    
    while j<n and index[j][0]<val:
        heapq.heappush(minheap,index[j][1])
        sumheap+=index[j][1]
        print("BEFORE",minheap,sumheap)
        if len(minheap)>k:
            sumheap-=heapq.heappop(minheap)
        j+=1
        print("AFTER",minheap,sumheap)

    answer[ind]=sumheap
    print("answer",answer)
    print("")
print(answer)
        
        