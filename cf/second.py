# # import heapq

# # t = int(input())

# # for _ in range(t):
# #     n = int(input())
# #     arr = list(map(int, input().split()))

# #     pq = []
# #     for i, w in enumerate(arr):
# #         heapq.heappush(pq, (w, i))

# #     done = [False] * n
# #     ans = 0

# #     while pq:
# #         w, idx = heapq.heappop(pq)
# #         lft = (idx > 0 and done[idx - 1])
# #         rgt = (idx < n - 1 and done[idx + 1])

# #         if not lft and not rgt:
# #             ans += 1

# #         done[idx] = True

# #     print(ans)
# fst,sec=0,0
# n=124

# while n>0:
#     val=n%10
#     if val>=fst:
#         temp=fst
#         fst=val
#         sec=temp
#     elif val>sec and val!=fst:
#         sec=val
#     n=n//10
#     print(sec,fst)

# def splgrid(N):
#     if N == 0:
#         return [[0]]
#     prev = splgrid(N - 1)
#     hlf = 2 ** (N - 1)
#     sz = hlf * 2
#     qsz = hlf * hlf

#     grid = [[0] * sz for _ in range(sz)]

#     for i in range(hlf):
#         for j in range(hlf):
#             val = prev[i][j]
#             grid[i][j + hlf] = val
#             grid[i + hlf][j + hlf] = val + qsz
#             grid[i + hlf][j] = val + 2 * qsz
#             grid[i][j] = val + 3 * qsz

#     return grid

# # Example usage:
# if __name__ == "__main__":
#     for N in range(4):
#         g = splgrid(N)
#         print(f"N = {N}")
#         for row in g:
#             print(row)
#         print()
