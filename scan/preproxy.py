import os
import sys
import platform
import main

class preproxy:
    def torproxy(self):
        try:
            main.Hasky.clear(self)
            os.system("sudo service tor start")
            print("     Proxy Started...................\n")
            ans = input(main.color.CYAN + "             Back To manu(Y/N)")
            if( ans == 'Y' or ans == 'y'):
                main.Hasky.spot(self)
            if( ans == 'N' or ans == 'n'):
                exit(1)
            else:
                print(main.color.RED + "Invalid Input :)")
        except :
            os.system("sudo service tor stop")
            print("     proxy Stoped......................")

if __name__ == '__main__':
    p = preproxy()
    p.torproxy()
