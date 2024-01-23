class Node(object):
    
    def __init__(self, x, nxt=None):
        """
        :type x: int
        :type nxt: Node | None
        """
        self.val = x
        self.next = nxt

class MyLinkedList(object):
    
    INVALID = -1
    
    def __init__(self):
        self.first = None
        self.size = 0
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        node = self.getNode(index)
        return node.val if node else self.INVALID
    
    def getNode(self, index):
        """
        :type index: int
        :rtype: Node | None
        """
        if index >= self.size or index < 0:
            return None
        node = self.first
        while index > 0:
            node = node.next
            index -= 1
        return node

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size or index < 0:
            return
        prev = self.getNode(index-1)
        if prev:
            prev.next = Node(val, prev.next)
        else:
            self.first = Node(val, self.first)
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index >= self.size or index < 0:
            return
        prev = self.getNode(index-1)
        if prev:
            prev.next = prev.next.next if prev.next else None
        else:
            self.first = self.first.next
        self.size -= 1