from Run import Run

if __name__ == "__main__": 
    user_command = None
    runs = {}
      
    while (True): 
        user_command = input("enter a command (new run, add split, display split, exit)\n")
        if (user_command == "exit"): 
            break
        elif (user_command == "new run"): 
            name = input("new run name: \n")
            runs[name] = Run(name)
            print("run created")
        elif (user_command == "add split"):
            run_name = input("name of run to add to:\n")
            segment_name = input("name of split to add:\n")
            run_obj = runs[run_name]
            if run_obj and isinstance(run_obj, Run):
                run_obj.add_split(segment_name)
                print("split added")
            else:
                print("invlid input")
        elif (user_command == "display splits"):
            run_name = input("name of run to display:\n")
            run_obj = runs[run_name]
            if run_obj and isinstance(run_obj, Run):
                run_obj.display_splits()
            else:
                print("invlid input")