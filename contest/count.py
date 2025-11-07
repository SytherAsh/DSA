# def cntCoveredBuildings(n, buildings):
#     row_min = {}
#     row_max = {}
#     col_min = {}
#     col_max = {}

#     for row, col in buildings:
#         if row not in row_min:
#             row_min[row] = row_max[row] = col
#         else:
#             if col < row_min[row]:
#                 row_min[row] = col
#             if col > row_max[row]:
#                 row_max[row] = col

#         if col not in col_min:
#             col_min[col] = col_max[col] = row
#         else:
#             if row < col_min[col]:
#                 col_min[col] = row
#             if row > col_max[col]:
#                 col_max[col] = row

#     cnt = 0
#     for row, col in buildings:
#         if row_min[row] < col < row_max[row] and col_min[col] < row < col_max[col]:
#             cnt += 1

#     return cnt
def connected_queries(n, values, max_diff, queries):
    cnt = [0] * n
    label = 0
    for i in range(1, n):
        if values[i] - values[i-1] > max_diff:
            label += 1
        cnt[i] = label

    return [cnt[u] == cnt[v] for u, v in queries]