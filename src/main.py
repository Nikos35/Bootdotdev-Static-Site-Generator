from copystatic import copy_files_recursive, clear_directory

from generate_page import generate_pages_recursive

import sys

def main():
    basepath = sys.argv[0]
    



    clear_directory("public")
    copy_files_recursive("static", "public")

    generate_pages_recursive("content/", "template.html", "docs/", basepath)



if __name__ == "__main__":
    main()
