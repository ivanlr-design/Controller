import socket
import time
from Configuration.Colors import RED, GREEN, YELLOW, BLUE, CYAN, RESET
from Configuration.ReadConfig import ReadJson
from Log.Logs import Logs
from Server.StartServer import StartServer
import sys

Log_print = Logs(RED,YELLOW,GREEN,CYAN,BLUE,RESET)

values = ReadJson("configuration.json")
if values == None or values == False:
    Log_print.Error(f"Error while reading configuration file!")
    sys.exit(1)
else:
    port = values


host = socket.gethostbyname(socket.gethostname())

StartServer(host, port)