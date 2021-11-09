def nextMove(n,r,c,grid):
    p = []
    m = [r, c]
    for index, val in enumerate(grid):
        for i in range(n):
            if val[i] == 'p':
                p.append(index)
                p.append(i)

                
    if abs(m[1] - p[1]) > abs(m[0] - p[0]) or m[1] == p[1]:
        return "RIGHT" if m[1] - p[1] < 0 else "LEFT"
    else:
        return "DOWN" if m[0] < p[0] else "UP"
            
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
