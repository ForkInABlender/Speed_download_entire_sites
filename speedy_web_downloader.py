# main5.py

# Dylan Kenneth Eliot

"""
Do use with caution. While I did write the code for website recovery, if you use this to hack someone, you will likely get caught and I am not responsible
 for code misuse.

This is meant for website recovery and nothing more.

"""

from sys import stdin
from os import environ, popen

#for each file, replace the newline character
for a in stdin.readlines():
	a=a.replace('\n','')
	#cd into subdirectory
	#snag the subdirectory name as a URL component; then remove the search button by commenting out said search button
	#cd back to root directory we started in
	popen("cd "+'/'.join(a.split("/")[0:-1])+"; wget https://"+environ['PWD'].split("/")[-1].replace("...", "")+'/'.join(a.split("/")[0:-1]).replace(".","")+'/;'+""" sed -zre 's/(<li id="menu-item-search" class="noMobile menu-item menu-item-search-dropdown menu-item-avia-special">.*?<\/li>)(<li class="av-burger-menu-main menu-item-avia-special ">)/<\!-- \\1  -->\\2/g' -i index.html; """+"cd ..")

#print(environ['PWD'].split("/")[-1].replace("...", ""))
#print()
