'''
            -- Algorithm --

    1) Start
    2) Input directory absolute path
    3) Find directory
    4) IF step 3 is true then
        4.1) Check is not Empty
        4.2) IF 4.1 step is true
            4.2.1) Extract files extention
            4.2.2) Create directory for diffrent file extention
            4.2.3) Move file to same type directory
            4.2.4) Output successful message on console
        4.3) IF 4.1 step is false
            4.3.1) Output "Directory is empty"
    5) IF step 3 is false
        5.1) Output "Directory not found"
        5.1) Go to step 2
    6) End

'''

import os
import shutil
import pathlib

# Global Variable
target_dir = ''

# Input directory path from user
def input_dir():
    target_dir = input("Enter Absolute Directory Path : ").strip()
    return target_dir

# Check directory existing and get file names
def find_files():
    while True:
        global target_dir
        target_dir = input_dir()
        try:
            with os.scandir(target_dir) as directory:
                files = [i.name for i in directory if os.path.isfile(target_dir + '/' + i.name)]
                print("Your Files : ", files)
                if files != '':
                    return files
        except:
            print(f"No such directory: '{target_dir}'\nPlease Enter valid path. For exit program press (CTRL + C)")

# Get file extention
def extention(file):
    file_ext = pathlib.Path(file).suffix
    return file_ext.lower()

# Check program support extention or not
def isSupport(file_extention, extention_list):
    supportOrNot = []
    for extention in extention_list:
        if file_extention in extention:
            supportOrNot.append(True)
        else:
            supportOrNot.append(False)
    return supportOrNot

# File move to same type directory
def move_file(file, type=''):
    try:
        from_path = target_dir + '/' + file
        if type != '':
            to_path = target_dir + '/' + type
            if not os.path.exists(to_path):
                os.mkdir(to_path)
            shutil.move(from_path, to_path + '/' + file)
        else:
            to_path = target_dir + '/Other'
            if not os.path.exists(to_path):
                os.mkdir(to_path)
            shutil.move(from_path, to_path + '/' + file)

    except:
        print("Program Error")
        print("Please Try Again.\n If still not working then report problem to Developer")

# Main function
if __name__ == "__main__":
    # Supported file type and extention
    # You can add more file type and extention
    # Like this format >>> 'type': ['.extention1', .extention2]
    type_and_extention = {
        'Audio': ['.mp3'],
        'Video': ['.mp4', '.mkv', '.webm'],
        'Photo': ['.jpg', 'png'],
        'Ebook': ['.pdf'],
        'Text': ['.txt'],
        'Font': ['.otf'],
        'HTML': ['.html'],
        'Css': ['.css'],
        'Python': ['.py'],
        'PHP': ['.php'],
        'Test': ['.t1', '.t2', '.t3']
    }

    type_list = list(type_and_extention.keys())
    extention_list = list(type_and_extention.values())

    files = find_files()
    for file in files:
        file_extention = extention(file)
        if any(isSupport(file_extention, extention_list)):
            type = type_list[isSupport(file_extention, extention_list).index(True)]
            move_file(file, type)
        else:
            move_file(file)

    print("Successfully File Moved\nThanks for using my program")