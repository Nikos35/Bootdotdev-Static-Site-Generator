from copystatic import copy_files_recursive, clear_directory

from generate_page import generate_pages_recursive
def main():
    clear_directory("public")
    copy_files_recursive("static", "public")

    generate_pages_recursive("content/", "template.html", "public/")



if __name__ == "__main__":
    main()
