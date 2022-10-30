from operator import truediv
from LinkedList import LinkedList
import time
import threading

class MainSplit: 
    def __init__(self, split_name): 
        self.split_name = split_name
        self.sub_splits = LinkedList()
        self.end_time = None
        self.show_miliseconds = True
        self.pause = False
        self.restart_timer = False
        self.timer_offset = 0

    def finish_split(self): 
        self.end_time = None

    def start_timer(self, test_seconds):
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

if __name__ == "__main__":
    test = MainSplit("Test")

    timer = threading.Thread(target=test.start_timer, args=(10, ), name="timer")
    timer.start()
    
    while True:
        time.sleep(2)
        test.pause = True
        time.sleep(5)
        test.pause = False
        time.sleep(2)
        test.restart_timer = True
        time.sleep(2)
        timer = threading.Thread(target=test.start_timer, args=(2, ), name="timer")
        timer.start()
        break
