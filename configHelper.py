import configparser
'''Diskombobulatorn. Den diskombobulerar.'''

def getConf():
    config = configparser.ConfigParser()
    config.read('../config.ini')
    return config

def getLights():
        '''Returns all light settings as a list of dicts'''
        lights = []
        data = []
        conf = getConf()
        for sec in conf.sections():             
                if sec.startswith('light'):
                        for atr in conf[sec]:
                                stratr = (str)(atr)
                                item:dict = {atr: conf[sec][stratr]}
                                data.append(item)
                        lights.append(data)
                        data = []        
        return lights

def getSpeakers():
        '''Returns all speaker settings as a list of dicts'''
        speakers = []
        data = []
        conf = getConf()
        for sec in conf.sections():
                if sec.startswith('speaker'):
                        for atr in conf[sec]:
                                item:dict = {atr: conf[sec][atr]}
                                data.append(item)
                        speakers.append(data)
                        data = []        
        return speakers

def getValue(secName: str, value: str):
        '''Return specific value from config'''
        conf = getConf()
        return conf[secName].get(value)



def getDictValues(keys: list):
        values: list = []
        for key in keys:
                key = list(key.values())[0]
                values.append(key)
        return values

def mergeDicts(list: list):
        out = {}
        for d in list:
                out.update(d)
        return out

def getHAheaders():
        '''Returns headers for HA POSTs'''
        conf = getConf()
        headers = dict(conf['ha_headers'])
        headers['authorization'] += " " + getValue('home_assistant_settings', 'token')
        return headers


                       
