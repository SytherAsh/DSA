def twopointer():
    nums =[0,0,66,1314]
    # nums=[-925,-170,-5,728,795,810,821,919,1776,1861]
    # nums = [1,2,2,2,2,2,3]
    # nums=[-2,-1,-1]


    f,e=nums[0],nums[-1]

    # if f>0:
    #     print(len(nums)) 
    # if e<0:
    #     print(len(nums))
    # if f==0 and e==0:
    #     print(0)
        

    l,r=0,len(nums)-1
    neg,pos=0,0
    while l<r:
        mid=l+(r-l)//2
        # print(l,r,mi
    #     print(len(nums)) 
    # if e<0:
    #     print(len(nums))
    # if f==0 and e==0:
    #     print(0)d)
        if nums[mid]<0 and nums[mid+1]>0:
            neg=mid+1
            break
        elif nums[mid]>=0 and nums[mid+1]>=0:
            r=mid
        else:
            l=mid+1

    print(neg)

    l,r=0,len(nums)-1
    while l<r:
        mid=l+(r-l)//2
        print(mid,l,r)
        if nums[mid-1]<=0 and nums[mid]>0:
            pos=len(nums)-mid
            break
        elif nums[mid-1]>0 and nums[mid]>0:
            r=mid-1
        else:
            l=mid
        print(l,r)
    print(pos)
    
    
