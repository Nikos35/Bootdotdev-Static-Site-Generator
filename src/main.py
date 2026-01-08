from copystatic import copy_files_recursive, clear_directory

from generate_page import generate_pages_recursive

import sys

def main():
    basepath = "/"
    if len(sys.argv) == 0:
        basepath = sys.argv[0]
    

    clear_directory("docs")
    copy_files_recursive("static", "docs")

    generate_pages_recursive("content/", "template.html", "docs/", basepath)



if __name__ == "__main__":
    main()
