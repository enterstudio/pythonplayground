import os


def rename_files():
    dir = "/Users/infotechtestmac/sites/pythonplayground/prank_after"
    saved_path = os.getcwd()
    file_list = os.listdir(dir)
    os.chdir(dir)

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print "File named " + file_name + " has been renamed to " + file_name.translate(None, "0123456789")

    os.chdir(saved_path)

rename_files()