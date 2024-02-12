import os
import shutil

# Define source and destination directories
from_dir = "path_to_downloads_folder"  # Update with actual path to Downloads folder
to_dir = "path_to_document_files_folder"  # Update with actual path to Document_Files folder

# Get list of files in the source directory
list_of_files = os.listdir(from_dir)

# Print the list of files
print("Files in the Downloads folder:")
for file in list_of_files:
    print(file)

# Move files to the Document_Files folder
for file in list_of_files:
    # Split the file name and extension
    filename, file_extension = os.path.splitext(file)
    
    # Check if the file is a document file (you can add more file extensions as needed)
    if file_extension in ['.pdf', '.doc', '.docx', '.txt']:
        # Construct source and destination paths
        src_path = os.path.join(from_dir, file)
        dest_path = os.path.join(to_dir, file)
        
        # Move the file to the Document_Files folder
        shutil.move(src_path, dest_path)
        print(f"Moved {file} to Document_Files folder.")
