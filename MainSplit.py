from operator import truediv
from LinkedList import LinkedList
import time
import threading

class MainSplit: 
    def __init__(self, split_name): 
        self.timer_thread_object = None
        self.split_name = split_name
        self.sub_splits = LinkedList()
        self.timer_offset = 0
        self.end_time = None
        
        '''
        self.show_miliseconds = True
        self.pause = False
        self.restart_timer = False
        '''

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
        print(self.timer_thread_object.get_current_time())

    def start_timer(self, test_seconds):
        '''
        seconds = 0
        miliseconds = 0
        while True:
            if not self.pause:
                for _ in range(0, 10):
                    if self.pause:
                        break

                    if self.restart_timer:
                        break

                    miliseconds += 1
                    if self.show_miliseconds:
                        print("{}.{}".format(seconds, int(str(miliseconds)[0])), end="\r")
                    else:
                        print("{}".format(seconds), end="\r")
                    time.sleep(0.1)

                if self.restart_timer:
                    self.restart_timer = False
                    print("0.0", end="\r")
                    break

                miliseconds = 0
                seconds += 1
                if seconds == test_seconds: # just for testing
                    break
            time.sleep(0.1)
        '''
            
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
        self.thread = threading.Thread(target=self.start_time_thread, args=(60, ), name="timer")
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

                    self.miliseconds += 1
                    if self.show_miliseconds:
                        print("{}.{}".format(self.seconds, int(str(self.miliseconds)[0])), end="\r")
                    else:
                        print("{}".format(self.seconds), end="\r")
                    time.sleep(0.1)

                if self.restart_timer:
                    self.seconds = 0
                    self.miliseconds = 0
                    self.time_elapsed = 0
                    self.restart_timer = False
                    print("0.0", end="\r")
                    # break this break gets out of the while true

                self.miliseconds = 0
                self.seconds += 1
                if self.seconds == test_seconds: # just for testing
                    break
            time.sleep(0.1)
    
    
    def get_current_time(self):
        return "{}.{}".format(self.seconds, int(str(self.miliseconds)[0]))
    


if __name__ == "__main__":
    test = MainSplit("Test")
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
