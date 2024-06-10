import os
import shutil

from copy_dir_contents import copy_dir_contentents
from generate_page import generate_page

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

    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )


main()
