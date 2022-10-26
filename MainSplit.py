from LinkedList import LinkedList


class MainSplit: 
    def __init__(self, split_name): 
        self.split_name = split_name
        self.sub_splits = LinkedList()
        self.end_time = None

    def finish_split(self): 
        self.end_time = None
