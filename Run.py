# from Dictionary import Dictionary

import time
from TimerThread import TimerThread
from Segment import Segment

class Run: 
    def __init__(self, name): 
        self.timer_thread_object = None
        self.run_name = name
        self.main_split = Segment(f'{name}-Main-Split')
        # a run contains a main split. A main split contains all splits (and it's splits can have subsplits by having an array of the same Segment class)
        # do you agree with this design?
        
        # make sure size of dictionary is a prime number
        # self.splits = Dictionary(6577)
        '''
        self.show_miliseconds = True
        self.pause = False
        self.restart_timer = False
        '''
    
    
    # Reinplment in segment.py 
    def get_main_split(self):
        return self.main_split
    
    def add_split(self, name):
        self.main_split.add_child_split(name)

    def display_splits(self):
        output = self.main_split.get_child_splits()
        print(output)

    def get_split(self, target_name): # target is the split/segment you want to get
        self.main_split.get_child_split(target_name)

    def get_splits_list(self):
        self.main_split.display_immediate_child_splits()
    
    def start_run(self):
        self.timer_thread_object = TimerThread(True)
        self.timer_thread_object.initialize_thread()
        self.main_split.set_start_segment(0)
        print(self.main_split.get_segment_start())
    
    def pause_run(self):
        self.timer_thread_object.pause_time_thread()
        
    def unpause_run(self):
        self.timer_thread_object.unpause_time_thread()

    def restart_run_timer(self): 
        self.timer_thread_object.restart_time_thread()
    
    def finish_run(self): 
        self.main_split.set_end_segment(self.timer_thread_object.get_current_time())
        self.timer_thread_object.end_timer_thread()
        print(self.main_split.get_segment_end())
        # need to look at different options for stopping the thread
        
    def get_run_time(self):
        self.timer_thread_object.get_current_time()
           
           


    

if __name__ == "__main__":
    test = Run("Test")
    test.start_run()
    time.sleep(5)
    test.finish_run()
    
    
    """
    test.add_split("0011", "Split1")
    test.add_split("0011", "Split2")
    test.add_split("0011", "Split3")
    FSN = "Split1"
    test.get_split(FSN, "Split1").latest_time = 67
    test.get_split(FSN, "Split2").latest_time = 122
    test.get_split(FSN, "Split3").latest_time = 336 
    test.start_split()
    test.subsplit.start_segment()
    time.sleep(2)
    test.subsplit.end_segment()
    test.subsplit.get_segment_start()
    test.subsplit.get_segment_end()
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
    """
