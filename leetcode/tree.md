# tree

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Invert Binary Tree](#invert-binary-tree)

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

