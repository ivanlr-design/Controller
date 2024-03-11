import socket
from Log.Logs import Logs
from Configuration.Colors import RED, BLUE, CYAN, GREEN, YELLOW ,RESET

def ConnectToClient(host, port):
    Log_print = Logs(RED, BLUE, CYAN, GREEN, YELLOW ,RESET)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Log_print.info(f"Trying connection to: {host}:{port}")
    try:
        client_socket.connect((host, port))
        Log_print.Success(f"Succesfully connected to {host}:{port}")
        return client_socket
    except Exception as e:
        return False