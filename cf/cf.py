# t = int(input())

# for _ in range(t):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))

#     x = None
#     ok = True
#     for ai, bi in zip(a, b):
#         if bi != -1:
#             s = ai + bi
#             if x is None:
#                 x = s
#             elif x != s:
#                 ok = False
#                 break

#     if not ok:
#         print(0)
#         continue

#     if x is not None:
#         for ai, bi in zip(a, b):
#             if bi == -1:
#                 res = x - ai
#                 if res < 0 or res > k:
#                     ok = False
#                     break
#         print(1 if ok else 0)

 
#     else:
#         left = max(a)
#         right = min(ai + k for ai in a)
#         if left > right:
#             print(0)
#         else:
#             print(right - left + 1)


def can(a, b, k):
    n, m = len(a), len(b)
    j0 = j1 = 0
    INF = n + 1
    for bi in b:
        o1, o2 = j0, j1
        new = INF
        if k >= bi:
            new = o1
        while o2 < n and a[o2] < bi:
            o2 += 1
        if o2 < n:
            new = min(new, o2 + 1)
        j1 = new

        while o1 < n and a[o1] < bi:
            o1 += 1
        j0 = o1 + 1 if o1 < n else INF

        if j0 > n and j1 > n:
            return False

    return (j0 <= n) or (j1 <= n)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if can(a, b, 0):
        print(0)
        continue

    vals = sorted(set(b))
    lo, hi = 0, len(vals) - 1
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if can(a, b, vals[mid]):
            ans = vals[mid]
            hi = mid - 1
        else:
            lo = mid + 1

    print(ans)
