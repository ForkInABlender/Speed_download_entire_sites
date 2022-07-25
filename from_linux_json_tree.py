# main.py

# Dylan Kenneth Eliot

"""

Takes input and correctly formats the linux json output of the current directory containing files, and return a list the filename & its originating
 directory.


That's all it does.

Look to README.md for more information on how to use it.

"""


import sys
x=sys.stdin.readlines()

for a in range(len(x)):
        x[a]=x[a].replace('\n','')
        if type(eval(x[a])) == type(tuple()):
                print(eval(x[a])[0]['name'])
        if type(eval(x[a])) == type(dict()):
                print(eval(x[a])['name'])
