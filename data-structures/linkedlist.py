# linkedlist.py
# Andrew Eljumaily
#
# An example of a basic linked list with some sample output.


class Node(object):
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextNode

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.nextNode = newNext


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, nodeData):
        newNode = Node(nodeData)
        newNode.setNext(self.head)
        self.head = newNode

    def size(self):
        currentNode = self.head
        nodeCount = 0
        while currentNode:
            nodeCount += 1
            currentNode = currentNode.getNext()

        return nodeCount

    def search(self, data):
        currentNode = self.head
        found = False
        while (currentNode and found is False):
            if(currentNode.getData() == data):
                found = True
            else:
                currentNode = currentNode.getNext()
        if(currentNode is None):
            raise ValueError("Item not in list")

        return currentNode

    # Deletes node by pointing previousNode to the node after
    # currentNode

    def delete(self, data):
        currentNode = self.head
        previousNode = None
        found = False
        while (currentNode and found is False):
            if(currentNode.getData() == data):
                found = True
            else:
                previousNode = currentNode
                currentNode = currentNode.getNext()
        if(currentNode is None):
            raise ValueError("Item not in list")
        else:
            previousNode.setNext(currentNode.getNext())


# Test output


ll = LinkedList()

ll.insert(1)
ll.insert(2)
ll.insert(3)

print("Added 1, 2, and 3 to the list")

print("The current list size is: ", ll.size())

print("Search for 2 in the list: ", ll.search(2).getData())

ll.delete(2)

print("Deleted 2 from list")

print("The current list size is: ", ll.size())
