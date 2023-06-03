# This python script reads the extention of the file and moves them in a apropriate folder
import os
import shutil

directory = os.getcwd() + ''

file_extensions ={
    'pdf': 'PDFs',
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'gif': 'Images',
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    'csv': 'Data',
    'xlsx': 'Data',
    'zip': 'Archives',
    'rar': 'Archives',
    'exe': 'Executables',
    'mp3': 'Music',
    'wav': 'Music',
    'mp4': 'Videos',
    'avi': 'Videos',
    'flv': 'Videos',
    'wmv': 'Videos',
}

for files in directory:
    filename,extension = os.path.splitext(files)
    extension = extension[1:]

    if os.path.exists(directory+'/'+extension):
        shutil.move(directory+'/'+files, directory+'/'+extension+'/'+files)
    else:
        os.mkdirs(directory+'/'+extension)
        shutil.move(directory+'/'+files, directory+'/'+extension+'/'+files)