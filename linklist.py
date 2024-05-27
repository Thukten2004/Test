# Define a class named Node representing a single node in a
#singly linked list.
class Node:
# method for the Node class. Node will have two attributes: data and next.
    def __init__(self, data):
# Initialize the data attribute of the node with the
#given data.
        self.data = data
# Initialize the next attribute of the node as None,indicating that it initially does not point to any other node as its empty.
        self.next = None
# Define a class named SinglyLinkedList representing a singly linked list.
class SinglyLinkedList:
# Define the constructor method for the SinglyLinkedListclass.
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


sll = SinglyLinkedList()
# Append some elements to the linked list.
sll.append(1)
sll.append(2)
sll.append(3)
# Display the elements of the linked list.
sll.display()
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None 
        curr = head 
        while curr:
            next_node = curr.next
            curr.next = prev 
            prev = curr 
            curr = next_node 
        return prev
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        return dummy.next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow = fast = dummy
# Move the 'fast' pointer n steps ahead of the 'slow' pointer.
        for i in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next