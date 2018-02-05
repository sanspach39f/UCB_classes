"""
Samuel Anspach
# 12/18/2017

1. Using os.walk, write a script that will print the filenames of zero length
files.
It should also print the count of zero length files.
"""
import os
import urllib.request
import re
count = 0
for path in os.walk("C:\\Users\\sansp\\Downloads"):
    files = path[2]
    for a in files:
        if os.path.getsize(os.path.join(path[0], a)) == 0:
            print(a)
            count += 1
print(count)

"""
2. Write a script that will list and count all of the images in a given HTML
web page/file.
You can assume that:
-   Each image file is enclosed with the tag <img and ends with >
-   The HTML page/file is syntactically correct
"""
site_name = input("What url would you like me to count the number of images in?")
f = urllib.request.urlopen(site_name)
contents = str(f.read())
pattern = re.compile("<img.*?>")
count = len(pattern.findall(contents))
print(count)
