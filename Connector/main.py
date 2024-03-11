from Configuration.ReadConfig import ReadJSON
from Configuration.Colors import RED, BLUE, CYAN, GREEN, YELLOW ,RESET
from Log.Logs import Logs
from Client.ClientStart import StartClient
import sys
import os

values = ReadJSON("configuration.json")

conections = {}

Log_print = Logs(RED, BLUE, CYAN, GREEN, YELLOW ,RESET)

if values == None or values == False:
    Log_print.Error(f"Error while reading configuration file!")
    sys.exit(1)
else:
    IP, Port = values
    
socket = StartClient(IP, Port)

if socket != False:
    conections[IP] = socket
else:
    Log_print.Error(f"Can't connect to : {IP}:{Port}")