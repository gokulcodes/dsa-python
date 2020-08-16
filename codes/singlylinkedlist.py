class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return 
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self, prev_node, next_node):
        new_node = Node(next_node)
        if prev_node == Node:
            self.head = new_node
            return
        
        new_node.next = prev_node.next 
        prev_node.next = new_node

    def delete(self, keys):
        temp = self.head
        if temp is not None:
            if temp == self.head:
                self.head = temp.next
                temp = None
                return 
        
        while temp is not None:
            if temp.key == keys:
                break
            prev = temp
            temp = temp.next
        
        if temp == None:
            return 
            
        print(prev.key, temp.key)
        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head
        count = 0
        while (temp):
            print(temp.key)
            count = count + 1
            temp = temp.next
        print("Total Element in LinkedList: "+ str(count))

if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.push(2)
    llist.delete(2)
    # n, m = map(int, input().split())
    # for i in range(0, n):
    #     llist.push(i)
    # llist.insertAfter(llist.head.next, n)
    llist.printList()


    