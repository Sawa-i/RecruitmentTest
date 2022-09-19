# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            pos = n

            if(head == None): # If LinkedList Empty
                raise Exception("\n[-] Linked List is Empty! Exiting...")
            
            if(pos<1): #If Position is 0 or -ve Value
                raise Exception("\n[-] Position can't be less than 1")

            temp = head
            temp2 = head
            xPos = 1
            size=1
            while(temp2!= None and temp2.next!= None): # Loop that determines the Size Quickly as well as traverses Half
                temp = temp.next
                temp2 = temp2.next.next
                xPos+=1
                size+=2
            
            if(temp2==None): # Adjustment of Size depending upon Position of 'temp2' pointer
                size-=1
                
            if(pos>size): # Checking whether Position exceeds size
                raise Exception("\n[-] Position exceeds the size of Linked List")
                
            targetX = size+1 - pos # Calculating position from the start
            
            if(pos==size): # If the First Node is to be deleted, delete accordingly
                temp = head
                head = head.next
                temp.next = None
                return head
            
            if(targetX<=xPos): # If the Deleting Node is in first half, reset pointer 'temp'
                xPos=1
                temp=head
                
            while(xPos != targetX-1): # Reach the node before the deleting Node
                temp=temp.next
                xPos+=1
                
            
            # Deleting Node from Linked List
            delet = temp.next
            temp.next = temp.next.next
            delet.next = None
            
            return head
