"""
The way this file works is as follows:

1) get the "output_dir" for directory where they're going to be moved to.
2) strip the excessive newline character from the end. We only want the filename.
3) check if the filename itself has a particular file extension that isn't a html-file.
4) make a directory if it hasn't been created and copy the files over to the "output_dir" directory.

That's all it does, folks.

Look to README.md for how to use this file.


"""

from sys import stdin
from os import system
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--output_dir", type=str)

st_list=vars(parser.parse_args())['output_dir']

def make_dirs_and_copy_files(a):
        system("mkdir -p "+st_list+str('/'.join(a.replace('./','').split('/')[0:-1])+"/"))
        system("cp "+a+" "+st_list+str('/'.join(a.replace('./','').split('/')[0:-1])+"/"))
        print(a,"has been copied over successfully")

for a in stdin.readlines():
        a=a.replace('\n','')
        if a.count(".jpg") == 1:
                make_dirs_and_copy_files(a)
        if a.count(".jpeg") == 1:
                make_dirs_and_copy_files(a)
        if a.count(".png") == 1:
                make_dirs_and_copy_files(a)
        if a.count(".pdf") == 1:
                make_dirs_and_copy_files(a)
        if a.count(".js") == 1:
                make_dirs_and_copy_files(a)
        if a.count(".json") == 1:
                make_dirs_and_copy_files(a)
