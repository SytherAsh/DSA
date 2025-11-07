cardPoints=[1,2,3,4,5,6,1]





k=3
cache={}
def cal(l,r,cnt):
    if cnt>=k:
        return 0
    if (l,r) in cache:
        return cache[(l,r)]

    left=cardPoints[l]+cal(l+1,r,cnt+1)
    print("left",left,l,r)
    right=cardPoints[r]+cal(l,r-1,cnt+1)
    print("right",right,l,r)
    cache[(l,r)]=max(left,right)
    print("cache",cache)

    return max(left,right)
print(cal(0,len(cardPoints)-1,0))