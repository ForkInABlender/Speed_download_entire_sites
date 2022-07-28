from sys import stdin
from os import environ, popen
from time import sleep



"""
This code sifts through "wp-*" (wordpress) subdirectories and looks at the index.html, then gets the missing .js & puts it in the correct folder.
It also gets the missing images that wordpress panels rely on.

"""



for a in stdin.readlines():
        a=a.replace('\n','')
        x=open(a, 'r')
        for b in x.readlines():
                if b.count("<a href=") and b.count("</a") == 1:
                        sub_dirs='/'.join(a.split("/")[0:-1])+"/"
                        print(popen("cd "+sub_dirs+"; wget https://"+environ['PWD'].split("/")[-1].replace("...", "")+"/"+sub_dirs+eval(b.replace('\n','').strip("<a href=").split(">")[0])).read())
                        sleep(1.5)
