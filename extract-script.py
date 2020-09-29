# import libraries
import os
import re

# define location of parent folder
BASE_DIRECTORY = r'C:\folderpath'
file_list = []

# search sub folders for xml files
for (dirpath, dirnames, filenames) in os.walk(BASE_DIRECTORY):
    for f in filenames:
        if 'xml' in str(f): # find filetypes matching xml, change for other types 
            e = os.path.join(str(dirpath), str(f))
            file_list.append(e)

# loop over files and use regex to get strings
with open('extract-output.csv', 'w', encoding='utf-8') as text_file: # change .csv to whatever is needed 
    print(f'column-1,column-2', file=text_file) # print column headers for csv
    for f in file_list:
        try:
            directoryname = re.search('before-match(.+?)after-match', f).group(1) # change 'before-match' and 'after-match' to the text before and after the string you want to extract)
            print('language: ' + directoryname)
            print(directoryname, file=text_file, end='') # end='' prevents new line after print method
        except AttributeError:
            directoryname = 'no directory match' # error handling placeholder
        txtfile = open(f, 'r', encoding='utf-8')
        for line in txtfile:
            try:
                found = re.search('before-match(.+?)after-match', line).group(1) # change 'before-match' and 'after-match' to the text before and after the string you want to extract)
                print('translation: ' + found)
                print(found, file=text_file)
            except AttributeError:
                found = 'no string match' # error handling placeholder
text_file.close()
