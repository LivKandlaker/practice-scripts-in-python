# You are given two non-empty lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    counter = 0
    counter2 = 0
    for i in range(0, (len(list(l1)))):
        if counter == 0:
            counter += 1
            sum_l1 = l1[i] * counter
        elif counter > 0:
            counter = counter * 10
            sum_l1 += l1[i] * counter
    for i in range(0, (len(list(l2)))):
        if counter2 == 0:
            counter2 += 1
            sum_l2 = l2[i] * counter2
        elif counter2 > 0:
            counter2 = counter2 * 10
            sum_l2 += l2[i] * counter2
    Total_sum = sum_l1 + sum_l2
    l3 = []
    while Total_sum > 0 :
        a = Total_sum % 10
        Total_sum = int(Total_sum / 10)
        l3.append(a)
    return l3


l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]

result = addTwoNumbers(l1, l2)
print(result)