# main2.py

# Dylan Kenneth Eliot


"""
This file works as follows:

1) get the "output_dir" for the output directory
2) find the content to search for with a unique identifier
3) exclude a particular search term or set of results and'ed together by filename
4) make a directory if it doesn't exist
5) copy content over from the original location to its final destination 

 :-)

Look to README.md for more information on how to use. 

"""

from sys import stdin
from os import system
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--output_dir", type=str)

system("mkdir -p "+vars(parser.parse_args())['output_dir'])


for a in stdin.readlines():
        a=a.replace('\n','')
        try:
                b=''.join(open(a, 'r').readlines())
                if b.count('SEARCH_TERM_GOES_HERE') >= 1:
                        if a.count('EXCLUDE_DIR_CONTAINING_THIS_TEXT_IN_AND_STATEMENT_TO_THE_NEXT_THING_TO_EXCLUDE') == 0:
                                st_list=vars(parser.parse_args())['output_dir']
                                system("mkdir -p "+st_list+str('/'.join(a.replace('./','').split('/')[0:-1])+"/"))
                                system("cp "+a+" "+st_list+str('/'.join(a.replace('./','').split('/')[0:-1])+"/"))
        except:
                continue
