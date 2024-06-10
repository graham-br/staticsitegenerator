import os
import shutil

from copy_dir_contents import copy_dir_contentents
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
template_path = "./template.html"
dir_path_content = "./content"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_dir_contentents(dir_path_static, dir_path_public)

    generate_pages_recursive(dir_path_content, template_path, dir_path_public)


main()
