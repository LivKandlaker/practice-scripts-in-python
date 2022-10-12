# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # print method for the linked list
  def printLL(self):
    current = self.head
    list_new = []
    while(current):
      print(current.data)
      current = current.next

# print method for the linked list
def addTwoNumbers(self, l1, l2):
    """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
    """
    current1 = l1.head
    current2 = l2.head
    sum1 = 0
    sum2 = 0
    counter1 = 0
    counter2 = 0
    while (current1):
        if counter1 == 0:
            counter1 += 1
            sum1 += current1.data
            current1 = current1.next
        elif counter1 > 0:
            counter1 = counter1 * 10
            sum1 += current1.data * counter1
            current1 = current1.next
    while (current2):
        if counter2 == 0:
            counter2 += 1
            sum2 += current2.data
            current2 = current2.next
        elif counter2 > 0:
            counter2 = counter2 * 10
            sum2 += current2.data * counter2
            current2 = current2.next
    TotalSum = sum1 + sum2
    l3 = LinkedList()
    while TotalSum > 0 :
        a = TotalSum % 10
        TotalSum = int(TotalSum / 10)
        l3.insert(a)
    return l3

# Linked List with a single node
L1 = LinkedList()
L1.head = Node(9)
L1.insert(9)
L1.insert(9)
L1.insert(9)
L1.insert(9)
L1.insert(9)
L1.insert(9)
L2 = LinkedList()
L2.head = Node(9)
L2.insert(9)
L2.insert(9)
L2.insert(9)

# l1 = [0], l2 = [0]
result = addTwoNumbers(LinkedList, L1, L2)
result.printLL()
