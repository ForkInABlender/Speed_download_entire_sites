# main1.py

# Dylan Kenneth Eliot

"""
"Give me the files that don't contain '.tmp' as a part of their filename" is all it does.

It is useful if you're using httrack to copy a website.

"""

from sys import stdin

for a in stdin.readlines():
        a=a.replace('\n','')
        if a.count('.tmp') == 0:
                print(a)
