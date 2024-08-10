import os
import importlib.util
from core.base import BaseModule

MODULE_DIR = os.path.join(os.path.dirname(__file__), '../modules')

def load_modules():
    modules = []
    for filename in os.listdir(MODULE_DIR):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            module_path = os.path.join(MODULE_DIR, filename)
            
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            for attr in dir(module):
                if attr.endswith('Module'):
                    cls = getattr(module, attr)
                    if issubclass(cls, BaseModule) and cls is not BaseModule:
                        # Instantiate the module class and add to the list
                        modules.append(cls())
    return modules

def get_all_modules():
    return load_modules()
