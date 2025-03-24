import os
import shutil
from collections import defaultdict

def organize_files(directory, location):
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return
    
    codeC = os.path.join(location, "CSS")
    
    # Move all files to root directory
    for root, dirs, files in os.walk(directory, topdown=False):
        print(root)
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.abspath(file_path) == os.path.abspath(__file__):
                continue  # Skip the script itself
            

            # Determine category
            file_ext = os.path.splitext(file)[1].lower()
            # print(file_path, "TYPE: ", file_ext)
            if file_ext == '.css' or file_ext == 'css':
                os.makedirs(codeC, exist_ok=True)
                shutil.move(file_path, os.path.join(codeC, file))
    
    print("Files organized successfully!")

# Usage
directory_to_organize = os.path.expanduser("~/Desktop/Code")  # Change this path
location_to_organize = os.path.expanduser("~/Desktop/Code")
organize_files(directory_to_organize, location_to_organize)
