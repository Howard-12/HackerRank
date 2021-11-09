# HackerRank

## Artificial Intelligence
- [Bot saves princess](Artificial Intelligence)

```python
def displayPathtoPrincess(n,grid):
    p = []
    m = []
    for index, val in enumerate(grid):
        for i in range(n):
            if val[i] == 'p':
                p.append(index)
                p.append(i)
            elif val[i] == 'm':
                m.append(index)
                m.append(i)

    route = []
    while m[0] - p[0] != 0:
        if m[0] - p[0] < 0:
            m[0], m[1] = m[0] + 1, m[1]
            print("DOWN")
        elif m[0] - p[0] > 0:
            m[0], m[1] = m[0] - 1, m[1]
            print("UP")

    while m[1] - p[1] != 0:
        if m[1] - p[1] < 0:
            m[0], m[1] = m[0], m[1] + 1
            print("RIGHT")
        elif m[1] - p[1] > 0:
            m[0], m[1] = m[0], m[1] - 1
            print("LEFT")


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)

```
