import time
import sys
import os
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import LoggingEventHandler

#DIR_TO_WATCH = 'C:\\Users\\$USER$\\Downloads'

#DIR FOR TESTS
DIR_TO_WATCH = 'C:\\Data\\scripts\\MyFileMenager\\DIR_FOR_TESTS'

FILE_EXT_TO_WATCH = ['.pdf','.exe','.docx','.mp4','.mp3','.flack','avi','.jpg','.png','.csv','.zip','.rar','.7z','.ova','.iso','ovpn','.ico','.tar.gz','.psd','.xlsx','.torrent','.pem','.json','.odt','.md','.mlx','.bat','.txt','.tif','.raw','.py','.js','.css','.html','.xml','.c','.cpp','.php','.java','.jar']

# TODO[ ] write rest of folders to create and arrange
DIRS_TO_MOVE = {'PDF': f'{DIR_TO_WATCH}\\PDF','EXE':f'{DIR_TO_WATCH}\\EXE','DOCX': f'{DIR_TO_WATCH}\\DOCX','MP4':f'{DIR_TO_WATCH}\\MP4','MP3':f'{DIR_TO_WATCH}\\MP3'}
#'': f'{DIR_TO_WATCH}\\'   for faster coping    
zmiana
def watchMyFiles():
    try:
        os.path.exists(DIR_TO_WATCH)
    except Exception:
        assert Exception("Directory does not exist.")

    #check if DIRS EXIST if not create folder 
    for value in DIRS_TO_MOVE.values():
        if not (os.path.exists(value)):
                print(f"Creating dir: {value}")
                os.mkdir(value) 
    #TODO [ ] moveing folders to DOWNLOADED_FOLDERS with everything in them
    filesInDir = os.listdir(DIR_TO_WATCH)
    for file in filesInDir:
        for fileExt in FILE_EXT_TO_WATCH:
            if file.endswith(fileExt) or file.endswith(fileExt.upper()):
                #TODO [ ] add exeption if file in folder already exists
                if not os.path.exists(f'{DIR_TO_WATCH}\\{fileExt.split(".")[1].upper()}\\{file}'):
                    shutil.move(f'{DIR_TO_WATCH}\\{file}',f'{DIR_TO_WATCH}\\{fileExt.split(".")[1].upper()}\\{file}')
                    print(f'{file} moved to {fileExt.split(".")[1].upper()} folder')
                    
                    
if __name__ == '__main__':
    try:
       watchMyFiles()
    except KeyboardInterrupt:
        sys.exit("Keyboard interruption, stopping.")
    
