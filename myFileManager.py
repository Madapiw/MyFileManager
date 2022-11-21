import sys
import os
import shutil
import time

#DIR FOR TESTS
DIR_TO_WATCH = os.getcwd()

FILE_EXT_TO_WATCH = ['.pdf','.exe','.docx','.mp4','.mp3','.flack','.avi','.jpg','.png','.csv','.zip','.rar','.7z','.ova','.iso','ovpn','.ico','.gz','.psd','.xlsx','.torrent','.pem','.json','.odt','.md','.mlx','.bat','.txt','.tif','.raw','.py','.js','.css','.html','.xml','.c','.cpp','.php','.java','.jar','.mkv','.dll','.aif','.cda','.midi','.mid','.mpa','.ogg','.wav','.wma','.wpl','.arj','.deb','.pkg','.rpm','.z','.bin','.dmg','.toast','.vcd','.dat','.db','.dbf','.log','.mdb','.sav','.sql','.email','.eml','.emlx','.msg','.oft','.ost','.pst','.vcf','.apk','.cgi','.pl','.com','sass','.gadget','.wsf','.fnt','.fon','.otf','ttf','.ai','.bmp','.ps','.psd','.svg','.tiff','.tif','.asp','.aspx','.cer','.cfm','.htm','.jsp','.part','.rss','.xhtml','.key','.odp','.pps','.ppt','.pptx','.cs','.h','.swift','.vb','.ods','.xls','.xlsm','.bak','.cab','.cfg','.cpl','.cur','.dmp','.drv','.icns','.ini','.ink','.msi','.sys','.tmp','.3g2','.3gp','.flv','.h264','.m4v','.mov','.mpg','.mpeg','.rm','.swf','.vob','.wmv','.doc','.rtf','.tex','.wpd','.epub','.img','.fb2','.mobi','.azw','.iba','.azw3']

