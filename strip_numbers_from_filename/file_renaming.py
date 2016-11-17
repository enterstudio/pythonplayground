import os


def rename_files():
    root_dir = os.getcwd()
    files_dir = root_dir + "/prank"
    file_list = os.listdir(files_dir)
    os.chdir(files_dir)

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print "The file named " \
              + file_name \
              + " has been renamed to " \
              + file_name.translate(None, "0123456789")

    os.chdir(root_dir)

rename_files()