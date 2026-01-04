import shutil
import os

def copy_files_recursive(source, destination):
    if not os.path.exists(source):
        raise FileNotFoundError("Error copying: source path not found")
    files = os.listdir(source)

    for file in files:
        file_path = os.path.join(source, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, destination)
        else:
            os.mkdir(os.path.join(destination, file))
            copy_files_recursive(file_path, os.path.join(destination, file))
        


def clear_directory(path):
    if os.path.exists(path):
        shutil.rmtree(path)        
    else:
        print(f"Clearing directory '{path}': directory '{path}' not found. Creating it.")
    
    os.mkdir(path)
