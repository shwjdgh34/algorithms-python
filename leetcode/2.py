# Definition for singly-linked list.

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

# 내장함수? 같은걸로 해도 될듯
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
            



class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         num1 = list2num(l1)
#         num2 = list2num(l2)

#         sum = num1 + num2

#         rlist = num2list(sum)

#         print(list2num(rlist))
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         return rlist


class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        n1=0
        n2=0
        ten=0
        sum=0
        
        while l1:
            n1 = n1 + (l1.val*(10**ten))
            ten+=1
            l1 = l1.next
      
        ten=0
        
        while l2:
            n2 = n2 + (l2.val*(10**ten))
            ten+=1
            l2 = l2.next
        
        sum = n1+n2
        testsum=sum
        length = 1
        
        while testsum//10 > 0:
            length+=1
            testsum=testsum//10
            
        node = None
        head = None
        while length > 0:
            if node==None:
                node = ListNode(sum%10)
                head = node
                #print(node)
            else:
                new_node = ListNode(sum % 10)
                node.next = new_node
                node=node.next
                #print(node)
            sum=sum/10
            length-=1
        #print(head)  
        return head


l1 = num2list(456)
l2 = num2list(678)

print(list2num(l1))
print(list2num(l2))


s = Solution()
s.addTwoNumbers(l1, l2)

