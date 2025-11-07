
arr=[3,2,2]
k=6
def WordWrap(arr,k):
    dp=[(float('inf'))]*(len(arr))
    dp[len(arr)-1]=0

    print(dp)
    for i in range(len(arr)-2,-1,-1):
        w=0
        for j in range(i,len(arr)-1):
            w+=arr[j]
            print("w",w,end=" ")
            if w>k:
                break
            cst=(k-w)*(k-w)
            print("i",i,end=" ")
            print("j",j,end=" ")
            dp[i]=min(dp[i],cst+dp[j+1])
            w+=1
            print("cst",cst)
            print(dp)
        print()
        print()
            
    print(dp[0])

def wordBreak(s,wordDict):
    import heapq,collections
    s="vvvlvp"
    dp={}
    for i in s:
        dp[i]=dp.get(i,0)+1
    maxHeap=[[-freq,char]for char,freq in dp.items()]
    heapq.heapify(maxHeap)

    prev=None
    res=""
    while maxHeap or prev:
        if prev and not maxHeap:
            print("Not possible")
            break
        freq,char=heapq.heappop(maxHeap)
        print(char,freq)
        res+=char
        freq+=1
        if prev:
            heapq.heappush(maxHeap,prev)
            prev=None
        if freq!=0:
            prev=[freq,char]
        print(prev,maxHeap)
        print(res)
        print()
    print(res)

s='ababd'
def minSawpPalindrome(s):
    s=list(s)
    res=0
    while s:
        i=s.index(s[-1])
        if i==len(s)-1:
            res+=i//2
        else:
            res+=i
            s.pop(i)
        s.pop()
    print(res)  

def ShortestPalindrome(s):
    pre=0
    suf=0
    mod=10**9+7
    base=29
    power=1
    lst=0
    s="aaacecaaa"
    for i,c in enumerate(s):
        char=(ord(c)-ord('a')+1)
        
        pre=(pre*base+char)%mod
        suf=(suf+char*power)%mod
        power=(power*base)%mod
        if pre==suf:
            lst=i
    print(s[lst+1:])
    print(s[lst+1:][::-1]+s)