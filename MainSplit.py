import time
import threading
from Dictionary import Dictionary
from Segment import Segment

class MainSplit: 
    def __init__(self, split_name): 
        self.timer_thread_object = None
        self.split_name = split_name
        self.timer_offset = 0
        self.end_time = None
        
        # make sure size of dictionary is a prime number
        self.splits = Dictionary(6577)
        '''
        self.show_miliseconds = True
        self.pause = False
        self.restart_timer = False
        '''
        

    def add_split(self, key, name):
        new_segment = Segment(key, name)
        self.splits.put(new_segment)
        if isinstance(self.splits.get_segment(name), Segment):
            self.splits.get_segment(name).latest_time = 102

    def display_splits(self, first_split_name):
        the_splits = self.splits.get_linked_list(first_split_name)
        for i in the_splits:
            if isinstance(i, Segment):
                print("{}: {}".format(i.name, i.latest_time))

    def get_split(self, first_split_name, target): # target is the split/segment you want to get
        the_splits = self.splits.get_linked_list(first_split_name)
        for i in the_splits:
            if isinstance(i, Segment):
                if i.name == target:
                    return i

    def get_splits_list(self, first_split_name):
        return self.splits.get_linked_list(first_split_name)
    
    def start_split(self):
        self.timer_thread_object = TimerThread(True)
        self.timer_thread_object.initialize_thread()
    
    def pause_split(self):
        self.timer_thread_object.pause_time_thread()
        
    def unpause_split(self):
        self.timer_thread_object.unpause_time_thread()

    def restart_timer(self): 
        self.timer_thread_object.restart_time_thread()
    
    def finish_split(self): 
        self.end_time = self.timer_thread_object.get_current_time()
        #self.timer_thread_object 
        # need to look at different options for stopping the thread
        
    def get_split_time(self):
        self.timer_thread_object.get_current_time()
            
class TimerThread(): 
    def __init__(self, show_milliseconds):
        self.thread = None
        
        self.seconds = 0
        self.miliseconds = 0
        self.time_elapsed = 0
        
        self.show_miliseconds = show_milliseconds
        self.pause = False
        self.restart_timer = False
        
    def initialize_thread(self):
        self.thread = threading.Thread(target=self.start_time_thread, args=(120, ), name="timer")
        self.thread.start()
        
    def pause_time_thread(self): 
        self.pause = True
    
    def unpause_time_thread(self):
        self.pause = False
    
    def restart_time_thread(self):
        self.restart_timer = True
    
    def start_time_thread(self, test_seconds):
        while True:
            if not self.pause:
                for _ in range(0, 10):
                    if self.pause:
                        break

                    if self.restart_timer:
                        break

                    if self.show_miliseconds:
                        print("{}.{}".format(self.seconds, int(str(self.miliseconds)[0])), end="\r")
                    else:
                        print("{}".format(self.seconds), end="\r")
                    
                    self.miliseconds += 1
                    time.sleep(0.1)

                if self.restart_timer:
                    self.seconds = 0
                    self.miliseconds = 0
                    self.time_elapsed = 0
                    self.restart_timer = False
                    print("0.0", end="\r")
                    break

                self.miliseconds = 0
                self.seconds += 1
                if self.seconds == test_seconds: # just for testing
                    break
            time.sleep(0.1)
    
    
    def get_current_time(self):
        return "{}.{}".format(self.seconds, int(str(self.miliseconds)[0]))



if __name__ == "__main__":
    test = MainSplit("Test")
    

    test.add_split("0011", "Split1")
    test.add_split("0011", "Split2")
    test.add_split("0011", "Split3")

    FSN = "Split1"
    test.get_split(FSN, "Split1").latest_time = 67
    test.get_split(FSN, "Split2").latest_time = 122
    test.get_split(FSN, "Split3").latest_time = 336

    test.start_split()
    test.get_split(FSN, "Split1").start_segment()
    time.sleep(2)
    test.get_split(FSN, "Split1").end_segment()
    
    test.get_split(FSN, "Split1").get_segment_start()
    test.get_split(FSN, "Split1").get_segment_end()
    
    '''
    test.display_splits("Split1")

    segment_to_remove = test.get_split("Split1", "Split2")
    
    the_splits = test.get_splits_list("Split1")
    the_splits.remove_node(segment_to_remove)
    print("\n")
    test.display_splits("Split1")
    
    test.start_split()

    time.sleep(2)
    test.pause_split()
    time.sleep(5)
    test.unpause_split()
    time.sleep(2)
    test.restart_timer()
    test.get_split_time()
    time.sleep(2)
    test.get_split_time()
    '''
