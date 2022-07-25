# Speed_download_entire_sites

Welcome. We'll speedily download as much of the website without using wget.

httrack $URL_GOES_HERE -O "~/websites/$DIR_NAME_GOES_HERE" -Y --continue

to download a website.

watch -n .1 'grep -rl $SEARCH_TEXT_IN_QUOTATIONS_GOES_HERE . | sed -e 's/?.*//g' | sed -e 's/.*search.*//g' | sort | uniq -c | sort -gr | wc -l'

to watch it download new content and eliminate unneeded results. "?" in a URL doesn't matter as much to what we'd be looking for.

# What is the purpose of this?

To recover websites as quickly as possible. It is for when someone hacks your website and you need a quick way to recover from that hack. The type of hack I am talking about is one where the hacker breaks in and leaves random content scattered about your website. The hack is done to force a website to be taken down in the hopes that it never gets stood back up.

# Wouldn't they just attempt to repeat that hack on the next standup of the website?

They can attempt such, but, the method of intrusion becomes easier to spot and secure against.

# What would stop the hacker completely? Wouldn't they just have to add in the text you searched for to make it harder?

Better analysis tools and better metrics
