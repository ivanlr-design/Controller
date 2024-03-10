import socket
import time
from Log.Logs import Logs
import sys
from Configuration.Colors import RED, GREEN, YELLOW, BLUE, CYAN, RESET

def StartServer(host, port):
    Log_print = Logs(RED,YELLOW,GREEN,CYAN,BLUE,RESET)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Log_print.info(f"SETING UP SERVER WITH HOST: {host}:{port}")
    time.sleep(1)
    try:
        server_socket.bind((host, int(port)))
    except Exception as e:
        Log_print.Error(f"Error while BINDING server: {e}")
        sys.exit(1)

    Log_print.Success(f"BINDED server successfully")
    server_socket.listen(5)
    Log_print.info(f"Waiting for CLIENTS to connect...")

    while True:
        client_socket, address = server_socket.accept()

        Log_print.info(f"CLIENT connected from: {address}!")