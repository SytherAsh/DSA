
def helper(nums):
    rob1,rob2=0,0
    for n in range(len(nums)-1):
        temp=max(nums[n]+rob1,rob2)
        rob1=rob2
        rob2=temp 
    return rob2
def house_robber(nums):
    if len(nums)==1:
        return nums[0]
    m1=helper(nums[1:])
    m2=helper(nums[:-1])
    return max(m1,m2)
nums=[2,3,2]
# print(house_robber(nums))


def frog(arr,k):
    # if len(arr)==1:
    #     return 0
    
    # one,two=0,abs(arr[1]-arr[0])
    # print(one,two)
    # for i in range(2,len(arr)):
    #     temp=min(abs(arr[i]-arr[i-1])+two,abs(arr[i]-arr[i-2])+one )
    #     one=two
    #     two=temp
    #     print(two)
    # return two
    dp=[float('inf')]*len(arr)
    dp[0]=0
    for r in range(1,len(arr)):
        for l in range(1,k+1):
            if r-l>=0:
                dp[r]=min(dp[r],dp[r-l]+abs(arr[r]-arr[r-l]))
    return dp[-1]

print(frog([10, 30, 40, 20, 5],2))
print(frog([2,1,3,5,4],1))