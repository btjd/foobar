from itertools import permutations

def answer(food, grid):
    N = len(grid)
    paths = 2*N-2
    NR = 'R'*(paths/2) # Basically N-1
    ND = 'D'*(paths/2)
    sequences = set(permutations(ND+NR))
    
    outcomes = []
    
    for s in sequences:
        x = 0
        y = 0
        count = 0
        for i in s:
            if i == 'R':
                count += grid[x][y+1]
                y += 1
            elif i == 'D':
                count += grid[x+1][y]
                x += 1
        outcomes.append(count)
        # print outcomes
        
    ans = max([o for o in outcomes if 0 < o <=food])
    
    if ans: return food - ans
    else: return -1
        
        
# #expect1
grid = [[0,2], [3,1]]
food = 5
# 
# expect 0
# grid = [[0, 1, 1], [1, 1, 1], [1, 1, 1]]
# food = 4
# 
# #expect 0
# grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
# food = 7
# 
# #expect 1
# grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
# food = 12
# 
#expect 0
# grid = [[0, 7, 4, 3], [3, 5, 5, 3], [5, 2, 7, 9], [1, 9, 8, 4]]
# food = 30


print answer(food, grid)