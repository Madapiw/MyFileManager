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
DIR_TO_WATCH = 'C:\\myData\\Scripts\\MyFileManager\\DIR_FOR_TESTS'

FILE_EXT_TO_WATCH = ['.pdf','.exe','.docx','.mp4','.mp3','.flack','.avi','.jpg','.png','.csv','.zip','.rar','.7z','.ova','.iso','ovpn','.ico','.gz','.psd','.xlsx','.torrent','.pem','.json','.odt','.md','.mlx','.bat','.txt','.tif','.raw','.py','.js','.css','.html','.xml','.c','.cpp','.php','.java','.jar','.mkv']

#TODO[X] write rest of folders to create and arrange
DIRS_TO_MOVE = {'PDF': f'{DIR_TO_WATCH}\\PDF','EXE':f'{DIR_TO_WATCH}\\EXE','DOCX': f'{DIR_TO_WATCH}\\DOCX','MP4':f'{DIR_TO_WATCH}\\MP4','MP3':f'{DIR_TO_WATCH}\\MP3','FLACK': f'{DIR_TO_WATCH}\\FLACK','AVI': f'{DIR_TO_WATCH}\\AVI','JPG': f'{DIR_TO_WATCH}\\JPG','PNG': f'{DIR_TO_WATCH}\\PNG','CSV': f'{DIR_TO_WATCH}\\CSV','ZIP': f'{DIR_TO_WATCH}\\ZIP','RAR': f'{DIR_TO_WATCH}\\RAR','7ZIP': f'{DIR_TO_WATCH}\\7ZIP','OVA': f'{DIR_TO_WATCH}\\OVA','ISO': f'{DIR_TO_WATCH}\\ISO','OVPN': f'{DIR_TO_WATCH}\\OVPN','ICO': f'{DIR_TO_WATCH}\\ICO','GZ': f'{DIR_TO_WATCH}\\TAR_GZ','PSD': f'{DIR_TO_WATCH}\\PSD','XLSX': f'{DIR_TO_WATCH}\\XLSX','TORRENT': f'{DIR_TO_WATCH}\\TORRENT','PEM': f'{DIR_TO_WATCH}\\PEM','JSON': f'{DIR_TO_WATCH}\\JSON','ODT': f'{DIR_TO_WATCH}\\ODT','MD': f'{DIR_TO_WATCH}\\MD','MLX': f'{DIR_TO_WATCH}\\MLX','BAT': f'{DIR_TO_WATCH}\\BAT','TXT': f'{DIR_TO_WATCH}\\TXT','TIF': f'{DIR_TO_WATCH}\\TIF','RAW': f'{DIR_TO_WATCH}\\RAW','PY': f'{DIR_TO_WATCH}\\PY','JS': f'{DIR_TO_WATCH}\\JS','CSS': f'{DIR_TO_WATCH}\\CSS','HTML': f'{DIR_TO_WATCH}\\HTML','XML': f'{DIR_TO_WATCH}\\XML','C': f'{DIR_TO_WATCH}\\C','C++': f'{DIR_TO_WATCH}\\C++','PHP': f'{DIR_TO_WATCH}\\PHP','JAVA': f'{DIR_TO_WATCH}\\JAVA','JAR': f'{DIR_TO_WATCH}\\JAR','MKV': f'{DIR_TO_WATCH}\\MKV','OTHER':f'{DIR_TO_WATCH}\\OTHER'}
#'': f'{DIR_TO_WATCH}\\'   for faster coping    

def watchMyFiles():

    if not os.path.exists(DIR_TO_WATCH):
        sys.exit("Directory does not exist.")

    filesInDir = os.listdir(DIR_TO_WATCH)
    #TODO [ ] moving folders to DOWNLOADED_FOLDERS with everything in them
    for file in filesInDir:
        for fileExt in FILE_EXT_TO_WATCH:
            if not (file.endswith(fileExt) or file.endswith(fileExt.upper())):
                if not os.path.exists(f'{DIR_TO_WATCH}\\OTHER'):
                    print(f'Creating dir: OTHER')
                    os.mkdir(f'{DIR_TO_WATCH}\\OTHER')

                shutil.move(f'{DIR_TO_WATCH}\\{file}',f'{DIR_TO_WATCH}\\OTHER\\{file}')
                print(f'{file} ----> OTHER folder')

            elif file.endswith(fileExt) or file.endswith(fileExt.upper()):
                #TODO [ ] add exeption if file in folder already exists 
                if os.path.exists(f'{DIR_TO_WATCH}\\{fileExt.split(".")[1].upper()}'):
                    shutil.move(f'{DIR_TO_WATCH}\\{file}',f'{DIR_TO_WATCH}\\{fileExt.split(".")[1].upper()}\\{file}')
                    print(f'{file} ----> {fileExt.split(".")[1].upper()} folder')
                elif os.path.exists(f'{DIR_TO_WATCH}\\{fileExt.split(".")[1].upper()}') == False:
                    print(f'Creating dir: {fileExt.split(".")[1].upper()}')
                    os.mkdir(f'{DIR_TO_WATCH}\\{fileExt.split(".")[1].upper()}')
                    shutil.move(f'{DIR_TO_WATCH}\\{file}',f'{DIR_TO_WATCH}\\{fileExt.split(".")[1].upper()}\\{file}')
                    print(f'{file} ----> {fileExt.split(".")[1].upper()} folder')    
                else:
                    print(f"Couldn't transfer {file} file to it's folder")  
            

def settingUp():
    print("Settings:")



if __name__ == '__main__':
    try:
       watchMyFiles()
    except KeyboardInterrupt:
        sys.exit("Keyboard interruption, stopping.")
    
