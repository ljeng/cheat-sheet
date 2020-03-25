## tree

[tree.**dfs**(*root*, *traversal*)](/tree.py)

Returns the preorder, inorder, or postorder traversal of a binary tree `root`.

Examples:

[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
```python
def inorderTraversal(root):
    return [x.val for x in dfs(root, 'inorder')]
```

[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
```python
def preorderTraversal(root):
    return [x.val for x in dfs(root, 'preorder')]
```

[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
```python
def postorderTraversal(root):
    return [x.val for x in dfs(root, 'postorder')]
```

[Two Sum IV - Input Is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst)
```python
def findTarget(root, k):
    nums = [x.val for x in dfs(root, 'inorder')]
    if len(nums) >= 2:
        enum = dict()
        for i, x in enumerate(nums):
            if x in enum: return True
            else: enum[k - x] = i
    return False
```

[tree.**memoize**(*root*, *none_val*, *function*)](/tree.py)

Applies a `function(x, L, R)` to a tree binary tree node `root` where `x` is the root, `L` is the output of `function` applied to `root.left`, and `R` is the output of `function` applied to `root.right`. If `root` is `None`, returns `none_val`.

Examples:

[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree)
```python
def maxDepth(root):
    return memoize(root, 0, lambda x, L, R: max(L, R) + 1)
```

[Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
```python
def minDepth(root):
    return memoize(root, 0, lambda x, L, R: (L or R) + 1)
```

[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum)
```python
def maxPathSum(root):
    return max(memoize(root, [-float('inf'), -float('inf')],
        lambda x, L, R: [x.val + max(L[0], R[0], 0),
            max(L + R + [x.val + L[0] + R[0]])
        ])
    )
```

[Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/)
```python
def sumNumbers(root):
    return memoize(root, 0, lambda x, L, R: (L + R)*10 + x.val)
```

[House Robber III](https://leetcode.com/problems/house-robber-iii)
```python
def rob(root):
    return max(memoize(root, (0, 0),
        lambda x, L, R: (L[1] + R[1] + x.val, max(L) + max(R))
    ))
```

[Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves)
```python
def sumOfLeftLeaves(root):

    def function(x, L, R):
        s = R
        if x.left:
            if x.left.left == x.left.right == None: s += x.left.val
            else: s += L
        return s

    return memoize(root, 0, function)
```

[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
Recursive:
```python
def diameterOfBinaryTree(root):
    def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            depth[root] = max(depth[root.left], depth[root.right]) + 1
    depth = {None: 0}
    postorder(root)
    return memoize(root, 0,
        lambda x, L, R: max(depth[x.left] + depth[x.right], L, R)
    )
```

Iterative:
```python
def diameterOfBinaryTree(root):
    stack, depth = [], {None: 0}
    if root: stack += [root]
    while stack:
        if stack[-1].left: stack += [stack[-1].left]
        elif stack[-1].right: stack += [stack[-1].right]
        else:
            while stack:
                current = stack.pop()
                depth[current] = max(depth[current.left],
                    depth[current.right]
                ) + 1
                if stack and stack[-1].left is current and stack[-1].right:
                    stack += [stack[-1].right]
                    break
    return memoize(root, 0,
        lambda x, L, R: max(depth[x.left] + depth[x.right], L, R)
    )
```

```python
def trimBST(root, L, R):

    def function(x, _L, _R):
        if x.val < L: return _R
        elif x.val > R: return _L
        x.left, x.right = _L, _R
        return x

    return memoize(root, None, function)
```

```python
def findSecondMinimumValue(root):

    def function(x, L, R):
        if x.left == x.right == None: return -1
        a = x.left.val if x.left.val != x.val else L
        b = x.right.val if x.right.val != x.val else R
        if min(a, b) > -1: return min(a, b)
        elif a > -1: return a
        else: return b

    return memoize(root, -1, function)
```

[tree.**level_order**(*root*)](/tree.py)

Returns the level-order traversal of a binary tree `root`, row by row.

[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
```python
def levelOrder(root):
    return [[y.val for y in x] for x in level_order(root)]
```

[Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
```python
def zigzagLevelOrder(root):
    visited = [[y.val for y in x] for x in level_order(root)]
    for i in range(1, len(visited), 2): visited[i].reverse()
    return visited
```

[Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
```python
def levelOrderBottom(root):
    [[y.val for y in x] for x in level_order(root)[::-1]]
```

[Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view)
```python
def rightSideView(root):
    return [x[-1].val for x in level_order(root)]
```

[Find Bottom Left Tree Value](https://leetcode.com/problems/find-bottom-left-tree-value/)
```python
def findBottomLeftValue(root):
    return level_order(root)[-1][0].val
```

[Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)
```python
def largestValues(root):
    return [max(y.val for y in x) for x in level_order(root)]
```

[Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/)
```python
import statistics


def averageOfLevels(root):
    return [statistics.mean(y.val for y in x) for x in level_order(root)]
```