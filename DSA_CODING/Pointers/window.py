# arr=[1,2,4,5]
# # arr=[1,2,3,4,5,6,7]
# # arr=[64,69,7,78,31,83,47,84,47,6,67]

# ans=[0]*len(arr)
# cnt=0
# for i in range(len(arr)):
#     if arr[i]%2 == 1:
#         cnt+=1
#     ans[i]=cnt
# # print(ans)

# flg=0
# ctr=0
# for i in range(len(ans)):
#     for j in range(i,len(ans)):
#         # print(ans[j]-flg)
#         if (ans[j]-flg)%2==1:
#             ctr+=1
#             # print(ans[i],ans[j],ctr)
#     print(flg)
#     print(arr[i],arr[i-1])
#     if i==0 and ans[i]%2==1:
#             flg+=1
#     if (i>0 and ans[i]!=ans[i-1]):
#             flg+=1
# print(ctr)

from collections import defaultdict
word="fdaeioudmsl"
k=2
def attack(k):
    vowel=defaultdict(int)
    non=0
    res=0
    l=0
    for i in range(len(word)):
        if word[i] in 'aeiou':
            vowel[word[i]]+=1
        else:
            non+=1
        while len(vowel)==5 and non>=k:
            res+=(len(word)-i)
            print(i,l,res)
            if word[l] in 'aeiou':
                vowel[word[l]]-=1
            else:
                non-=1
            if vowel[word[l]]==0:
                vowel.pop(word[l])
            l+=1
            print(vowel,non)
    return res
print( attack(k)-attack(k+1))
    
    