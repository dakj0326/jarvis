import configparser
# Diskombobulatorn
def getConf():
    config = configparser.ConfigParser()
    config.read('../config.ini')
    return config

def getLights():        # Utdata är en lista av dicts
        lights = []
        data = []
        conf = getConf()
        for sec in conf.sections():
                if sec.startswith("light"):
                        for atr in conf[sec]:
                                item:dict = {atr: conf[sec][atr]}
                                data.append(item)
                        lights.append(data)
                        data = []        
        return lights

def getSpeakers():      # Utdata är en lista av dicts
        speakers = []
        data = []
        conf = getConf()
        for sec in conf.sections():
                if sec.startswith("speaker"):
                        for atr in conf[sec]:
                                item:dict = {atr: conf[sec][atr]}
                                data.append(item)
                        speakers.append(data)
                        data = []        
        return speakers

def getValue(secName: str, value: str):       # Return specific value
        conf = getConf()
        return conf[secName].get(value)



def getDictValues(keys: list):  # Get the values from a dict
        values: list = []
        for key in keys:
                key = list(key.values())[0]
                values.append(key)
        return values

def mergeDicts(list: list): # Convert a list of dicts into one dict
        out = {}
        for d in list:
                out.update(d)
        return out


                       
