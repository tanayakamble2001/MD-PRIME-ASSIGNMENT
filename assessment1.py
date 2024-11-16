import os

def rename_folder_files(folder_path, reverse=False):
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f"Error: The folder '{folder_path}' does not exist.")
            return

        # List all files in the folder (ignoring directories)
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
        # If the folder is empty, exit
        if not files:
            print("The folder is empty. No files to rename.")
            return
        
        # Sort files alphabetically
        files.sort(reverse=reverse)

        # Start renaming files
        print("Renaming files...")
        for idx, file in enumerate(files, start=1):
            file_path = os.path.join(folder_path, file)
            file_extension = os.path.splitext(file)[1]
            new_file_name = f"{idx}{file_extension}"
            new_file_path = os.path.join(folder_path, new_file_name)

            # Attempt to rename the file
            try:
                os.rename(file_path, new_file_path)
                print(f"File '{file}' renamed to '{new_file_name}'")
            except PermissionError:
                print(f"Error: Unable to rename file '{file}' due to permission issues.")
            except Exception as e:
                print(f"Error: Could not rename file '{file}'. {e}")

        print("Renaming completed.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program
def main():
    folder_path = input("Enter the path to the folder: ")
    rename_folder_files(folder_path)

if __name__ == "__main__":
    main()
