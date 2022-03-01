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
DIR_TO_WATCH = 'C:\\Users\\madap\\Documents\\myData\\Scripts\\MyFileMenager\\DIR_FOR_TESTS'

FILE_EXT_TO_WATCH = ['.pdf','.exe','.docx','.mp4','.mp3','.flack','.avi','.jpg','.png','.csv','.zip','.rar','.7z','.ova','.iso','ovpn','.ico','.tar.gz','.psd','.xlsx','.torrent','.pem','.json','.odt','.md','.mlx','.bat','.txt','.tif','.raw','.py','.js','.css','.html','.xml','.c','.cpp','.php','.java','.jar']

#TODO[X] write rest of folders to create and arrange
DIRS_TO_MOVE = {'PDF': f'{DIR_TO_WATCH}\\PDF','EXE':f'{DIR_TO_WATCH}\\EXE','DOCX': f'{DIR_TO_WATCH}\\DOCX','MP4':f'{DIR_TO_WATCH}\\MP4','MP3':f'{DIR_TO_WATCH}\\MP3','FLACK': f'{DIR_TO_WATCH}\\FLACK','AVI': f'{DIR_TO_WATCH}\\AVI','JPG': f'{DIR_TO_WATCH}\\JPG','PNG': f'{DIR_TO_WATCH}\\PNG','CSV': f'{DIR_TO_WATCH}\\CSV','ZIP': f'{DIR_TO_WATCH}\\ZIP','RAR': f'{DIR_TO_WATCH}\\RAR','7ZIP': f'{DIR_TO_WATCH}\\7ZIP','OVA': f'{DIR_TO_WATCH}\\OVA','ISO': f'{DIR_TO_WATCH}\\ISO','OVPN': f'{DIR_TO_WATCH}\\OVPN','ICO': f'{DIR_TO_WATCH}\\ICO','TAR_GZ': f'{DIR_TO_WATCH}\\TAR_GZ','PSD': f'{DIR_TO_WATCH}\\PSD','XLSX': f'{DIR_TO_WATCH}\\XLSX','TORRENT': f'{DIR_TO_WATCH}\\TORRENT','PEM': f'{DIR_TO_WATCH}\\PEM','JSON': f'{DIR_TO_WATCH}\\JSON','ODT': f'{DIR_TO_WATCH}\\ODT','MD': f'{DIR_TO_WATCH}\\MD','MLX': f'{DIR_TO_WATCH}\\MLX','BAT': f'{DIR_TO_WATCH}\\BAT','TXT': f'{DIR_TO_WATCH}\\TXT','TIF': f'{DIR_TO_WATCH}\\TIF','RAW': f'{DIR_TO_WATCH}\\RAW','PY': f'{DIR_TO_WATCH}\\PY','JS': f'{DIR_TO_WATCH}\\JS','CSS': f'{DIR_TO_WATCH}\\CSS','HTML': f'{DIR_TO_WATCH}\\HTML','XML': f'{DIR_TO_WATCH}\\XML','C': f'{DIR_TO_WATCH}\\C','C++': f'{DIR_TO_WATCH}\\C++','PHP': f'{DIR_TO_WATCH}\\PHP','JAVA': f'{DIR_TO_WATCH}\\JAVA','JAR': f'{DIR_TO_WATCH}\\JAR'}
#'': f'{DIR_TO_WATCH}\\'   for faster coping    

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
#TODO [] create folders only when extension is detected and at least one file exists                 
                    
if __name__ == '__main__':
    try:
       watchMyFiles()
    except KeyboardInterrupt:
        sys.exit("Keyboard interruption, stopping.")
    
