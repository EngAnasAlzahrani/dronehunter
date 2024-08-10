# core/base.py
class BaseModule:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category
        self.options = {}  # To store module options
    
    def set_option(self, name, value):
        self.options[name] = value
    
    def show_options(self):
        for name, option in self.options.items():
            if len(option) == 3:
                value, required, desc = option
                print(f"{name} (Required: {required}): {value} - {desc}")
            else:
                print(f"Error: Incorrect number of values for option {name}")
    
    def run(self):
        raise NotImplementedError("You must implement the 'run' method.")

class CommandLine:
    @staticmethod
    def print_banner():
        print("""
       
         _____                       _    _             _            
 |  __ \                     | |  | |           | |           
 | |  | |_ __ ___  _ __   ___| |__| |_   _ _ __ | |_ ___ _ __ 
 | |  | | '__/ _ \| '_ \ / _ \  __  | | | | '_ \| __/ _ \ '__|
 | |__| | | | (_) | | | |  __/ |  | | |_| | | | | ||  __/ |   
 |_____/|_|  \___/|_| |_|\___|_|  |_|\__,_|_| |_|\__\___|_|   
                                                              
                                                              
        
        """)
        print("DroneHunter Framework - Drone Exploitation Toolkit\n")
        
    @staticmethod
    def list_modules(modules):
        print("\nAvailable Modules:")
        for module in modules:
            print(f"{module.name}: {module.description}")
        print()
