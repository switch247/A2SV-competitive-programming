class Node(object):
    
    def __init__(self, x, nxt=None):
        """
        :type x: int
        :type nxt: Node | None
        """
        self.val = x
        self.next = nxt

class MyLinkedList(object):
     def __init__(self):
        self.first = None
        self.size = 0
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        node = self.getNode(index)
        return node.val if node else -1
    
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
        
    """
    #
    if implemented using array
    
    class MyLinkedList:
    def __init__(self):
        self.link = []

    def get(self, index: int) -> int:
        if index >=0 and index <len(self.link):
            return self.link[index]
        return -1

    def addAtHead(self, val: int) -> None:
        self.link.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.link.append(val)
 

    def addAtIndex(self, index: int, val: int) -> None:
        if index == len(self.link):
            self.link.append(val)
            return
        if index >= 0 and index < len(self.link):
            self.link.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if index >=0 and index <len(self.link):
            self.link.pop(index)
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
    
    
    
    """
