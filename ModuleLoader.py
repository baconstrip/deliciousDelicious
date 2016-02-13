from os import walk
from pprint import pprint
import json
import re
import os

f = []
for (dirpath, dirnames, filenames) in walk(os.getcwd() + "/modules/"):
    f.extend(filenames)
    break

pat = re.compile('.*?\.json')

jsonfiles = []

for candidate in f:
    if(pat.match(candidate)):
        jsonfiles.append(candidate)

for jsonfile in jsonfiles:
    definition = json.load(open(os.getcwd() + "/modules/" + jsonfile))
    pprint(definition)
