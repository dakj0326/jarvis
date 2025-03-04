from json import dumps, loads

def updateCallHistory(dataIn: any): # Function(arguments='{"id": "all", "state": true, "color": [0, 0, 0], "brightness": 255}', name='setLights') toolResponse[0].function
    data = {
        'name': dataIn.name,
        'arguments': loads(dataIn.arguments)
    }
    lines = []
    try:
        f = open('callHistory', 'r')
        lines = f.readlines()
    except Exception as e:
        print('File does not exist, creating new')
        f = open('callHistory', 'x')

    if len(lines) != 0:
        for line in lines:
            rData = loads(line.replace('\n', ''))
            rArgs = rData['arguments']
            if data['arguments']['id'] == rArgs['id']:
                line = dumps(data)
                break
            else:
                lines.append(dumps(data) + '\n')
    else:
        lines.append(dumps(data) + '\n')
    f.close()
    f = open('callHistory', 'w')
    f.writelines(lines)
    f.close()

