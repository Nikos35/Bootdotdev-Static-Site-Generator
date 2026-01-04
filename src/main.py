from copystatic import copy_files_recursive, clear_directory

def main():
    clear_directory("public")

    copy_files_recursive("static", "public")






if __name__ == "__main__":
    main()
