from Run import Run
from Segment import Segment
from os import system, name
from pynput import keyboard
import threading

timer_active = False
runs = {}
current_run = None

def on_press(key):
    try:
        #print('alphanumeric key {0} pressed'.format(
            #key.char))
        temp = key.char # need to put some line of code here that uses key.char to trigger the except
    except AttributeError:
        #print('special key {0} pressed'.format(
            #key))
        if timer_active and str(key) == "Key.space":
            print("pausing timer")
            pause_timer(current_run)

def on_release(key):
    #print('{0} released'.format(
        #key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


'''
function for clearning the terminal based on system
'''
def clear_terminal():
    # for windows
    if name == 'nt':
        _ = system('cls')
    
    # for mac and linux
    else:
        _ = system('clear')

def pause_timer(current_run):
    current_run.pause_run()

'''
A user input command based loop for using the program
'''
def main():

    #runs = {}
    user_command = None
    current_selection = Segment # the current split selected
    current_selection_path = [] # path from top level the split selected
    options = {
        "new run": "create a new run",
        "select": "select a split in a run",
        "add split": "add a split to current selection or new selection",
        "runs": "display all the created runs",
        "splits": "display all the splits in a run",
        "start timer": "starts the timer for your current selected splits",
        "exit": "exit the program"
    }

    '''
    function for dispaying all the current runs the user has defined
    '''
    def display_runs():
        print("runs:")
        for i in runs:
            print(f' {i} ')
    
    
    '''
    function for selecting a segment as deeply nested as required
    '''
    def select_segment():
        current_selection = Segment
        current_selection_path = []
        
        print("---new segment selection---")    
        display_runs()
        run_name = input("run name: ")
        selected_child_name = None
        try:
            current_selection = runs[run_name].get_main_split()
            current_selection_path.append(current_selection)
            print(current_selection)
            print(current_selection_path)
                
            select_child = input("select a child? (y/n): ")
            while select_child != "n":
                if current_selection.get_child_splits_length() == 0:
                    print(f'{current_selection} does not have any children')
                    break
                        
                print_segment_list(current_selection.get_immediate_child_splits())
                    
                selected_child_name = input("child name: ")
                current_selection = current_selection.get_child_split(selected_child_name)
                    
                current_selection_path.append(current_selection)
                print(current_selection)
                print(current_selection_path)
                select_child = input("select a child? (y/n): ")

        except KeyError:
            print('Invalid Input: no run with that name exists')
            
        return (current_selection, current_selection_path)
    
    
    '''
    function for printing the path to the current selected split
    '''
    def print_segment_list(segment_list):
        length = len(segment_list)
        if length > 0:
            for i in range(length):
                if (i == length-1):
                    print(f'{segment_list[i]}', end="\n")
                else:
                    print(f'{segment_list[i]} --> ', end="")

    while (True):
        if len(current_selection_path) != 0:
            print(f'current selection:')
            print_segment_list(current_selection_path)
        user_command = input(">> ")
        clear_terminal()
        
        if user_command == "exit": 
            break
        
        elif user_command == "help":
            print(f'Commands: ')
            for i in options.keys():
                print(f'{i:10}: {options[i]}')
        
        
        elif user_command == "runs":
            display_runs()
        
        
        elif user_command == "new run": 
            run_name = input("new run name: ")
            if run_name in runs.keys(): 
                print('Invalid Input: a run with that name already exists')
            else:
                new_run_obj = Run(run_name)
                runs[run_name] = new_run_obj
                print("run created")
        
                
        elif user_command == "select":
            current_selection = Segment
            current_selection_path = []
            
            current_selection, current_selection_path = select_segment()
                
                
        elif user_command == "add split":
            add_to_current_selection = input("add split to current selection? (y/n): ")
            if add_to_current_selection == 'n':
                select_segment()
            elif add_to_current_selection == 'y':
                new_segment_name = input("name of new segment:\n")
                if new_segment_name not in current_selection.get_immediate_child_splits():
                    current_selection.add_child_split(new_segment_name)
                    print("split added")
                else:
                    print("Invalid Input: a child segment with that name already exists")
        
        
        elif user_command == "splits":
            run_name = input("name of run to display:\n")
            try: 
                run_obj = runs[run_name]
                run_obj.display_splits()
            except KeyError:
                print('Invalid Input: no run with that name exists')
        
        elif user_command == "start timer":
            current_run_name = input("name of the run to start: ")
            global current_run
            current_run = runs[current_run_name]
            current_run.start_run()
            global timer_active
            timer_active = True
            print("\n")
        
        elif user_command == "current selection":
            print(str(current_selection), current_selection_path)
        
            
        else:
            print("invalid command")

if __name__ == "__main__":     
    
    clear_terminal()

    main_thread = threading.Thread(target=main, args=())
    main_thread.start()
    
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
