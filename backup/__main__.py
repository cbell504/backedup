#!/usr/bin/env python3

import Constants

import datetime
import logging
import os
import shutil


def main():
    create_backupper_folder()
    if(not did_backup_today()):
        backup_directory = create_backup_directory()
        create_backup(backup_directory)
        print(Constants.DONE)


def create_backupper_folder():
    if(os.path.isdir(Constants.DEST_FOLDER)):
        print(Constants.FOLDER_EXIST)
        return True
    else:
        os.mkdir(Constants.DEST_FOLDER)


def did_backup_today():
    dest_folder_list = os.listdir(Constants.DEST_FOLDER)
    for folder in dest_folder_list:
        if(str(datetime.date.today()) in folder):
            print(Constants.OUTPUT_FOLDER_EXIST)
            return True
        else:
            print(Constants.STARTING_UPDATE)
            return False


def create_backup(backup_directory):
    shutil.copytree(src=Constants.SRC_FOLDER,
                    dst=backup_directory,
                    ignore=logpath)


def create_backup_directory():
    backup_directory = Constants.DEST_FOLDER + \
        Constants.NEW_UPDATE_FOLDER + str(datetime.date.today())
    if(os.path.isdir(backup_directory)):
        print(Constants.OUTPUT_FOLDER_EXIST)
    return backup_directory


def logpath(path, names):
    logging.info('Working in %s' % path)
    return []


if __name__ == "__main__":
    main()
