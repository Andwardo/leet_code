# 
# add_two_numbers.py
#
# Created: 3 Jul 2025
# Edited:  3 Jul 2025
#
# Version 1.0
# Andwardo
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(nums):
    dummy = ListNode()
    current = dummy
    for n in nums:
        current.next = ListNode(n)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def add_two_numbers(l1, l2):
    dummy_head = ListNode()
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        current.next = ListNode(digit)
        current = current.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy_head.next

# === Interactive User Input ===
input1 = input("Enter first number in reverse order (e.g., 2,4,3 for 342): ")
input2 = input("Enter second number in reverse order (e.g., 5,6,4 for 465): ")

# Convert input strings to lists of integers
nums1 = list(map(int, input1.strip().split(',')))
nums2 = list(map(int, input2.strip().split(',')))

# Convert to linked lists
l1 = list_to_linkedlist(nums1)
l2 = list_to_linkedlist(nums2)

# Add numbers
result_node = add_two_numbers(l1, l2)

# Convert result to list and print
result_list = linkedlist_to_list(result_node)
print("Sum as reversed linked list:", result_list)
