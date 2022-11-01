# dictionary using hashtable and linked lists

from LinkedList import LinkedList
from Segment import Segment

class Dictionary:

    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key) -> int:
        value = int(key[0])
        x = 41
        M = self.size

        # polynomial hash code
        for i in range(len(key) -2, 0, -1):
            value = (value * x + int(key[i])) % M
        
        return value
    
    def put(self, seg) -> int:
        # collisoins are handled by seperate chaining

        if self.get(seg.get_key() != None):
            return None
        
        hash_value = self.hash(seg.get_key())

        if self.table[hash_value] == None:
            result = 0
            self.table[hash_value] = LinkedList()
        else:
            result = 1

        self.table[hash_value].add_last(seg)

        return result

    def get(self, key) -> Segment:
        # checks if segment is in table. if it is, return it. otherwise return null (None)

        hashValue = hash(key)
        if self.table[hashValue] == None:
            return None
        
        count = 0
        for i in self.table:
            if i.get(count).get_key() == key:
                return i.get(count)
            count += 1

        return None

    def get_segment(self, name) -> Segment:
        count = 0
        for i in self.table:
            if isinstance(i, LinkedList):
                if i.get(count).name == name:
                    return i.get(count)
                count += 1
        return None
            
    def get_linked_list(self, name) -> LinkedList:
        '''
        gets the linked list based on the name of the first split
        '''
        count = 0
        for i in self.table:
            if isinstance(i, LinkedList):
                if i.get(count).name == name:
                    return i
        return None

    def print_dict(self):
        print(self.table)

if __name__ == "__main__":
    test_dict = Dictionary(11)

    test_seg = Segment("0011", "Split1")

    test_seg2 = Segment("00221112", "FirstSplit")
    test_seg3 = Segment("00221112", "Split2")

    test_dict.put(test_seg)

    test_dict.put(test_seg2)
    test_dict.put(test_seg3)

    print(test_dict.get_linked_list("FirstSplit"))

    '''
    test_dict.get_segment("Split2").latest_time = 205

    print(test_dict.get_segment("Split2").latest_time)
    print(test_dict.get_segment("Split1").name)

    test_dict.print_dict()
    '''