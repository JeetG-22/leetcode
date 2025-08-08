class Node(object):
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class MyLinkedList(object):

    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        cur = self.head.next
        count = 0
        while cur:
            if count == index:
                return cur.val
            count += 1
            cur = cur.next
        return -1
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if self.head == self.tail: #if list is empty
            self.tail = new_node
            new_node.prev = self.head
        else:
            new_node.next.prev = new_node
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        #if list is empty
        if self.tail == self.head:
            self.head.next = new_node
            self.tail = new_node
            new_node.prev = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        cur = self.head
        count = 0
        while cur and count < index:
            count += 1
            cur = cur.next
        #greater than length 
        if not cur:
            return 
        #empty list equal or length of list
        if self.tail == self.head or cur == self.tail:
            self.addAtTail(val)
            return
        new_node = Node(val)
        new_node.next = cur.next
        new_node.prev = cur
        new_node.next.prev = new_node
        new_node.prev.next = new_node


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        cur = self.head.next
        count = 0
        while cur and count < index:
            count += 1
            cur = cur.next
        #index not valid or empty list
        if not cur or self.head == self.tail:
            return
        #deleting the tail
        if cur == self.tail:
            self.tail = cur.prev
            self.tail.next = None 
        else:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev 


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)