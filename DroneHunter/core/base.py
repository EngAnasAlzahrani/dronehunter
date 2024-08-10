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
        print("\nModule options:")
        for name, (value, required, desc) in self.options.items():
            print(f"{name: <20} {value: <15} {required: <10} {desc}")
        print()
    
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
