class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print('Linked list is empty')
        itr = self.head
        llstr = ' '
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr) 
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head 
        while itr.next:
            itr = itr.next   
        itr.next = Node(data,None)
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count
    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            print("Invalid exception")
        if index == 0:
            self.head = self.head.next
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1
    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            print("Invalid Exception")
        if index == 0:
            self.insert_at_beginning(data)
        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            count += 1
    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return
        if self.head == data_after:
            self.head = Node(data_to_insert,self.head)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break
            itr = itr.next
    def remove_by_value(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next =itr.next.next
                break
            itr = itr.next
    def search(self,input):
        itr = self.head
        count = 0
        while itr:
            if itr.data == input:
                print(count)
                return   # here we return instead of break because if element is not found it will directly exit from the loop without "printing not in linked list"
            itr = itr.next
            count += 1
        print("Not in Linked List")
    def insert_before(self,before,data):
        if self.head is None:
            return
        if self.head == before:
            self.insert_at_beginning(data)
        itr = self.head
        while itr:
            if itr.next.data == before:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
    def insert_after(self,after,data):
        if self.head is None:
            return
        if self.head == after:
            self.insert_at_end(data)
        itr = self.head
        while itr:
            if itr.data == after:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
    def reverse_linkedlist(self):
        if self.head == None or self.head.next == None:
            print(self.head)
            return
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    def sortList(self,head):
        if not head or not head.next:
            return head
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.mergeList(left,right)
    def getMid(self,head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def mergeList(self,left,right):
        dummy_ptr = head_ptr = Node()
        while (left and right):
            if left.data < right.data:
                dummy_ptr.next = left
                left = left.next
            else:
                dummy_ptr.next = right
                right =  right.next
            dummy_ptr = dummy_ptr.next

            if left:
                dummy_ptr.next = left
            if right:
                dummy_ptr.next = right
            return head_ptr.next
    
    


        
        



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(9)
    ll.insert_at_beginning(7)
    ll.print()
    ll.insert_at_end(79)
    ll.insert_at_end(99)
    ll.print()
    ll.insert_values(['Milli','Medha','Sai'])
    ll.print()
    print('Length:',ll.get_length())
    ll.remove_at(2)
    ll.print()
    ll.insert_at(2,"Sai")
    ll.print()
    ll.insert_after_value('Sai',"Nikhila")
    ll.print()
    ll.insert_after_value('Nikhila','Maya')
    ll.print()
    ll.remove_by_value('Maya')
    ll.print()
    ll.search('Sai')
    ll.search('Medha')
    ll.search('Milli')
    ll.insert_before('Nikhila','Siddu')
    ll.print()
    ll.remove_at(4)
    ll.print()
    ll.insert_before('Siddu','Nikhila')
    ll.print()
    ll.insert_after('Nikhila','Akhila')
    ll.print()
    ll.reverse_linkedlist()
    ll.print()
    
    ll.head = ll.sortList(ll.head)  #here ll.head will sort the list and prints the head i..e akhila
    
    print(ll.head.data)
    
    
    ll.print()