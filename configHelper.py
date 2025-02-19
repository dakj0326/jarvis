import configparser
# Diskombobulatorn
def getConf():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def getLights():
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

def getSpeakers():
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

                       
