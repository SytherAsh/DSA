def countandsay(n):
    n=7

    # if n==1:
    #     print("1")
    # elif n==2:
    #     print("11")
    s="11"
    for i in range(3,n+1):
        s=s+"&"
        t=""
        cnt=1
        for j in range(1,len(s)):
            if s[j]==s[j-1]:
                cnt+=1
            else:
                t+=str(cnt)+s[j-1]
                cnt=1
        s=t
        print(s)
        
# strt=['flow','flower','flight']
def longestCommonPrefix(strt):
    chk=strt[0]
    for i in range(len(strt)):
        # print(strt[i])
        res=''
        j=0
        while j<len(chk) and j<len(strt[i]) and chk[j]==strt[i][j]:
            res+=chk[j]
            j+=1
        chk=res
        # print(res)
    print(chk)
    
def genaratecommonsequence(s,c,i):
    if i==len(s):
        print(c)
        return c
    genaratecommonsequence(s,c+s[i],i+1)
    genaratecommonsequence(s,c,i+1)
# genaratecommonsequence("abc","",0)

strc='aacecaaa'
def LongestPalindromeSubstring(s):
    res=0
    val=''
    for i in range(len(s)):
        l,r=i,i
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
            # res=max(res,r-l-1)
            if r-l-1>res:
                val=s[l+1:r]
                res=r-l-1
                # print(i,val,res,l,r)
        print("ODD")
        print(i,val,res,l,r)    
        l,r=i,i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
            # res=max(res,r-l-1)
            if r-l-1>res:
                val=s[l+1:r]
                res=r-l-1
        print("EVEN")
        print(i,val,res,l,r)
                
    print(val)            
            
        # print(s[l+1:r])
    print(res)
LongestPalindromeSubstring(strc)

#! Longest Common Subsequence
def LCS(s1,s2):
    dp=[[0 for i in range(len(s2)+1) ] for j in range(len(s1)+1)]
    # print(dp)
    
    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            if s1[i]==s2[j]:
                dp[i][j]=1+dp[i+1][j+1]
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j+1])
    print(dp[0][0])
    print(dp)
    return dp[0][0]
# LCS("abcde","ace")
#! Longest Palindrome Subsequence
def LongestpalindromeSubsequence(s):        
    s1=s
    s2=s1[::-1]
    return LCS(s1,s2)

s="letelt"
# x=LongestpalindromeSubsequence(s)
# print(len(s)-x)
