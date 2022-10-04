#!/usr/bin/env python3
from sys import argv

def add_bullet():
    file_name = argv[1]
    # file_name = "/media/dat/DISK/Note/Personal/Hospital.md"
    
    with open(file_name, 'r') as file:
        items = file.readlines()
        with open(file_name+'.md', 'w') as f:
            for i in items:
                tabs = i.count('\t')
                # remove tabs then add '- '
                removed_tabs = '- ' + i.replace('\t','')
                # add tabs
                new_line = '\t'*tabs + removed_tabs
                f.write(new_line)

    print(f"Done {file_name}")

add_bullet()