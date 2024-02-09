# Looks for files which contain all of listed strings
# It looks only in .txt .xml and .json files
import os

path = '/PATH/TO/FOLDER//'

strings_to_have = [
    'FILE',
    'MUST',
    'CONTAIN',
    "THESE",
    'STRINGS.',
]

for path, subdirs, files in os.walk(path):
    for fl in files:
        key = ''
        if '.txt' in fl or '.xml' in fl or '.json' in fl:
            file1 = open(path + '/' + fl, "r")
            read_content = file1.read()
            file1.close()
            if all(i in read_content for i in strings_to_have):
                print(fl)
            # print(read_content)
        # break
    # break


