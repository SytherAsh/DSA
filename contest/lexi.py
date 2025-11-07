def smallest_divisible_permutation(nums, k):
    n = len(nums)
    dc = []
    tm = []
    for num in nums:
        length = len(str(num))
        dc.append(length)
        md = 1
        for _ in range(length):
            md = (md * 10) % k
        tm.append(md)

    msk = (1 << n) - 1
    reach = [[False] * k for _ in range(1 << n)]
    for r in range(k):
        reach[msk][r] = (r == 0)

    for mask in range(msk - 1, -1, -1):
        for rem in range(k):
            for idx in range(n):
                bit = 1 << idx
                if mask & bit:
                    continue
                new_rem = (rem * tm[idx] + nums[idx]) % k
                if reach[mask | bit][new_rem]:
                    reach[mask][rem] = True
                    break

    if not reach[0][0]:
        return []

    order = [(nums[i], i) for i in range(n)]
    order.sort()

    result = []
    mask = 0
    rem = 0
    for _ in range(n):
        for value, idx in order:
            bit = 1 << idx
            if mask & bit:
                continue
            new_rem = (rem * tm[idx] + value) % k
            if reach[mask | bit][new_rem]:
                result.append(value)
                mask |= bit
                rem = new_rem
                break

    return result


# example runs
print(smallest_divisible_permutation([3, 12, 45], 5))  # [3, 12, 45]
print(smallest_divisible_permutation([10, 5], 10))     # [5, 10]
print(smallest_divisible_permutation([1, 2, 3], 5))    # []
