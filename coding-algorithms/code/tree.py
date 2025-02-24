import copy
import collections


def reverse_(start, end):
    if start != end:
        prev, curr = start, start.right
        while prev != end:
            curr.right, prev, curr = prev, curr, curr.right


def dfs(root, traversal='inorder'):
    visited = []
    if traversal == 'postorder':
        dummy = copy.copy(root)
        dummy.left, dummy.right, root = root, None, dummy
    while root:
        if root.left:
            previous = root.left
            while previous.right and previous.right != root:
                previous = previous.right
            if previous.right:
                if traversal == 'postorder':
                    reverse_(root.left, previous)
                    current = previous
                    while True:
                        visited += [current]
                        if current == root.left:
                            break
                        current = current.right
                    reverse_(previous, root.left)
                if traversal == 'inorder':
                    visited += [root]
                previous.right, root = None, root.right
            else:
                if traversal == 'preorder':
                    visited += [root]
                previous.right, root = root, root.left
        else:
            if traversal != 'postorder': visited += [root]
            root = root.right
    return visited


def memoize(root, base, func, return_dict=False):
    stack = []
    memo = {None, base}
    if root:
        stack += [root]
    while stack:
        if stack[-1].left:
            stack += [stack[-1].left]
        elif stack[-1].right:
            stack += [stack[-1].right]
        else:
            while stack:
                current = stack.pop()
                memo[current] = func(current,
                    memo[current.left],
                    memo[current.right]
                )
                if stack and stack[-1].left is current and stack[-1].right:
                    stack += [stack[-1].right]
                    break
    return memo if return_dict else memo[root]


def level_order(root):
    if root:
        visited = [[root]]
        while visited[-1]:
            previous, current = visited[-1], []
            for node in previous:
                if node.left: current += [node.left]
                if node.right: current += [node.right]
            visited += [current]
        return visited[:-1]
    return []