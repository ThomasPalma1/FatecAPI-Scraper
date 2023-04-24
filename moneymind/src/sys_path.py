import os
import sys

def setup_sys_path():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(os.path.join(current_dir, 'src'))
    sys.path.append(os.path.join(current_dir, 'src/insert'))

setup_sys_path()
