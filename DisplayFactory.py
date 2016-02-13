import json

class DisplayFactory:
    
    def __init__():

        with open('config.json', 'r') as json_data:
            config = json.load(json_data)


        # Exec the module's constructor
        constructor = globals()[config['display']]
        # instantiate
        instance = constructor(config['data'])
        modules.append(instance)

