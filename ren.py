#!/usr/bin/env python3
import os
import shutil
import unicodedata


def rename(source):
    os.chdir(source)

    for file in os.listdir(source):
        new_file = file
        if os.path.isdir(file):
            if new_file.find(' ') == -1:
                continue
            new_file = file.title()  # convert "name folder" => "NameFolder"
            new_file = new_file.replace(' ', '')  # remove ' '
            shutil.move(file, new_file)
            continue

        new_file = file.replace(' ', '-')  # remove ' '
        new_file = unicodedata.normalize('NFKD', new_file).encode(
            'ascii', 'ignore').decode()  # change Unicode VN to EN
        shutil.move(file, new_file)


try:
    source = os.getcwd()
    rename(source)
except KeyboardInterrupt:
    print("Wrong!")
