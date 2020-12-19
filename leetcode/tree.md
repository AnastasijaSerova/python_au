# Tree

+ [Maximum Depth of Binary Tree](maximum-depth-of-binary-tree)

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

