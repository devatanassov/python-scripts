#!/usr/bin/python

import sys
from os import listdir
from os.path import isfile, join
import re

def rename_files(path, regEx):
    files = []
    for file in listdir(path):
      if isfile(file) and bool(re.match(regEx, file)):
        files.append(file)
    print(files)
    # onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    


print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

try:
    path = sys.argv[1]
    regEx = sys.argv[2]
except IndexError:
    print('Path or regEx is not provided')
else:
    rename_files(path, regEx)


