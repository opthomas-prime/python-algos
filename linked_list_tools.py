########################################################
### Definition for singly-linked list.
########################################################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

########################################################
### Dummy / Prehead Node Technique
########################################################
# Explanation: You can use a dummy/prehead node to create something to point to head. (ListNode(0, head))
#              Then, you can just point to prehead.next to return the head of the list after you've traversed / manipulated the list in your problem
########################################################
### Algorithm for reversing a linked list
########################################################
def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr 
        curr = nxt
    
    return prev

########################################################
### Algorithm for merging two sorted lists
########################################################
def mergeTwoLists(list1, list2):
    prehead = ListNode(0)
    prev = prehead

    while list1 and list2:
        if list1.val < list2.val:
            prev.next = list1
            list1 = list1.next

        else:
            prev.next = list2
            list2 = list2.next
        
        prev = prev.next
    
    prev.next = list1 if list1 is not None else list2

    return prehead.next

########################################################
### Algorithm for finding the midpoint of a linked list
########################################################
# Explanation: You set two ptrs (a slow and a fast)
#              - You iterate while fast is not None and fast.next is not None
#                   - This is because you need to make sure that there are two spots ahead for the fast ptr
#                   - If fast is None, then you've reached the tail of the list (middle will be offset 1 - even number of non-empty nodes)
#                   - If fast.next is None, then you've reached the last non-empty node, so slow will be at the midpoint (middle will be direct - odd number)

def middle_of_list(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

########################################################
### Algorithm for removing Nth node from list
########################################################
# Explanation: Create an offset by having a right ptr shifted by N spots. Then, starting with the left ptr at a Node prior to the head (-1 position),
#              start to move until right is at the tail (while right:) and then replace (left.next = left.next.next)
def remove_nth_node(head, n):
    prehead = ListNode(0, head)
    left = prehead
    right = head
    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left, right = left.next, right.next

    left.next = left.next.next
    return prehead.next

########################################################
### Algorithm for detecting a cycle in a Linked List 
########################################################
def find_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False

########################################################
### Algorithm for reording a Linked List 
########################################################
# Example: 1 -> 2 -> 3 -> 4 -> X ==> 1 -> 4 -> 2 -> 3 -> X

def reorder_list(head):
    # Step 1: Find Middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse Second List
    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # Step 3: Merge 2 Lists together
    first = head
    second = slow

    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
    
    return head

########################################################
### Algorithm for merging K sorted lists
########################################################
def mergeKLists(lists):
    if len(lists) == 0:
        return None
    
    while len(lists) > 1:
        mergedLists = []

        # iterated every two lists
        for i in range(0, len(lists), 2):
            l1 = list[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None # make sure l2 is in range, else we can just merge with None
            mergedLists.append(mergeTwoLists(l1, l2))
        
        lists = mergedLists
    
    return lists[0]
 