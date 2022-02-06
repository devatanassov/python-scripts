#!/usr/bin/python

from genericpath import isdir
from os import listdir, rename
from os.path import isfile, join, getctime, splitext, dirname
from datetime import datetime
import re
import argparse

def browse_dir(path, regEx, files = []):
    for file in listdir(path):
      file_candidate = join(path, file);
      if isdir(file_candidate) and file != ".git": #lame
        browse_dir(file_candidate, regEx, files)
        continue
      if isfile(file_candidate) and bool(re.search(regEx, file)):
        files.append(file_candidate)
    
def rename_files(path_to_file, regEx):
    files = []
    browse_dir(path_to_file, regEx, files)
    for file in files:
        try:
            new_file_name = datetime.fromtimestamp(getctime(file)).strftime("%Y_%m_%d_%H_%m_%s")
            extention = splitext(file)[1]
            file_path = dirname(file)
            rename(file, join(file_path, new_file_name+extention))
        except FileExistsError:
            print('File already exist '+new_file_name)
            continue

try:
    # Construct the argument parser
    ap = argparse.ArgumentParser()

    # Add the arguments to the parser
    ap.add_argument("-d", "--dir", required=True,
    help="Path to root folder")
    ap.add_argument("-r", "--regex", required=True,
    help="Filter out by regex")
    args = vars(ap.parse_args())
    path = args['dir']
    regEx = args['regex']
except IndexError:
    print('Path or regEx is not provided')
else:
    rename_files(path, regEx)


