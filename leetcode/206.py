# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = 0
        self.tail = 0
    def append(self, value):
        new_node = ListNode(value)
        if self.head == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

def num2list(num):
    rlist = LinkedList()
    if num == 0:
        rlist.append(num)
    else :
        while num:
            rlist.append(num % 10)
            num //= 10
    return rlist.head
def list2num(input_list_node):
    list_node = input_list_node
    num = 0
    count = 0
    while list_node:
        num += list_node.val*(10**count)  
        count += 1
        list_node = list_node.next
    return num
            

class Solution(object):
    def reverseList(self, head):
        r_list_node = ListNode()
        cur_node = r_list_node
        
        def recur(node):
            if node.next != 0:
                recur(node.next)
                
            cur_node.value = node.value
            cur_node.next = ListNode()
            cur_node = cur_node.next
                
            return 
    
        recur(head)
        
        return r_list_node
            


l1 = num2list(12345)
s = Solution()
s.reverseList(l1)