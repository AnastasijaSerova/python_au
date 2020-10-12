# Linked List

+ [Reverse Linked List](#reverse-linked-list)

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        ret = Solution.reverseList(self, head.next)
        head.next.next = head
        head.next = None
        return ret
```
