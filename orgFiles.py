import os
import shutil
from collections import defaultdict

def organize_files(directory, location):
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return
    if not os.path.exists(location):
        print("Directory does not exist!")
        return
    
    # File categories
    categories = {
        "Code": {".py", ".cpp", ".java", ".js", ".html", ".css", ".cs", ".c"},
        "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"},
        "Documents": {".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"},
        "Extras": set()
    }
    
    # Create category folders
    for category in categories.keys():
        os.makedirs(os.path.join(location, category), exist_ok=True)
    
    # Move all files to root directory
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.abspath(file_path) == os.path.abspath(__file__):
                continue  # Skip the script itself
            
            # Determine category
            file_ext = os.path.splitext(file)[1].lower()
            moved = False
            for category, extensions in categories.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(location, category, file))
                    moved = True
                    break
            
            if not moved:  # If file doesn't match any category, move to Extras
                shutil.move(file_path, os.path.join(location, "Extras", file))
        
        # Remove empty folders
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
    
    print("Files organized successfully!")


#     # Sort files by keywords
#     for category in categories.keys():
#         sort_files_by_keywords(os.path.join(directory, category))

# def sort_files_by_keywords(directory):
#     if not os.path.exists(directory):
#         return
    
#     file_groups = defaultdict(list)
    
#     for file in os.listdir(directory):
#         file_path = os.path.join(directory, file)
#         if os.path.isfile(file_path):
#             file_name, _ = os.path.splitext(file)
#             keywords = file_name.split('_')  # Splitting based on underscores as an example
#             primary_keyword = keywords[0] if keywords else "Misc"
#             file_groups[primary_keyword].append(file_path)
    
#     for keyword, files in file_groups.items():
#         keyword_dir = os.path.join(directory, keyword)
#         os.makedirs(keyword_dir, exist_ok=True)
#         for file_path in files:
#             shutil.move(file_path, os.path.join(keyword_dir, os.path.basename(file_path)))
    
#     print(f"Files in {directory} sorted by keywords!")

# Usage
directory_to_organize = os.path.expanduser("~/Desktop")  # Change this path
location_to_organize = os.path.expanduser("~/Desktop")
organize_files(directory_to_organize, location_to_organize)
