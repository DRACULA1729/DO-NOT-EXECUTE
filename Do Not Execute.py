import os

current_dir = os.path.dirname(os.path.abspath(__file__))
files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]

for i, file in enumerate(files):
      
        print(f'Deleting {i}th file ',file,'...........................')
        try:
            os.remove(os.path.join(current_dir, file))
        except OSError as e:
            print(f"Error deleting file {file}: {e}")

print("Deleted every other file in the folder!")
