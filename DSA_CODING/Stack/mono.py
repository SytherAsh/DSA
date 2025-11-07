arr=[1,4,6,3,2,7]
arr=[4,3,2,5,2,5,1,53,14,54]

ans=[0]*len(arr)
stack = []
cnt=0
for i in range(len(arr)):
    if not stack or arr[i]> stack[-1]:
        stack.append(arr[i])    
        for j in range(cnt,i+1):    
            ans[j]= arr[i]
            cnt+=1
    print(stack, ans, cnt)
       