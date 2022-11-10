import time
import threading

class TimerThread(): 
    def __init__(self, show_milliseconds):
        self.thread = None
        
        self.seconds = 0
        self.miliseconds = 0
        self.time_elapsed = 0
        
        self.show_miliseconds = show_milliseconds
        self.pause = False
        self.restart_timer = False
        self.end_thread = False
        
    def initialize_thread(self):
        self.thread = threading.Thread(target=self.start_time_thread, args=(120, ), name="timer")
        self.thread.start()
        
    def pause_time_thread(self): 
        self.pause = True
    
    def unpause_time_thread(self):
        self.pause = False
    
    def restart_time_thread(self):
        self.restart_timer = True
    
    def end_timer_thread(self): 
        self.end_thread = True
        
    def start_time_thread(self, test_seconds):
        while True:
            if not self.pause:
                for _ in range(0, 10):
                    if self.pause:
                        break
                    
                    if self.end_thread: 
                        return

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
                
                if self.end_thread: 
                    return
                

            time.sleep(0.1)
    
    def get_current_time(self):
        return "{}.{}".format(self.seconds, int(str(self.miliseconds)[0]))