from os import listdir, path, curdir, sep
from re import search
import argparse


def generate_playlist_by_path(directory):
    if path.isdir(directory):
      # define m3u file based on directory name;
      # print(path.split(directory)[0])
      try: 
        m3uFileName = path.join(directory, path.split(directory)[1] + ".m3u")
        m3u = open(m3uFileName, "w")
        for file in listdir(directory):
            pathToFile = path.join(directory, file)
            if path.isdir(pathToFile):
                
                generate_playlist_by_path(pathToFile)
                continue

            # add file paths to playlist data
            # print(file, bool(file.lower().endswith(('.mp3', '.mp4', '.avi'))))
            if bool(file.lower().endswith(('.mp3', '.mp4', '.avi'))):
                m3u.write(file + "\n")
        m3u.close()
      except PermissionError:
        print('SKIPPED: ' + directory + ' - Do not have permissions to write')
      else:
        print('SUCCESS: ' + m3uFileName + ' have been generated in ' + directory)
    else:
        print('Error: ' + directory + 'is not a dir')

if __name__ == '__main__':
    try:
        # Construct the argument parser
        ap = argparse.ArgumentParser()

        # Add the arguments to the parser
        ap.add_argument("-d", "--dir", required=True,
        help="Path to root folder")
        args = vars(ap.parse_args())
        dir = args['dir']
    except IndexError:
        print('Path or regEx is not provided')
    else:
        generate_playlist_by_path(dir if dir.endswith(sep) else dir[':-1'])

    

    