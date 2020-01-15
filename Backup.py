#!/user/bin/env python3

import Constants

import datetime
import os
import shutil


def main():
    create_backupper_folder()
    if(not did_update_today()):
        update_directory = create_update_directory()
        create_update(update_directory)


def create_backupper_folder():
    if(os.path.isdir(Constants.DEST_FOLDER)):
        print("The Backupper folder exist.")
        return True
    else:
        os.mkdir(Constants.DEST_FOLDER)


def did_update_today():
    dest_folder_list = os.listdir(Constants.DEST_FOLDER)
    for folder in dest_folder_list:
        if(str(datetime.date.today()) in folder):
            print(Constants.OUTPUT_FOLDER_EXIST)
            return True
        else:
            print("Starting update...")
            return False


def create_update_directory():
    update_directory = Constants.DEST_FOLDER + \
        Constants.NEW_UPDATE_FOLDER + str(datetime.date.today())
    if(os.path.isdir(update_directory)):
        print(Constants.OUTPUT_FOLDER_EXIST)
    return update_directory


def create_update(update_directory):
    shutil.copytree(src=Constants.SRC_FOLDER,
                    dst=update_directory)


main()
