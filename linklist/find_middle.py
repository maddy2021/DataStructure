#Class to make Node
class Node:
    def __init__(self,data,nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data
    
    def setData(self,val):
        self.data = val
    
    def getNextNode(self):
        return self.nextNode

    def setNextNode(self,val):
        self.nextNode = val

#class for linklist
class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def insertNode(self,data):
        newNode = Node(data,self.head)
        self.head = newNode
        return True

    #logic to find middle value in linklist using floyd algorithm 
    def findMiddle(self):
        fast_ptr = self.head
        slow_ptr = self.head
        if(self.head is not None) : 
            while fast_ptr is not None and fast_ptr.getNextNode() is not None:
                slow_ptr = slow_ptr.getNextNode()
                fast_ptr = fast_ptr.getNextNode().getNextNode()
            print(slow_ptr.data)

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()
    

#Find middle
myList = LinkedList()
print("Inserting")
for i in range(1,101):
    myList.ins(i)

myList.findMiddle()

