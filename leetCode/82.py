# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(-101, head)
        ptr = newHead.next
        prePtr = newHead
        inLoop = False
        while prePtr.next:
            #print(prePtr.val, ptr.val)
            while ptr.next and ptr.val == ptr.next.val:
                #print('inLoop',prePtr.val, ptr.val)
                inLoop = True
                ptr = ptr.next
            if inLoop:
                prePtr.next = ptr.next
                ptr = ptr.next
                inLoop = False
            else:
                prePtr = ptr
                ptr = ptr.next
        return newHead.next