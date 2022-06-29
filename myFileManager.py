import sys
import os
import shutil
import time

#DIR FOR TESTS
DIR_TO_WATCH = os.getcwd()

FILE_EXT_TO_WATCH = ['.pdf','.exe','.docx','.mp4','.mp3','.flack','.avi','.jpg','.png','.csv','.zip','.rar','.7z','.ova','.iso','ovpn','.ico','.gz','.psd','.xlsx','.torrent','.pem','.json','.odt','.md','.mlx','.bat','.txt','.tif','.raw','.py','.js','.css','.html','.xml','.c','.cpp','.php','.java','.jar','.mkv']

#TODO[X] write rest of folders to create and arrange
DIRS_TO_MOVE = {'PDF': f'{DIR_TO_WATCH}\\PDF','EXE':f'{DIR_TO_WATCH}\\EXE','DOCX': f'{DIR_TO_WATCH}\\DOCX','MP4':f'{DIR_TO_WATCH}\\MP4','MP3':f'{DIR_TO_WATCH}\\MP3','FLACK': f'{DIR_TO_WATCH}\\FLACK','AVI': f'{DIR_TO_WATCH}\\AVI','JPG': f'{DIR_TO_WATCH}\\JPG','PNG': f'{DIR_TO_WATCH}\\PNG','CSV': f'{DIR_TO_WATCH}\\CSV','ZIP': f'{DIR_TO_WATCH}\\ZIP','RAR': f'{DIR_TO_WATCH}\\RAR','7ZIP': f'{DIR_TO_WATCH}\\7ZIP','OVA': f'{DIR_TO_WATCH}\\OVA','ISO': f'{DIR_TO_WATCH}\\ISO','OVPN': f'{DIR_TO_WATCH}\\OVPN','ICO': f'{DIR_TO_WATCH}\\ICO','GZ': f'{DIR_TO_WATCH}\\TAR_GZ','PSD': f'{DIR_TO_WATCH}\\PSD','XLSX': f'{DIR_TO_WATCH}\\XLSX','TORRENT': f'{DIR_TO_WATCH}\\TORRENT','PEM': f'{DIR_TO_WATCH}\\PEM','JSON': f'{DIR_TO_WATCH}\\JSON','ODT': f'{DIR_TO_WATCH}\\ODT','MD': f'{DIR_TO_WATCH}\\MD','MLX': f'{DIR_TO_WATCH}\\MLX','BAT': f'{DIR_TO_WATCH}\\BAT','TXT': f'{DIR_TO_WATCH}\\TXT','TIF': f'{DIR_TO_WATCH}\\TIF','RAW': f'{DIR_TO_WATCH}\\RAW','PY': f'{DIR_TO_WATCH}\\PY','JS': f'{DIR_TO_WATCH}\\JS','CSS': f'{DIR_TO_WATCH}\\CSS','HTML': f'{DIR_TO_WATCH}\\HTML','XML': f'{DIR_TO_WATCH}\\XML','C': f'{DIR_TO_WATCH}\\C','C++': f'{DIR_TO_WATCH}\\C++','PHP': f'{DIR_TO_WATCH}\\PHP','JAVA': f'{DIR_TO_WATCH}\\JAVA','JAR': f'{DIR_TO_WATCH}\\JAR','MKV': f'{DIR_TO_WATCH}\\MKV','OTHER':f'{DIR_TO_WATCH}\\OTHER'}
#'': f'{DIR_TO_WATCH}\\'   for faster coping    

def watchMyFiles():
    start = time.perf_counter()
    if not os.path.exists(DIR_TO_WATCH):
        sys.exit("Directory does not exist.")
        
    print(os.path.basename(os.path.realpath(__file__)))
    #TODO [ ] moving folders to DOWNLOADED_FOLDERS with everything in them // probably not useful lest leave folders alone
    for file in os.listdir(DIR_TO_WATCH):
        if file != str(os.path.basename(os.path.realpath(__file__))):
            if file != "myfileManager.exe":
                if os.path.isfile(DIR_TO_WATCH +"\\"+ file):
                    fileExt = file.split(".")[-1]
                    if ("."+fileExt) in FILE_EXT_TO_WATCH:
                        print(f'file: {file} | ext: {fileExt}')
                        if file.endswith(fileExt) or file.endswith(fileExt.upper()):
                            #TODO [ ] add exeption if file in folder already exists 
                            if os.path.exists(f'{DIR_TO_WATCH}\\{fileExt.upper()}'):
                                shutil.move(f'{DIR_TO_WATCH}\\{file}',f'{DIR_TO_WATCH}\\{fileExt.upper()}\\{file}')
                                print(f'{file} ----> {fileExt.upper()} folder')
                            elif os.path.exists(f'{DIR_TO_WATCH}\\{fileExt.upper()}') == False:
                                print(f'Creating dir: {fileExt.upper()}')
                                os.mkdir(f'{DIR_TO_WATCH}\\{fileExt.upper()}')
                                shutil.move(f'{DIR_TO_WATCH}\\{file}',f'{DIR_TO_WATCH}\\{fileExt.upper()}\\{file}')
                                print(f'{file} ----> {fileExt.upper()} folder')  
                            else:
                                print(f"Couldn't transfer {file} file to it's folder")
                else:
                    continue
            continue
        continue
    
    # for the remaning files with no known extension
    for file in os.listdir(DIR_TO_WATCH):
        if file != str(os.path.basename(os.path.realpath(__file__))):
            if file != "myfileManager.exe":
                if os.path.isfile(DIR_TO_WATCH +"\\"+ file):
                    if not os.path.exists(f'{DIR_TO_WATCH}\\OTHER'):
                        print(f'Creating dir: OTHER')
                        os.mkdir(f'{DIR_TO_WATCH}\\OTHER')

                    shutil.move(f'{DIR_TO_WATCH}\\{file}',f'{DIR_TO_WATCH}\\OTHER\\{file}')
                    print(f'{file} ----> OTHER folder')
                else:
                    assert Exception("Couldn't move file")
            continue
        continue
    
    print(f'Time taken to organize files: {round((time.perf_counter()-start),6)}s')
    
if __name__ == '__main__':
    try:
        print(f'Cleaning and organizing in progress in folder: {os.getcwd()}')
        watchMyFiles()
        sys.exit("All done !")
    except KeyboardInterrupt:
        sys.exit("Keyboard interruption, stopping.")
    
