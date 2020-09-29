# python-scripts
 simple scripts for simple tasks

## Extract script
Written specifically for extracting data from translations provided in the format `translation-root-directory\language-code\strings.xml` with hundreds of different languages, to make it easier to import strings into design tools eg. Figma.

### What it does
- Opens all .xml files in a specified `BASE_DIRECTORY` (including subdirectories) 
- Uses regex to extract data between a given start and end string from the opened files 
- Uses regex to extract data between a given start and end string to extract data from the directory path of each file
- Prints the results into an output csv

### How to use it
- Install [Python](https://www.python.org/downloads/) using the installer, include all the defaults (this script was written in 3.8.6)
- Download extract-script.py
- Edit the script 
    - Set `BASE_DIRECTORY` to the parent directory
    - Set the column headers for the .csv `column-1,column-2`
    - Specify the beginning/end delimiters for the regex (`before-match` and `after-match`). The script will select whatever is between the two strings you provide. You need to do this in two places, one for the directory structure and one for the files opened. You may need to use four backslashes `\\\\` in place of a single backslash in the directory string.
- Open the script in IDLE (a Python IDE installed with Python) and run. Or run it any other way if you want.
- Check extract-output.csv in the directory of the script you ran. You may need to tweak your `before-match` and `after-match` to get the right string and directory fragment for your case.