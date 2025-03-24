import os
import shutil
from datetime import datetime

# Define the path to the directory containing files to be organized
source_directory = '/Users/maxwe_kpki328/Downloads/'

# Define the target directories for each file type
folders = {
    'pdf': '/Users/maxwe_kpki328/Desktop/pdfs/',
    'zip': '/Users/maxwe_kpki328/Desktop/zips/',
    'png': '/Users/maxwe_kpki328/Desktop/imgs/',
    'gif': '/Users/maxwe_kpki328/Desktop/imgs/',
    'jpg': '/Users/maxwe_kpki328/Desktop/imgs/',
    # Add more types if needed
}

folder_mapping = {
    'Maxwell Lokshin': 'Important Documents',     # Files containing 'report' in the name go to 'reports' folder
    'planet': 'Planets',   # Files containing 'invoice' in the name go to 'invoices' folder
    # 'photo': 'photos',       # Files containing 'photo' in the name go to 'photos' folder
    # Add more mappings as needed
}

# Make sure the target folders exist, if not create them
for folder in folders.values():
    if not os.path.exists(folder):
        os.makedirs(folder)

# Loop through all files in the source directory
for filename in os.listdir(source_directory):
    file_path = os.path.join(source_directory, filename)
    
    # Check if it's a file (and not a folder)
    if os.path.isfile(file_path):
        # Get the file extension
        file_extension = filename.split('.')[-1].lower()
        
        # If the extension matches a defined folder, move the file
        if file_extension in folders:
            target_path = os.path.join(folders[file_extension], filename)
            shutil.move(file_path, target_path)
            print(f'Moved {filename} to {folders[file_extension]}')

# place by name substring
# Loop through all files in the source directory
for sourceFolder in folders.values():
    for filename in os.listdir(sourceFolder):
        file_path = os.path.join(sourceFolder, filename)
        
        # Check if it's a file (and not a folder)
        if os.path.isfile(file_path):
            # Flag to check if a match is found
            moved = False
            
            # Check each substring mapping
            for substring, folder_name in folder_mapping.items():
                # If the substring is found in the filename (case insensitive)
                if substring.lower() in filename.lower():
                    target_directory = os.path.join(sourceFolder, folder_name)
                    
                    # Create the target directory if it doesn't exist
                    if not os.path.exists(target_directory):
                        os.makedirs(target_directory)
                    
                    # Define the target file path
                    target_file_path = os.path.join(target_directory, filename)
                    
                    # Move the file to the corresponding folder
                    shutil.move(file_path, target_file_path)
                    print(f'Moved {filename} to {target_directory}')
                    moved = True
                    break  # No need to check other folders once the file is moved

            # If no match is found, you can either skip or move it to a default folder
            if not moved:
                print(f'{filename} does not match any specified category and was skipped.')

# places all files according to date in their respective locations
for sourceFolder in folders.values():
    for filename in os.listdir(sourceFolder):
        file_path = os.path.join(sourceFolder, filename)

        if os.path.isfile(file_path):
            # Get the last modification time of the file
            mod_time = os.path.getmtime(file_path)
            
            # Convert modification time to a datetime object
            mod_date = datetime.fromtimestamp(mod_time)
            
            # Create a folder name based on the year (e.g., 2025)
            folder_name = mod_date.strftime('%Y')
            
            # Define the target directory based on the modification year
            target_directory = os.path.join(sourceFolder, folder_name)

            # Create the directory if it doesn't exist
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)

            # Define the target file path
            target_file_path = os.path.join(target_directory, filename)

            # Move the file to the corresponding folder
            shutil.move(file_path, target_file_path)
            print(f'Moved {filename} to {target_directory}')
    

print("Organizing files complete.")
