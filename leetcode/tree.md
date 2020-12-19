# tree

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Symmetric Tree](#symmetric-tree)

## Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

```python
class Solution(object):

    def maxDepth(self, root):
        return self.children(root)

    def children(self, t):
        if t is None:
            return 0
        if t.left is None and t.right is None:
            return 1
        return 1 + max(self.children(t.left), self.children(t.right))
```

## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

```python
class Solution(object):

    def inorderTraversal(self, root):
        if root is None:
            return []

        left_children = self.inorderTraversal(root.left)
        right_children = self.inorderTraversal(root.right)

        return left_children + [root.val] + right_children
```

## Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

```python
class Solution(object):

    def invertTree(self, root):
        if root:
            (root.left, root.right) = (root.right, root.left)
            self.invertTree(root.right)
            self.invertTree(root.left)

        return root
```

## Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

```python
class Solution(object):

    def levelOrder(self, root):
        if root is None:
            return []

        result = []
        queue = []
        queue.append(root)

        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)

                if not node.left is None:
                    queue.append(node.left)

                if not node.right is None:
                    queue.append(node.right)
            result.append(level)
        return result
```

## Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

```python
class Solution(object):

    def kthSmallest(self, root, k):

        def helper(cur, nodes):
            if not cur:
                return
            helper(cur.left, nodes)
            nodes.append(cur.val)
            helper(cur.right, nodes)

        nodes = []
        helper(root, nodes)
        return nodes[k - 1]
```

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

```python
class Solution(object):

    def isValidBST(self, root):

        def check(node, low_range=float('-inf'), high_range=float('inf'
                  )):
            if not node:
                return True
            elif not low_range < node.val < high_range:
                return False

            return check(node.left, low_range, node.val) \
                and check(node.right, node.val, high_range)

        return check(root)
```

## Symmetric Tree

https://leetcode.com/problems/symmetric-tree/

```python
class Solution(object):
    def isSymmetric(self, root):
        def is_same_node(l, r):
            if l is None and r is None:
                return True
            elif l is None or r is None:
                return False

            if l.val != r.val:
                return False

            return is_same_node(l.left, r.right) and is_same_node(l.right, r.left)
        
        if root is None:
            return True
        
        return is_same_node(root.left, root.right)
```

