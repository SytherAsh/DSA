# nums=[1,4,3,3,1]
# nums=[10,9,8,7,6,5,4,3,3,2,1]
# nums=[1,5,2,7]
# dp=[[0,0]]*len(nums)
# dp[0]=[1,1]
# ans=0
# for i in range(1,len(nums)):
#     if nums[i-1]<nums[i]:
#         dp[i]=[dp[i-1][0]+1,1]
#     elif nums[i-1]>nums[i]:
#         dp[i]=[1,dp[i-1][1]+1]
#     else:
#         dp[i]=[1,1]
#     ans=max(ans,dp[i][0],dp[i][1])
#     print(dp,ans)
# # return ans
# print(ans)


nums = [0,0]
k = 2
from collections import defaultdict

def largestAlmostMissing(nums, k):
    freq = defaultdict(int)  # Dictionary to track frequency of numbers in subarrays

    # Sliding window approach
    for i in range(len(nums) - k + 1):
        subarray = nums[i:i + k]
        print(subarray)
        # unique_values = set(subarray)  # Get unique values in the subarray
        # print(unique_values)
        for val in subarray:
            freq[val] += 1  # Increase count in frequency dictionary
        print(freq)
    # Find the largest number that appears in exactly one subarray
    result = -1
    for num, count in freq.items():
        if count == 1:
            result = max(result, num)
    
    return result
# x=largestAlmostMissing(nums, k)
# print(x)
dic={}
for i in range(4):
    dic[i]=i+10
print(dic)
for i in range(4):
    if i in dic:
        print(dic[i])
        
def maxVowels(s, k):      
    s="weallloveyou"
    k=7
    vowel=('a','e','i','o','u')
    cnt=0
    for i in range(len(s)-k):
        window=s[i:i+k]
        val=0
        for j in range(k):
            if window[j] in vowel:
                val+=1
        cnt=max(cnt,val)
        print(window,val)
    print(cnt)
    

def maxScore(cardPoints, k):
    n = len(cardPoints)
    total = sum(cardPoints)  # Total sum of all elements

    if k == n:  # If we can take all cards, return total sum
        return total

    # Compute the sum of the 'n-k' middle section (window to be removed)
    window_sum = sum(cardPoints[:n-k])  # Initial window sum
    min_window = window_sum  # Track min sum of window to remove

    # Slide the window to find the minimum sum of 'n-k' elements
    for i in range(n-k, n):
        window_sum += cardPoints[i] - cardPoints[i-(n-k)]
        min_window = min(min_window, window_sum)

    return total - min_window  # Max points = Total - Min removable window sum

# Example Usage
cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
print(maxScore(cardPoints, k))  # Output: 12


