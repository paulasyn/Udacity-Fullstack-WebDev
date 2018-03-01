import os
import string

def rename_files():
#  get filenames from folder
    file_list = os.listdir(r"/Users/paulasyn/Desktop/Udacity-Fullstack-WebDev/1 - Python Foundation /Secret Message/prank")
    print(file_list)
    translist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    translation_table = str.maketrans("0123456789", "          ")
    saved_path = os.getcwd()
    os.chdir((r"/Users/paulasyn/Desktop/Udacity-Fullstack-WebDev/1 - Python Foundation /Secret Message/prank"))
#  find all filenames in file, need path
    for file_name in file_list:
        os.rename(file_name, file_name.translate(translation_table))
        print(file_name)
    os.chdir(saved_path)


rename_files()