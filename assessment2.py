import os
import zipfile
import sys

def zip_directory(folder_path):
    """
    Zips the entire contents of a folder (including subdirectories).
    
    :param folder_path: The path to the folder to zip.
    """
    # Check if the folder path is valid
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return
    
    # Determine the name of the zip file
    zip_filename = f"{os.path.basename(folder_path)}.zip"
    zip_filepath = os.path.join(os.path.dirname(folder_path), zip_filename)
    
    try:
        # Open a zip file in write mode
        with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through the directory and add files to the zip file
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    # Get the full file path
                    file_path = os.path.join(root, file)
                    
                    # Add the file to the zip file, preserving the folder structure
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, arcname)
                    
                    print(f"Adding {file_path} as {arcname}")
                    
        print(f"Successfully created {zip_filepath}")
    
    except PermissionError:
        print(f"Error: Permission denied when accessing '{folder_path}' or files inside it.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_folder_path():
    """
    Prompt the user for the folder path and validate it.
    
    :return: A valid folder path.
    """
    folder_path = input("Please enter the path to the folder you want to zip: ").strip()
    
    # Check if the input path exists and is a directory
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        sys.exit(1)
    
    return folder_path

if __name__ == "__main__":
    folder_path = get_folder_path()
    zip_directory(folder_path)
