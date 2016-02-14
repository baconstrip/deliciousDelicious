from os import walk
from pprint import pprint
from Display import Display
from LayoutGenerator import *

import json
import re
import os

        
def createDisplays():
    displays = loadDisplays(globals())
    with open('config.json', 'r') as json_data:
        configs = json.load(json_data)

    panels = []

    for config in configs:
        # Exec the module's constructor
        pprint(config)
        constructor = globals()[displays.get(config['display'])]
        # instantiate
        instance = constructor(config['name'], config['data'])
        panels.append(instance)

    return panels


def loadDisplays(gvalues):
    
    f = []
    for (dirpath, dirnames, filenames) in walk(os.getcwd() + "/displays/"):
        f.extend(filenames)
        break

    pat = re.compile('.*?\.json')

    jsonfiles = []

    for candidate in f:
        if(pat.match(candidate)):
            jsonfiles.append(candidate)

    modules = {}

    for jsonfile in jsonfiles:
        print("loading display {}".format(jsonfile))
        definition = json.load(open(os.getcwd() + "/displays/" + jsonfile))
        pyfile = definition.get("pyfile")
        classname = definition.get("classname")
        name = definition.get("name")
        # Load and execute the pyfile specified
        exec(open(os.getcwd() + "/displays/" + pyfile).read(),gvalues)
        # Exec the module's constructor
       # constructor = globals()[classname]
        # instantiate
        #instance = constructor()
        #modules.append(instance)
        modules[name] = classname

    return modules

if __name__ == "__main__":
    displays = loadDisplays()
    print(displays)

    for display in displays:
        print(htmlForDisplay(display))
