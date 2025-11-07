
def ninja(arr,day,last,dp):
    if day==0:
        maxi=0
        print("1st day",day, "last", last)
        for i in range(3):
            if (i!=last):
                maxi=max(maxi,arr[day][i])
        print("maxi", maxi)
        return maxi
    if dp[day][last]!=-1:
        return dp[day][last]
    maxi=0
    for task in range(3):
        if task!=last:
            print("day", day, "task", task, "last", last, "arr[day][task]", arr[day][task])
            maxi=max(maxi,arr[day][task]+ninja(arr,day-1,task,dp))
        dp[day][last]=maxi
    print(dp)
    return dp[day][last]

arr=[[1,2,5],[3,1,1],[3,3,3]]
dp=[[-1]*4 for i in range(len(arr))]
print(ninja(arr,len(arr)-1,3,dp))