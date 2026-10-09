# 92. reverse linked list II
# walk to the node before `left`, then head-insert nodes one by one

# leetcode provides this:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0, head)
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        cur = pre.next
        for _ in range(right - left):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
        return dummy.next
