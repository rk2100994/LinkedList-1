class Node:
    def __init__(self,data,n=None):
        self.data = data
        self.next = n
    def get_next(self):
        return self.next
    def set_next(self,node):
        self.next = node
    def get_data(self):
        return self.data
    def set_data(self,data):
        self.data = data   
    def has_next(self): #to check if the calling node has next node
        if self.get_next() is None:
            return False
        return True
    def to_string(self):
        # return "Node Value " + str(self.data)
        return "Node Value " + str(self.data)

class LinkedLists:
    def __init__(self):
        self.head = None
        self.size = 0
    def get_size(self):
        return self.size
    def add(self,data):
        # add at first
        new_node = Node(data,self.head)
        self.head = new_node #setting head pointer to the new_node
        self.size +=1
    def add_node(self, n):
        n.set_next(self.head)
        self.head = n
        self.size +=1
    def find(self,data):
        curr_node = self.head
        # while until end of node
        while curr_node is not None:
            if(curr_node.get_data() == data):
                return data
            elif curr_node.get_next() == None: #means we reached last node
                return False
            else:
                curr_node = curr_node.get_next()
    def remove(self,data):
        curr_node = self.head
        prev_node = None
        while curr_node is not None:
            if(curr_node.get_data() == data):
                if(prev_node is not None):
                    prev_node.set_next(curr_node.get_next())
                else:
                    self.head == curr_node.get_next() #if the data is in first node, we just set the head pointer to the next node
                self.size -= 1
                return True #data removed
            else:
                prev_node = curr_node
                curr_node = curr_node.get_next()    
        return False # data not found
    def printList(self):
        if self.head is None:
            return
        curr_node = self.head
        print(curr_node.to_string())
        while curr_node.has_next():
            curr_node = curr_node.get_next()
            print(curr_node.to_string())
    def sort(self):
        if self.size > 1:
            newlist = []
            current = self.head
            newlist.append(self.head)
            while current.has_next():
                current = current.get_next()
                newlist.append(current)
            newlist = sorted(newlist, key = lambda node: node.get_data(), reverse = True)
            newLl = LinkedLists()
            for node in newlist:
                newLl.add_node(node)
            return newLl
        return self

def main():
    myList = LinkedLists()
    myList.add(5)
    myList.add(9)
    myList.add(3)
    myList.add(8)
    myList.add(9)
    print("Size of the LinkedList is: "+str(myList.get_size()))
    myList.printList()
    print("After sorting LinkedList")
    myList = myList.sort()
    myList.printList()
    myList.remove(8)
    print("Size of the LinkedList is: "+str(myList.get_size()))
    print("Remove 25",myList.remove(25))
    print("Size of the LinkedList is: "+str(myList.get_size()))
    print("Find an element ",myList.find(15))
    print("Final Linked List is a below: \n")
    myList.printList()
main()
