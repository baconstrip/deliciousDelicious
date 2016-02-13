from os import walk
from pprint import pprint
from Display import Display
from LayoutGenerator import *

import json
import re
import os

def loadDisplays():
    f = []
    for (dirpath, dirnames, filenames) in walk(os.getcwd() + "/displays/"):
        f.extend(filenames)
        break

    pat = re.compile('.*?\.json')

    jsonfiles = []

    for candidate in f:
        if(pat.match(candidate)):
            jsonfiles.append(candidate)

    modules = []

    for jsonfile in jsonfiles:
        print("loading display {}".format(jsonfile))
        definition = json.load(open(os.getcwd() + "/displays/" + jsonfile))
        pyfile = definition.get("pyfile")
        classname = definition.get("classname")
        # Load and execute the pyfile specified
        exec(open(os.getcwd() + "/displays/" + pyfile).read(),globals())
        # Exec the module's constructor
        constructor = globals()[classname]
        # instantiate
        instance = constructor()
        modules.append(instance)

    return modules


if __name__ == "__main__":
    displays = loadDisplays()
    print(displays)

    for display in displays:
        print(htmlForDisplay(display))
