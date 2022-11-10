from MainSplit import MainSplit

class Segment(MainSplit):
    def __init__(self, key, name):
        '''
        create the segment or subsplit
        all the times are stored in seconds
        '''
        super().__init__(name)
        self.start_time = None
        self.end_time = None
        
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
    
    # methods that override parent methods
    def start_segment(self):
        self.start_time = self.get_split_time()
    
    def pause_segment(self): 
        self.pause_split()
    
    def end_segment(self):
        self.end_time = self.get_split_time()
        
    def get_segment_start(self):
        return self.start_time
    
    def get_segment_end(self):
        return self.end_time