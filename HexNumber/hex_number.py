class Node:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '{}'.format(self.val)

    def get(node):
        if node is None:
            return '0'
        else:
            return node.val


class LinkedListIterator:

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


class LinkedList:

    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size

    def __iter__(self):
        return LinkedListIterator(self.head)

    def addAtHead(self, val):
        new = Node(val, self.head)
        self.head = new

    def __str__(self):
        res = ''
        for i in self:
            res = i + res
        if res == '':
            return '0'
        return res

class HexNumber:
    dec_to_hex = {i:c for i, c in enumerate('0123456789ABCDEF')}
    hex_to_dec = {c:i for i, c in enumerate('0123456789ABCDEF')}

    def __init__(self, num=None):
        if num != num.upper():
            print("Error! Number must be UPPERCASE!")
            return None
        self.num = LinkedList()
        for ch in num:
            if ch not in "0123456789ABCDEF":
                print("Error! Invalid number!")
                return None
            self.num.addAtHead(ch)
            self.num.size += 1

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        rest = 0
        res = ""
        a = self.num.head
        b = other.num.head
        while a or b:
            rest += HexNumber.hex_to_dec[Node.get(a)] + HexNumber.hex_to_dec[Node.get(b)]
            if rest > 16:
                rest -= 16
                res = HexNumber.dec_to_hex[rest] + res
                rest = 1
            else:
                res = HexNumber.dec_to_hex[rest] + res
                rest = 0
            a = a.next
            b = b.next
        if rest > 0:
            res = HexNumber.dec_to_hex[rest] + res
        return HexNumber(res)
