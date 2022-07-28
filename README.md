# Welcome one and all

# Do you need to recover from a borked website state? Has someone hacked you and left garbled content you don't recognize?
# Do you need a simple way to recover as much of the content as possible?

This repo is for those who need to recover their website. lets say a hacker broke in and flooded your website with content that isn't yours. And you don't
 know how much is random bunk added from anywhere. And lets also say that said hacker did such in the hopes that the website gets taken down for good.
Well, now their is a easy solution to that problem.

# What is the solution that your repo offers?

The solution is to edit the files after cloning this repo. Mainly the "look_for_and_exclude_html_copy.py" file in particular.

# What do I edit about that file so it works for me?

1) the text that says "SEARCH_TERM_GOES_HERE" for what you're looking for that is consistent with your name or company name.
2) the line that has the "a.count('EXCLUDE_DIR_CONTAINING_THIS_TEXT_IN_AND_STATEMENT_TO_THE_NEXT_THING_TO_EXCLUDE') == 0". In particular, the statement
 to exclude "EXCLUDE_DIR_CONTAINING_THIS_TEXT_IN_AND_STATEMENT_TO_THE_NEXT_THING_TO_EXCLUDE". And if you have more things that need exclusion, just add to 
  the line "and a.count('str_txt') == 0" with "str_txt" replaced with what you want excluded before the colon.

# Okay, now I've edited my local copy of the file "look_for_and_exclude_html_copy.py", now how do I use overall solution?

All depends on if you used "wget" or "httrack" to download your web-content recursively.

It is recommended you do this from within the directory you downloaded the content into and the rest of this is written with that assumption in mind.

# If you used "httrack" to recursively get your web-content back:

tree -f -J . | grep ":\\"file" | python3 from_linux_json_tree.py | python3 httrack_tmp_file_extension_excluder.py | python3 look_for_and_exclude_html_copy.py --output_dir=../website_recovered_data/

# If you used "wget" to recursively get your web-content back:
wget -r --continue --domains $DOMAIN https://$DOMAIN # DOMAIN=www.example.com<br>
tree -f -J . | grep ":\\"file" | python3 from_linux_json_tree.py | python3 look_for_and_exclude_html_copy.py --output_dir=../website_recovered_data/

# And finally

tree -f -J .| python3 from_linux_json_tree.py | python3 transfer_not_html_files.py --output_dir=../website_recovered_data/<br>
tree -f -J ./subdir_with_js_files | grep "\\?" | python3 from_linux_json_tree.py | python3 js_filename_correction.py

# Is that it?

Primarily, yes. Now their will be some link correction you'll have to do probably manually. And that's before
restanding up your website.

Their shouldn't be much beyond that. 


# How do I use your speedy_web_downloader.py file?

tree -f -J . | grep "\.html" | python3 from_linux_json_tree.py | python3 speedy_web_downloader.py

# what do I do if I have duplicates with a "html.1" extension?
tree -f -J . | grep "\.html.1" | python3 from_linux_json_tree.py >> dupes.txt
rm $(cat dupes.txt)
rm dupes.txt

# What do I do to remove access to a part of the site like my custom search for my website?

sed -zre 's/(\<li id="menu-item-search" class="noMobile menu-item menu-item-search-dropdown menu-item-avia-special">.*?\<\/li>)(\<li class="av-burger-menu-main menu-item-avia-special "\>)/<\!-- \1  -->\2/g' -i index.html

The first field is the html to look for, the second is the end tag to that search field. The second field in parentesis is the thing it ends near.
 The third part separates the first two parentesis into group 1 that is being commented out ("\1"). The group ("\2") is the second part that isn't getting commented out.
