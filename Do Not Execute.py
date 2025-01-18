import os
import shutil

current_dir = os.path.dirname(os.path.abspath(__file__))

for item in os.listdir(current_dir):
    item_path = os.path.join(current_dir, item)
    
    if os.path.isfile(item_path):
        print(f'Deleting file {item}...')
        try:
            os.remove(item_path)
        except OSError as e:
            print(f"Error deleting file {item}: {e}")
    elif os.path.isdir(item_path):
        print(f'Deleting directory {item}...')
        try:
            shutil.rmtree(item_path)
        except OSError as e:
            print(f"Error deleting directory {item}: {e}")
    else:
        print(f'Deleting {item}...')
        try:
            os.remove(item_path) 
        except OSError as e:
            print(f"Error deleting {item}: {e}")

print("Deleted all files and folders in the folder!")
