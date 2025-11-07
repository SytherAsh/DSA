from typing import List

class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        quendravil = nums  # per problem instruction

        def can_partition(maxor):
            cnt = 0
            curr = 0
            for num in nums:
                curr ^= num
                if curr > maxor:
                    cnt += 1
                    curr = num  
                    if curr > maxor:
                        return False  
            return cnt + 1 <= k

        l, r = 0, 0
        for num in nums:
            r ^= num  

        ans = r
        while l <= r:
            mid = (l + r) // 2
            if can_partition(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans

# Example usage:
sol = Solution()
print(sol.minXor([2,3,3,2], 2))  # Output: 1

from typing import List

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def check(s1, s2):
            i = 0
            while i < min(len(s1), len(s2)) and s1[i] == s2[i]:
                i += 1
            return i

        n = len(words)
        if n == 1:
            return [0]

        lcp = [check(words[i], words[i + 1]) for i in range(n - 1)]

        prefix_max = [0] * (n - 1)
        suffix_max = [0] * (n - 1)

        prefix_max[0] = lcp[0]
        for i in range(1, n - 1):
            prefix_max[i] = max(prefix_max[i - 1], lcp[i])

        suffix_max[-1] = lcp[-1]
        for i in range(n - 3, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], lcp[i])

        ans = []
        for i in range(n):
            curr_max = 0
            if i >= 2:
                curr_max = max(curr_max, prefix_max[i - 2])
            if i <= n - 3:
                curr_max = max(curr_max, suffix_max[i + 1])
            if 0 < i < n - 1:
                curr_max = max(curr_max, check(words[i - 1], words[i + 1]))
            ans.append(curr_max)

        return ans
