import os
import shutil


# comment
def copy_dir_contentents(source_dir_path, dest_dir_path):
    # create the dest dir if it does not exist
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for item in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, item)
        dest_path = os.path.join(dest_dir_path, item)
        print(f" - {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            # copy the file
            shutil.copy(from_path, dest_path)
        else:
            # new directory to copy from
            copy_dir_contentents(from_path, dest_path)
    return None
