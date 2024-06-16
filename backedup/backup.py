#!/usr/bin/env python3

from backedup import Constants

import datetime
import logging
import os
import shutil

class Backup:

    def __init__(self, configs):
        self.config = configs
        self.destination_folder = self.config["destFolder"]
        self.source_folder = self.config["srcFolder"]

    def create_backedup_folder(self):
        """
            create_backedup_folder

        """
        if os.path.isdir(self.destination_folder):
            logging.info("Destionation folder does exist. Continuing forward with backup.")
            return True
        else:
            logging.info("Destionation folder does not exist.")
            logging.info("Creating destionation folder for backup.")
            os.mkdir(self.destination_folder)

    def create_source_folder(self):
        pass

    def did_backup_today(self):
        """
            did_backup_today
        """
        dest_folder_list = os.listdir(self.destination_folder)
        for folder in dest_folder_list:
            if str(datetime.date.today()) in folder:
                print(Constants.OUTPUT_FOLDER_EXIST)
                return True
            else:
                print(Constants.STARTING_UPDATE)
                return False
    
    def start_backup(self, backup_directory):
        """
            start_backup
        """
        shutil.copytree(src=Constants.SRC_FOLDER,
                        dst=backup_directory,
                        ignore=self._logpath)
    
    def _logpath(self, path, names):
        logging.info('Copying %s' % path)
        return []

    