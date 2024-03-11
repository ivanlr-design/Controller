from Utils.GetTime import GetTime

class Logs():
    def __init__(self, RED, YELLOW, GREEN, CYAN, BLUE, RESET) -> None:
        self.RED = RED
        self.YELLOW = YELLOW
        self.GREEN = GREEN
        self.CYAN = CYAN
        self.BLUE = BLUE
        self.RESET = RESET
        pass

    def Error(self, msj):
        print(f"{self.YELLOW}[{self.RED}!{self.YELLOW}] {self.YELLOW}{msj}{self.RESET}")
        with open("Logs.txt","a") as file:
            file.write(f"[ERROR] {GetTime()}: {msj}")
        
        file.close()
    
    def info(self, msj):
        print(f"[{self.BLUE}*{self.RESET}] {self.CYAN}{msj}{self.RESET}")
        with open("Logs.txt","a") as file:
            file.write(f"[INFO] {GetTime()}: {msj}")
        
        file.close()

    def Success(self, msj):
        print(f"{self.BLUE}[{self.GREEN}+{self.BLUE}] {self.GREEN}{GetTime()}: {msj}{self.RESET}")
        with open("Logs.txt","a") as file:
            file.write(f"[SUCCESS] {GetTime()}: {msj}")
        
        file.close()