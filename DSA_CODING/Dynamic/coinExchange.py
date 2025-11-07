def coin(i,amt,arr,dp):
    if amt ==0:
        return 1
    if i<0 or amt<0:
        return 0
    if (i,amt) in dp:
        return dp[(i,amt)]
    notake=coin(i-1,amt,arr,dp)
    take=0
    if amt>=arr[i]:
        take=coin(i,amt-arr[i],arr,dp)
    dp[(i,amt)]=take+notake
    # print(f"i: {i}, amt: {amt}, take: {take}, notake: {notake}, dp: {dp}")
    return dp[(i,amt)]

arr=[1,2,3]
amt=4
print(coin(len(arr)-1,amt,arr,{}))