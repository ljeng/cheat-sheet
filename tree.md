## tree

### [tree.**dfs**(*root*, *traversal='inorder'*)](/tree.py)

Returns the preorder, inorder, or postorder traversal of a binary tree `root`.

[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal)
```python
def inorderTraversal(root):
    return [x.val for x in dfs(root)]
```

[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal)
```python
def preorderTraversal(root):
    return [x.val for x in dfs(root, 'preorder')]
```

[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal)
```python
def postorderTraversal(root):
    return [x.val for x in dfs(root, 'postorder')]
```

[Two Sum IV - Input Is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst)
```python
def findTarget(root, k):
    nums = [x.val for x in dfs(root)]
    if len(nums) >= 2:
        enum = dict()
        for i, x in enumerate(nums):
            if x in enum:
                return True
            else:
                enum[k - x] = i
    return False
```

[All Elements in Two Binary Search Trees](https://leetcode.com/problems/all-elements-in-two-binary-search-trees)
```python
import itertools


def getAllElements(root1, root2):
    reverse_inorder = lambda x: [y.val for y in dfs(x)][::-1]
    lists = [[], reverse_inorder(root1), reverse_inorder(root2)]
    while lists[1] and lists[2]:
        lists[0] += [sorted(lists[1:], key = lambda z: z[-1])[0].pop()]
    return itertools.chain(*lists)
```

### [tree.**memoize**(*root*, *base*, *function*)](/tree.py)

Applies a `function(x, L, R)` to a tree binary tree node `root` where `x` is the root, `L` is the output of `function` applied to `root.left`', and `R` is the output of `function` applied to `root.right`. Sets the base case to `function(x = None) = base`.

[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree)
```python
def maxDepth(root):
    return memoize(root, 0, lambda x, L, R: max(L, R) + 1)
```

[Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree)
```python
def isBalanced(root):
    depth = memoize(root, 0, lambda x, L, R: max(L, R) + 1, True)
    return memoize(root, True,
        lambda x, L, R: all([abs(depth[x.left] - depth[x.right]) <= 1, L, R])
    )
```

[Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree)
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

[Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers)
```python
def sumNumbers(root):
    return memoize(root, 0, lambda x, L, R: x.val + (L + R)*10)
```

[Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths)
```python
def binaryTreePaths(root):
    concatenate = lambda x, value: [str(x.val) + '->' + y for y in value]
    return memoize(root, [],
        lambda x, L, R: [str(x.val)]
            if x.left == x.right == None
            else concatenate(x, L) + concatenate(x, R)
    )
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
            if x.left.left == x.left.right == None:
                s += x.left.val
            else:
                s += L
        return s

    return memoize(root, 0, function)
```

[Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum)
```python
import statistics


def findFrequentTreeSum(root):
    subtree_sum = memoize(root, 0, lambda x, L, R: x.val + L + R, True)
    del subtree_sum[None]
    return statistics.multimode(subtree_sum.values())
```

[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree)
```python
def diameterOfBinaryTree(root):
    depth = memoize(root, 0, lambda x, L, R: max(L, R) + 1, True)
    return memoize(root, 0,
        lambda x, L, R: max(depth[x.left] + depth[x.right], L, R)
    )
```

[Binary Tree Tilt](https://leetcode.com/problems/binary-tree-tilt)
```python
def findTilt(root):
    subtree_sum = memoize(root, 0, lambda x, L, R: x.val + L + R, True)
    return memoize(root, 0,
        lambda x, L, R: abs(subtree_sum[x.left] - subtree_sum[x.right]) + L + R
    )
```

[Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree)
```python
def tree2str(t):

    def function(x, L, R):
        s = str(x.val)
        if x.left:
            s += parenthesize(L)
            if x.right:
                s += parenthesize(R)
        elif x.right:
            s += '()' + parenthesize(R)
        return s

    parenthesize = lambda y: '(' + y + ')'
    return memoize(t, '()', function) if t else ''
```

[Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree)
```python
def trimBST(root, L, R):

    def function(x, _L, _R):
        if x.val < L:
            return _R
        elif x.val > R:
            return _L
        x.left, x.right = _L, _R
        return x

    return memoize(root, None, function)
```

[Second Minimum Node in a Binary Tree](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree)
```python
def findSecondMinimumValue(root):

    def function(x, L, R):
        if x.left == x.right == None:
            return -1
        a = x.left.val if x.left.val != x.val else L
        b = x.right.val if x.right.val != x.val else R
        if min(a, b) > -1:
            return min(a, b)
        elif a > -1:
            return a
        else:
            return b

    return memoize(root, -1, function)
```

[Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path)
```python
def longestUnivaluePath(root):

    def function(root, L, R):
        left_same = is_same(root, root.left)
        right_same = is_same(root, root.right)
        return max((L + R + 2)*left_same*right_same,
            (L + 1)*left_same, (R + 1)*right_same, L, R
        )

    is_same = lambda parent, child: bool(child and child.val == parent.val)
    return memoize(root, 0, function)
```

[Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning)
```python
def pruneTree(root):

    def function(x, L, R):
        x.left, x.right = L, R
        return None if x.val == 0 and x.left == x.right == None else x

    return memoize(root, None, function)
```

[Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes)
```python
def subtreeWithAllDeepest(root):

    def function(x, L, R):
        if L[0] > R[0]:
            return L[0] + 1, L[1]
        elif L[0] < R[0]:
            return R[0] + 1, R[1]
        else:
            return L[0] + 1, x

    return memoize(root, (0, None), function)[1]
```

[Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst)
```python
def rangeSumBST(root, L, R):

    def function(x, _L, _R):
        if x.val < L:
            return _R
        elif x.val > R:
            return _L
        else:
            return x.val + _L + _R

    return memoize(root, 0, function)
```

[Univalued Binary Tree](https://leetcode.com/problems/univalued-binary-tree)
```python
def isUnivalTree(root):
    return memoize(root, True, lambda x, L, R: all([x.val == root.val, L, R]))
```

[Lowest Common Ancestor of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves)
```python
def lcaDeepestLeaves(root):

    def function(x, L, R):
        if L[0] > R[0]:
            return L[0] + 1, L[1]
        elif L[0] < R[0]:
            return R[0] + 1, R[1]
        else:
            return L[0] + 1, x

    return memoize(root, (0, None), function)[1]
```

```python
def sumEvenGrandparent(root):

    def sum_grandchildren(x, L, R):
        s = 0
        if x.left:
            if x.left.left:
                s += x.left.left.val
            if x.left.right:
                s += x.left.right.val
        if x.right:
            if x.right.left:
                s += x.right.left.val
            if x.right.right:
                s += x.right.right.val
        return s
        
    sum_memo = memoize(root, None, sum_grandchildren, True)
    del sum_memo[None]
    return sum(sum_memo[y] for y in sum_memo if y.val%2 == 0)
```

```python
def removeLeafNodes(root):

    def function(x, L, R):
        if x.left:
            x.left = L
        if x.right:
            x.right = R
        return None if x.left == x.right and x.val == target else x

    return memoize(root, None, function)
```

[Maximum Product of Splitted Binary Tree](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree)
```python
def maxProduct(root):
    subtree_sum = memoize(root, 0, lambda x, L, R: x.val + L + R, True)
    return max((y*(subtree_sum[root] - y))
        for y in subtree_sum.values()
    ) % (10**9 + 7)
```

```python
def longestZigZag(root):
    return memoize(root, (-1, -1, -1),
        lambda x, L, R: (L[1] + 1,
            R[0] + 1,
            max(L[1] + 1, R[0] + 1, L[2], R[2])
        )
    )[2]
```
### [tree.**level_order**(*root*)](/tree.py)

Returns the level-order traversal of a binary tree `root`, row by row.

[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal)
```python
def levelOrder(root):
    return [[y.val for y in x] for x in level_order(root)]
```

[Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal)
```python
def zigzagLevelOrder(root):
    visited = [[y.val for y in x] for x in level_order(root)]
    for i in range(1, len(visited), 2):
        visited[i].reverse()
    return visited
```

[Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii)
```python
def levelOrderBottom(root):
    [[y.val for y in x] for x in level_order(root)[::-1]]
```

[Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view)
```python
def rightSideView(root):
    return [x[-1].val for x in level_order(root)]
```

[Find Bottom Left Tree Value](https://leetcode.com/problems/find-bottom-left-tree-value)
```python
def findBottomLeftValue(root):
    return level_order(root)[-1][0].val
```

[Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row)
```python
def largestValues(root):
    return [max(y.val for y in x) for x in level_order(root)]
```

[Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree)
```python
import statistics


def averageOfLevels(root):
    return [statistics.mean(y.val for y in x) for x in level_order(root)]
```

[Deepest Leaves Sum](https://leetcode.com/problems/deepest-leaves-sum)
```python
def deepestLeavesSum(root):
    return sum(x.val for x in level_order(root)[-1])
```