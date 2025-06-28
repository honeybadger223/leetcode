# This is the general solution for LeetCode problem 199: Binary Tree Right Side View.

# Using DFS
def rightSideView(root):
    res = []
    def dfs(node, level):
        if not node:
            return
        if level == len(res):
            res.append(node.val)
        dfs(node.right, level + 1)
        dfs(node.left, level + 1)
    dfs(root, 0)
    return res

# Return the values of the node you can see, first form teh left side of the tree.
# Then, from the right side of the tree.
# Using BFS
from collections import deque
def rightSideViewBFS(root):
    # if the tree is empty...
    if not root:
        return []
    # left and right most lists
    left_view = []
    right_view = []
    queue = deque([root])
    while queue:
        # get the size of the current level
        level_size = len(queue)
        # store values at this level...
        level = []
        for i in range(level_size):
            # pop from queue and save
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        left_view.append(level[0])  # first element is the leftmost
        right_view.append(level[-1])  # last element is the rightmost
    left_part = left_view[::-1]  # reverse the left view
    if left_part[-1] == right_view[0]:
        right_part = right_view[1:]  # skip the first element if it's the same as the last of left view
    else:
        right_part = right_view
    return left_part + right_part
    # or print for meta variant
    for val in left_part + right_part:
        print(val, end=' ')
    