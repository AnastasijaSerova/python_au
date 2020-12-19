class Node:

    def __init__(
        self,
        val=0,
        prev=None,
        next=None,
        ):
        self.val = val
        self.prev = prev
        self.next = next

class Iterator:
    def __init__(self, node):
        self.node = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.node is None:
            raise StopIteration
        else:
            node = self.node
            self.node = self.node.next
            return node.val

class MyLinkedList(object):

    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size

    def __iter__(self):
        return Iterator(self.head)

    def get(self, index):
        node = self.getLink(index)
        if node:
            return node.val
        else:
            return -1

    def getLink(self, index):
        if index >= self.size or index < 0:
            return None
        else:
            node = self.head
            for i in range(index):
                node = node.next
            return node

    def addAtHead(self, val):
        new = Node(val, None, self.head)
        if self.head:
            self.head.prev = new
        self.head = new
        self.size += 1

    def addAtTail(self, val):
        if self.size == 0:
            self.addAtHead(val)
        else:
            node = self.getLink(self.size - 1)
            new = Node(val, node)
            node.next = new
            self.size += 1

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        node = self.getLink(index)
        if node:
            new = Node(val, node.prev, node)
            new.prev.next = new
            new.next.prev = new
            self.size += 1

    def add(self, val):
        self.addAtTail(val)

    def deleteAtIndex(self, index):
        node = self.getLink(index)
        if node:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            if index == 0:
                self.head = node.next
            self.size -= 1

def main():
    lst = MyLinkedList()
    lst.add(3)
    lst.add(5)
    lst.add(7)

    it = iter(lst)

    print(next(it))
    print(next(it))
    print(next(it))
    print("-----")
    for num in lst:
        print(num)

if __name__ == "__main__":
    main()
