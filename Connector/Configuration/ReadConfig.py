import json
import os

def ReadJSON(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            jsonfile = json.load(f)
            try:
                IP = jsonfile['Connection']['ConnectIP']
                Port = jsonfile['Connection']['ConnectPort']
                
                return IP, Port
            except:
                return False
            
    else:
        return None