#TODO[X] write rest of folders to create and arrange
DIRS_TO_MOVE = {'PDF': f'{DIR_TO_WATCH}\\PDF','EXE':f'{DIR_TO_WATCH}\\EXE','DOCX': f'{DIR_TO_WATCH}\\DOCX','MP4':f'{DIR_TO_WATCH}\\MP4','MP3':f'{DIR_TO_WATCH}\\MP3','FLACK': f'{DIR_TO_WATCH}\\FLACK','AVI': f'{DIR_TO_WATCH}\\AVI','JPG': f'{DIR_TO_WATCH}\\JPG','PNG': f'{DIR_TO_WATCH}\\PNG','CSV': f'{DIR_TO_WATCH}\\CSV','ZIP': f'{DIR_TO_WATCH}\\ZIP','RAR': f'{DIR_TO_WATCH}\\RAR','7ZIP': f'{DIR_TO_WATCH}\\7ZIP','OVA': f'{DIR_TO_WATCH}\\OVA','ISO': f'{DIR_TO_WATCH}\\ISO','OVPN': f'{DIR_TO_WATCH}\\OVPN','ICO': f'{DIR_TO_WATCH}\\ICO','GZ': f'{DIR_TO_WATCH}\\TAR_GZ','PSD': f'{DIR_TO_WATCH}\\PSD','XLSX': f'{DIR_TO_WATCH}\\XLSX','TORRENT': f'{DIR_TO_WATCH}\\TORRENT','PEM': f'{DIR_TO_WATCH}\\PEM','JSON': f'{DIR_TO_WATCH}\\JSON','ODT': f'{DIR_TO_WATCH}\\ODT','MD': f'{DIR_TO_WATCH}\\MD','MLX': f'{DIR_TO_WATCH}\\MLX','BAT': f'{DIR_TO_WATCH}\\BAT','TXT': f'{DIR_TO_WATCH}\\TXT','TIF': f'{DIR_TO_WATCH}\\TIF','RAW': f'{DIR_TO_WATCH}\\RAW','PY': f'{DIR_TO_WATCH}\\PY','JS': f'{DIR_TO_WATCH}\\JS','CSS': f'{DIR_TO_WATCH}\\CSS','HTML': f'{DIR_TO_WATCH}\\HTML','XML': f'{DIR_TO_WATCH}\\XML','C': f'{DIR_TO_WATCH}\\C','C++': f'{DIR_TO_WATCH}\\C++','PHP': f'{DIR_TO_WATCH}\\PHP','JAVA': f'{DIR_TO_WATCH}\\JAVA','JAR': f'{DIR_TO_WATCH}\\JAR','MKV': f'{DIR_TO_WATCH}\\MKV','DLL': f'{DIR_TO_WATCH}\\DLL','AIF': f'{DIR_TO_WATCH}\\AIF','CDA': f'{DIR_TO_WATCH}\\CDA','MIDI': f'{DIR_TO_WATCH}\\MIDI','MID': f'{DIR_TO_WATCH}\\MID','MPA': f'{DIR_TO_WATCH}\\MPA','OGG': f'{DIR_TO_WATCH}\\OGG','WAV': f'{DIR_TO_WATCH}\\WAV','WMA': f'{DIR_TO_WATCH}\\WMA','WPL': f'{DIR_TO_WATCH}\\WPL','ARJ': f'{DIR_TO_WATCH}\\ARJ','DEB': f'{DIR_TO_WATCH}\\DEB','PKG': f'{DIR_TO_WATCH}\\PKG','RPM': f'{DIR_TO_WATCH}\\RPM','Z': f'{DIR_TO_WATCH}\\Z','BIN': f'{DIR_TO_WATCH}\\BIN','DMG': f'{DIR_TO_WATCH}\\DMG','TOAST': f'{DIR_TO_WATCH}\\TOAST','VCD': f'{DIR_TO_WATCH}\\VCD','DAT': f'{DIR_TO_WATCH}\\DAT','DB': f'{DIR_TO_WATCH}\\DB','DBF': f'{DIR_TO_WATCH}\\DBF','LOG': f'{DIR_TO_WATCH}\\LOG','MDB': f'{DIR_TO_WATCH}\\MDB','SAV': f'{DIR_TO_WATCH}\\SAV','SQL': f'{DIR_TO_WATCH}\\SQL','EMAIL': f'{DIR_TO_WATCH}\\EMAIL','EML': f'{DIR_TO_WATCH}\\EML','EMLX': f'{DIR_TO_WATCH}\\EMLX','MSG': f'{DIR_TO_WATCH}\\MSG','OFT': f'{DIR_TO_WATCH}\\OFT','OST': f'{DIR_TO_WATCH}\\OST','PST': f'{DIR_TO_WATCH}\\PST','VCF': f'{DIR_TO_WATCH}\\VCF','APK': f'{DIR_TO_WATCH}\\APK','CGI': f'{DIR_TO_WATCH}\\CGI','PL': f'{DIR_TO_WATCH}\\PL','COM': f'{DIR_TO_WATCH}\\COM','SASS': f'{DIR_TO_WATCH}\\SASS','GADGET': f'{DIR_TO_WATCH}\\GADGET','WSF': f'{DIR_TO_WATCH}\\WSF','FNT': f'{DIR_TO_WATCH}\\FNT','FON': f'{DIR_TO_WATCH}\\FON','OTF': f'{DIR_TO_WATCH}\\OTF','TTF': f'{DIR_TO_WATCH}\\TTF','AI': f'{DIR_TO_WATCH}\\AI','BMP': f'{DIR_TO_WATCH}\\BMP','PS': f'{DIR_TO_WATCH}\\PS','PSD': f'{DIR_TO_WATCH}\\PSD','SVG': f'{DIR_TO_WATCH}\\SVG','TIFF': f'{DIR_TO_WATCH}\\TIFF','TIF': f'{DIR_TO_WATCH}\\TIF','ASP': f'{DIR_TO_WATCH}\\ASP','ASPX': f'{DIR_TO_WATCH}\\ASPX','CER': f'{DIR_TO_WATCH}\\CER','CFM': f'{DIR_TO_WATCH}\\CFM','HTM': f'{DIR_TO_WATCH}\\HTM','JSP': f'{DIR_TO_WATCH}\\JSP','PART': f'{DIR_TO_WATCH}\\PART','RSS': f'{DIR_TO_WATCH}\\RSS','XHTML': f'{DIR_TO_WATCH}\\XHTML','KEY': f'{DIR_TO_WATCH}\\KEY','ODP': f'{DIR_TO_WATCH}\\ODP','PPS': f'{DIR_TO_WATCH}\\PPS','PPT': f'{DIR_TO_WATCH}\\PPT','PPTX': f'{DIR_TO_WATCH}\\PPTX','CS': f'{DIR_TO_WATCH}\\CS','H': f'{DIR_TO_WATCH}\\H','SWIFT': f'{DIR_TO_WATCH}\\SWIFT','VB': f'{DIR_TO_WATCH}\\VB','ODS': f'{DIR_TO_WATCH}\\ODS','XLS': f'{DIR_TO_WATCH}\\XLS','XLSM': f'{DIR_TO_WATCH}\\XLSM','BAK': f'{DIR_TO_WATCH}\\BAK','CAB': f'{DIR_TO_WATCH}\\CAB','CFG': f'{DIR_TO_WATCH}\\CFG','CPL': f'{DIR_TO_WATCH}\\CPL','CUR': f'{DIR_TO_WATCH}\\CUR','DMP': f'{DIR_TO_WATCH}\\DMP','DRV': f'{DIR_TO_WATCH}\\DRV','ICNS': f'{DIR_TO_WATCH}\\ICNS','INI': f'{DIR_TO_WATCH}\\INI','INK': f'{DIR_TO_WATCH}\\INK','MSI': f'{DIR_TO_WATCH}\\MSI','SYS': f'{DIR_TO_WATCH}\\SYS','TMP': f'{DIR_TO_WATCH}\\TMP','3G2': f'{DIR_TO_WATCH}\\3G2','3GP': f'{DIR_TO_WATCH}\\3GP','FLV': f'{DIR_TO_WATCH}\\FLV','H264': f'{DIR_TO_WATCH}\\H264','M4V': f'{DIR_TO_WATCH}\\M4V','MOV': f'{DIR_TO_WATCH}\\MOV','MPG': f'{DIR_TO_WATCH}\\MPG','MPEG': f'{DIR_TO_WATCH}\\MPEG','RM': f'{DIR_TO_WATCH}\\RM','SWF': f'{DIR_TO_WATCH}\\SWF','VOB': f'{DIR_TO_WATCH}\\VOB','WMV': f'{DIR_TO_WATCH}\\WMV','DOC': f'{DIR_TO_WATCH}\\DOC','RTF': f'{DIR_TO_WATCH}\\RTF','TEX': f'{DIR_TO_WATCH}\\TEX','WPD': f'{DIR_TO_WATCH}\\WPD','EPUB': f'{DIR_TO_WATCH}\\EPUB','IMG': f'{DIR_TO_WATCH}\\IMG','FB2': f'{DIR_TO_WATCH}\\FB2','MOBI': f'{DIR_TO_WATCH}\\MOBI','AZW': f'{DIR_TO_WATCH}\\AZW','IBA': f'{DIR_TO_WATCH}\\IBA','AZW3': f'{DIR_TO_WATCH}\\AZW3'}
#'': f'{DIR_TO_WATCH}\\'   for faster coping    

def watchMyFiles():
    start = time.perf_counter()
    if not os.path.exists(DIR_TO_WATCH):
        sys.exit("Directory does not exist.")
        
    #TODO [ ] moving folders to DOWNLOADED_FOLDERS with everything in them // probably not useful just leave folders alone
    for file in os.listdir(DIR_TO_WATCH):
        if file != str(os.path.basename(os.path.realpath(__file__))):
            if file != "myFileManager.exe":
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
            if file != "myFileManager.exe":
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
    
    print(f'\n Time elapsed for organizing files: {round((time.perf_counter()-start),6)}s \n')
    
if __name__ == '__main__':
    try:
        print("                                               <<< My File Manager >>> \n")
        print("<---------------------------------------------------------------------------------------------------------------->")
        print(f'Cleaning and organizing in progress, in folder: {os.getcwd()} \n')
        watchMyFiles()
        print("All done ! Press any key to quit")
        os.system("pause")
    except KeyboardInterrupt:
        sys.exit("Keyboard interruption, stopping.")
        
    
