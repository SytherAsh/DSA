arr=[12,32,3,123,43,2]

#! SELECTION SORT
# for i in range(len(arr)):
#     mn=i
#     for j in range(i,len(arr)):
#         if arr[j]<arr[mn]:
#             mn=j
#     # print(mn)
#     arr[mn],arr[i]=arr[i],arr[mn]

#! BUBBLE SORT
# for i in range(len(arr)-1):
#     for j in range(len(arr)-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr)


#! INSERTION SORT 
# for i in range(len(arr)):
#     j=i
#     while (j>0 and arr[j-1]>arr[j]):
#         arr[j],arr[j-1]=arr[j-1],arr[j]
#         j-=1
# print(arr)

# #! MERGE SORT 
# def Merge(arr,l,mid,r):
#     left,right=arr[l:mid+1],arr[mid+1:r+1]
#     i,j,k=0,0,l

#     while (i<len(left) and j<len(right)):
#         if left[i]<=right[j]:
#             arr[k]=left[i]
#             i+=1
#         else:
#             arr[k]=right[j]
#             j+=1
#         k+=1
#     while i<len(left):
#         arr[k]=left[i]
#         i+=1
#         k+=1
#     while j<len(right):
#         j+=1
#         k+=1

# def MergeSort(arr,l,h):
#     if l==h:
#         return arr
#     mid=l+(h-l)//2
#     MergeSort(arr,l,mid)
#     MergeSort(arr,mid+1,h)
#     Merge(arr,l,mid,h)
# MergeSort(arr,0,len(arr))
# print(arr)

#!QUICK SORT
def partIndex(arr,l,h):
    pivot=arr[l]
    i=l
    j=h

    while i<j:
        while (arr[i]<=pivot and i<=h-1):
            i+=1
        while (arr[j]>pivot and j>=l+1):
            j-=1
        if (i<j):
            arr[j],arr[i]=arr[i],arr[j]

    # print(arr,l,j)
    arr[l],arr[j]=arr[j],arr[l]
    print(arr)

    return j

def QuickSort(arr,l,h):
    if(l<h):
        pi=partIndex(arr,l,h)
        QuickSort(arr,l,pi-1)
        QuickSort(arr,pi+1,h)
# arr=[4,6,2,5,7,9,1,3]
print(arr)
QuickSort(arr,0,len(arr)-1)
print(arr)