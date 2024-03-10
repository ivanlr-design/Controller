import json
import os

def ReadJson(filename): 
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                read = json.load(f)
                port = read['Config']['Default Port']

            if port:

                return port
            else:
                return None
        except:

            return False
    else:
        return None
