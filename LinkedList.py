# A linked list implementation 
# would be used for the array of subsplits? 
# since initializing the linkedlist and adding an element to the end takes O(N)
# it might be more effichent to use normal arrays, but would still need to consider
# normal array's time complexity. Example if a user uses gui to add an extra subplit in the middle of their list of subsplits 
# another idea is to just use a dictionary (hashmap) and call each subsplit by it's iterationName 
# for example if a user wants to switch the order of two subplits it might be faster to do it with a hashmap


from tokenize import Double


class LinkedList: 
    
    # To allow for us to not have to say Node(ourdata) every time we want to edit a linked list 
    # we can make a function to create a node every time data is passed to this class
    
    '''
    def __init__(self, nodes=None): 
        self.head = None
        if nodes is not None: 
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes: 
                node.next = Node(data=elem)
                node = node.next
    '''

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Segment(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Segment(data=elem)
                node = node.next
    
    def add_first(self, node): 
        node.next = self.head
        self.head = node

    def add_last(self, node): 
        if self.head is None: 
            self.head = node
            return
        for current_node in self: 
            pass
        current_node.next = node

    def get(self, index):
        current = self.head
        count = 0

        while current:
            if count == index:
                return current.get_data()
            count += 1
            current = current.next

        return None

    # change function to use the index instead? would require modification of  __iter__ 
    # depends on usage which is currently unclear
    def add_after(self, target_node_data, new_node): 
        if self.head is None: 
            raise Exception("List is empty")

        for node in self: 
            if node.data == target_node_data: 
                new_node.next = node.next
                node.next = new_node
                return
    

    # modify to delete by index?
    def remove_node(self, target_node_data): 
        if self.head is None: 
            raise Exception("List is empty")
        
        if self.head.data == target_node_data: 
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self: 
            if node.data == target_node_data: 
                previous_node.next = node.next
                return # leaves it up to the garbage collector to get rid of the value
            previous_node = node
        
        raise Exception("Node with data '%s' not found" % target_node_data)



    def __iter__(self): 
        node = self.head
        while node is not None: 
            yield node
            node = node.next

    
    def __repr__(self): 
        node = self.head
        nodes = []
        while node is not None: 
            nodes.append(node.name)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    


class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None
    
    def __repr__(self): 
        return self.data

class Segment:
    def __init__(self, key, name):
        '''
        create the segment or subsplit
        all the times are stored in seconds
        '''
        self.key = key
        self.next = None
        self.name = name
        self.best_time = 0
        self.worst_time = 0
        self.average_time = 0
        self.latest_time = 0

    def get_key(self) -> str:
        return self.key

    def split(self):
        return None

    def skip_split(self):
        return None

    def undo_split(self):
        return None

    def get_data(self):
        return self

if __name__ == "__main__": 
    linked_list_tester = LinkedList(["a", "b", "c", "d", "e"])
    print(linked_list_tester)
    print(linked_list_tester.add_first(Node("lol")))
    print(linked_list_tester.add_last(Node("hello")))
    print(linked_list_tester.add_after("d", Node("after")))
    print(linked_list_tester.remove_node("a"))
    
    print(linked_list_tester)
