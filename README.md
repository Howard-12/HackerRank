# HackerRank

## [Artificial Intelligence](./Artificial%20Intelligence)
#### [Bot saves princess](./Artificial%20Intelligence/Bot%20saves%20princess.py)

```python
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
```
#### [Bot saves princess - 2](./Artificial%20Intelligence/Bot%20saves%20princess%20-%202.py)

```python
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
```
