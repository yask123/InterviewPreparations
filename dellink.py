class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

def delete_node(node):
	

def printall(head):
	temp = head
	while(temp):
		print temp.value,
		temp = temp.next
printall(a)
delete_node(b)
print ''
printall(a)