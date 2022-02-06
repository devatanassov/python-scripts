#!/usr/bin/python

from genericpath import isdir
import sys
from os import listdir
from os.path import isfile, join, sep
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
    
def rename_files(path, regEx):
    files = []
    browse_dir(path, regEx, files)
    print(files)

try:
    # Construct the argument parser
    ap = argparse.ArgumentParser()

    # Add the arguments to the parser
    ap.add_argument("-d", "--dir", required=True,
    help="Default is current folder")
    ap.add_argument("-r", "--regex", required=True,
    help="Default is *")
    args = vars(ap.parse_args())
    path = args['dir']
    regEx = args['regex']
except IndexError:
    print('Path or regEx is not provided')
else:
    rename_files(path, regEx)


