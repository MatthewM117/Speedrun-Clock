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