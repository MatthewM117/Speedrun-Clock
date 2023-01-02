class Segment():
    def __init__(self, name):
        # Object Properties
        self.split_name = name
        self.start_time = None
        self.end_time = None
        self.child_splits = [] 
        
        # Node Info
        self.key = 111
        self.next = None
        self.name = name
        
        # Segment Stats
        self.best_time = 0
        self.worst_time = 0
        self.average_time = 0
        self.latest_time = 0

    # Node Methods
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
    
    # Object Methods
    def set_start_segment(self, currentTime):
        self.start_time = currentTime
    
    def set_end_segment(self, currentTime):
        self.end_time = currentTime
    
    def get_segment_start(self):
        return self.start_time
    
    def get_segment_end(self):
        return self.end_time
    
    
    # modifying subsplits
    def add_child_split(self, name):
        new_segment = Segment(name)
        self.child_splits.append(new_segment)
        #if isinstance(self.splits.get_segment(name), Segment): not sure what this was for
        #    self.splits.get_segment(name).latest_time = 102

    def display_immediate_child_splits(self):
        print(f'child-splits: ')
        for i in self.child_splits:
            if isinstance(i, Segment):
                print(f' {i.name} ', end="")
        print("\n")

    def get_immediate_child_splits(self):
        return self.child_splits

    def get_child_splits(self):
        acc = None # accumilates all the split and child split names
        if len(self.child_splits) == 0:
            acc = self.split_name + " "
            return acc
        else:
            acc = self.split_name + " ["
            for i in self.child_splits:
                print(i.split_name)
                if isinstance(i, Segment):
                    acc += i.get_child_splits()
            acc += "] "
        return acc
                
    def get_child_splits_length(self):
        return len(self.child_splits)
    
    def get_child_split(self, target): # target is the split/segment you want to get
        for i in self.child_splits:
            if isinstance(i, Segment):
                if i.name == target:
                    return i
    
    def __add__(self, b): 
        if isinstance(b, Segment):
            return self.latest_time + b.latest_time
        
    def __radd__(self, b):
        if isinstance(b, Segment):
            return self.latest_time + b.latest_time
    
    def __str__(self) -> str:
        return (str) (self.split_name)
    
    
