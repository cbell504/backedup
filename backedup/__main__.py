#!/usr/bin/env python3

from backedup import Constants
from backedup import Backup

import datetime
import json
import logging
import os

def main():
    logging.basicConfig(filename='backedup.log', level=logging.INFO)
    json_configs = get_config_json_file()
    backup = Backup(json_configs)
    backup.create_backedup_folder()
    if not backup.did_backup_today():
        backup_directory = create_backup_directory()
        backup.start_backup(backup_directory)
        print(Constants.DONE)

def get_config_json_file(self):
    """
        get_config_json_file

        - Gets the config JSON file and returns the output
    """
    logging.info("Current directory: " + os.getcwd())
    logging.info("Loading JSON config file.")
    with open(Constants.CONFIG_LOCATION, 'r') as file:
        return json.load(file)

def create_backup_directory():
    """
        create_backup_directory
    """
    backup_directory = Constants.DEST_FOLDER + \
        Constants.NEW_UPDATE_FOLDER + str(datetime.date.today())
    if os.path.isdir(backup_directory):
        print(Constants.OUTPUT_FOLDER_EXIST)
    return backup_directory

if __name__ == "__main__":
    main()
