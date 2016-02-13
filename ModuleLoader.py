from os import walk
from pprint import pprint
import json
import re
import os

def loadModules():
    f = []
    for (dirpath, dirnames, filenames) in walk(os.getcwd() + "/modules/"):
        f.extend(filenames)
        break

    pat = re.compile('.*?\.json')

    jsonfiles = []

    for candidate in f:
        if(pat.match(candidate)):
            jsonfiles.append(candidate)

    modules = []

    for jsonfile in jsonfiles:
        definition = json.load(open(os.getcwd() + "/modules/" + jsonfile))
        pyfile = definition.get("pyfile")
        classname = definition.get("classname")
        # Load and execute the pyfile specified
        exec(open(os.getcwd() + "/modules/" + pyfile).read())
        # Exec the module's constructor
        constructor = globals()[classname]
        # instantiate
        instance = constructor()
        modules.append(instance)

    return modules
