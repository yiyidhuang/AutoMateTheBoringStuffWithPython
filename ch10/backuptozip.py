#! python3
# backuptozip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile
import os


def backuptozip(folder):
    # Back up the entire contents of "folder" into a ZIP file

    folder = os.path.abspath(folder)     # make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exist
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the ZIP fle.
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire forlder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the zip file
        backupZip.write(foldername)

        # Add all the files in this folder to the zip file.
        for filename in filenames:
            if filename.startwitch(os.path.basename(folder) + '_') and filename.endswitch('.zip'):
                continue
            backupZip.write(os.path.join(filename, filename))
    backupZip.close()
    print('Done.')


backuptozip('C:\\delicious')
