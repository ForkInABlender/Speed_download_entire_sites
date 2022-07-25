from sys import stdin
from os import system
"""
The purpose of this file is to correct files with unneeded URI information and keep the file content.

It does the following in this order:

1) remove excessive newline characters from the input. We only need the file name.
2) create a new file not containing URI information.
3) write the data of the original file to the filename it should have been. We don't need the URI information embedded in the filename. 
4) close the file when we're done.
5) delete the original file with the URI in its filename.
6) check to be sure it was deleted after transfer of its contents.

Look to the README.md for how to use this file correctly.

"""

for a in stdin.readlines():
        orig_fn=a.replace('\n','')
        b=open(orig_fn.split('?')[0], 'w')
        b.write(''.join(open(orig_fn, 'r').readlines()))
        b.close()
        system("rm "+orig_fn)
        system("ls "+orig_fn)
