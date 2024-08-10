from core.base import CommandLine
from core.module import get_all_modules

def search_modules(modules, query):
    matches = [mod for mod in modules if query.lower() in mod.name.lower()]
    return matches


def start_cli():
    CommandLine.print_banner()
    modules = get_all_modules()

    if not modules:
        print("No modules found.")
        return

    selected_module = None

    while True:
        command = input("DroneHunter > ").strip().lower()
        if command == "exit":
            print("Exiting DroneHunter...")
            break
        elif command == "help":
            print("Commands: search <query>, use <index|name>, show options, set <option> <value>, exploit")
        elif command.startswith("search "):
            query = command[7:]
            matches = search_modules(modules, query)
            print("Matching Modules")
            print("================")
            if matches:
                for i, mod in enumerate(matches):
                    print(f"{i}  {mod.name}  {mod.description}")
            else:
                print("No matching modules found.")
        elif command.startswith("use "):
            identifier = command[4:]
            if identifier.isdigit():
                index = int(identifier)
                if 0 <= index < len(modules):
                    selected_module = modules[index]
                    print(f"Using module: {selected_module.name}")
                else:
                    print("Invalid module index.")
            else:
                selected_module = next((mod for mod in modules if mod.name == identifier), None)
                if selected_module:
                    print(f"Using module: {selected_module.name}")
                else:
                    print("Module not found.")
        elif command == "show options":
            if selected_module:
                selected_module.show_options()
            else:
                print("No module selected.")
        elif command.startswith("set "):
            if selected_module:
                parts = command[4:].split(" ", 1)
                if len(parts) == 2:
                    option, value = parts
                    selected_module.set_option(option, value)
                    print(f"Set {option} to {value}")
                else:
                    print("Invalid command format. Use: set <option> <value>")
            else:
                print("No module selected.")
        elif command == "exploit":
            if selected_module:
                selected_module.run()
            else:
                print("No module selected.")
        else:
            print(f"Unknown command: {command}")
