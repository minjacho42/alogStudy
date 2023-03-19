N, M = map(int, input().split())

trees = list(map(int, input().split()))

max_height = max(trees)
height = max_height - M
min_height = height
timber_function = lambda h: sum([0 if tree < height else tree-height for tree in trees])
timber = timber_function(height)
before_height = max_height
while timber != M and before_height != height:
    if timber > M:
        min_height = height
        before_height, height = height, (height + max_height) // 2
    else:
        max_height = height
        before_height, height = height, (height + min_height) // 2
    timber = timber_function(height)
print(height)