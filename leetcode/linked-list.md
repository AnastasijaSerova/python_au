# Linked List

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Linked List Cycle II](#linked-list-cycle-ii)
+ [Linked List Cycle](#linked-list-cycle)

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

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
class Solution(object):
    def middleNode(self, head):
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) / 2]
```

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python
class Solution:
    def isPalindrome(self, head):
        def reverse(node):
            prev = None
            curr = node
            while curr is not None:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        if head is None or head.next is None:
            return True
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        back = reverse(mid)
        curr = head
        while back is not None:
            if back.val != curr.val:
                return False
            back = back.next
            curr = curr.next
        return True
```

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

```python
class Solution:
    def mergeTwoLists(self, l1, l2):
        head = curr = None
        while l1 and l2:
            if l1.val < l2.val:
                if curr:
                    curr.next = l1
                curr = l1
                l1 = curr.next
            else:
                if curr:
                    curr.next = l2
                curr = l2
                l2 = curr.next
            if not head:
                head = curr
                continue
        if not head:
            return l1 if l1 else l2
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return head
```

## Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
class Solution:
    def removeNthFromEnd(self, head, n):
        i = j = 0
        n += 1
        node_i = node_j = head
        while i + j != n and node_j:
            j += 1
            node_j = node_j.next
        if i + j != n:
            return head.next
        while node_j:
            node_j = node_j.next
            node_i = node_i.next
        node_i.next = node_i.next.next
        return head
```

## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

```python
class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        ans = None
        nodeset = set()
        node = head
        while node:
            if node.next in nodeset:
                ans = node.next
                break
            nodeset.add(node)
            node = node.next
        return ans
```

## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

```python
class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        i = 0
        while i <= 10000:
            head = head.next
            if head:
                return False
            i += 1
        return True
```