class Segment():
    def __init__(self, key, name, numb_of_children=0):
        # Object Properties
        self.split_name = name
        self.start_time = None
        self.end_time = None
        self.child_splits = [Segment(111, 'split' + i, 0) for i in range(numb_of_children)] #change this to whatever datastruct later
        
        # Node Info
        self.key = key
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
    
    
