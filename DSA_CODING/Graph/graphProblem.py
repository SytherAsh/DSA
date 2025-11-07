def island():
    def dfs(grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0:
            return 0
        grid[i][j]=0
        cnt=1+dfs(grid,i+1,j)+dfs(grid,i-1,j)+dfs(grid,i,j+1)+dfs(grid,i,j-1)
        return cnt

    grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    count=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j])
            if grid[i][j]==1:
                count=max(count,dfs(grid,i,j))
                print(count)
    print(count)

recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]

can_cook={s:True for s in supplies}
recipe_ind={r:i for i,r in enumerate(recipes)}
def dsf(r):
    if r in can_cook:
        return can_cook[r]
    if r not in recipe_ind:
        return False

    for i in ingredients[recipe_ind[r]]:
        if not dsf(i):
            return False
    can_cook[r]=True
    return can_cook[r]
r=[]
print([r for r in recipes if dsf(r)])

