import pyfiglet as pi
import os
import platform
import whois
import time
import main
class WhoisInfo:

    def whoisInfo(self):
        main.Hasky.clear(self)
        print('\n')
        print(os.system("figlet 'Whois Informaion' -f digital -c"))
        
        print(main.color.PURPLE + "             -for More information please visit https://icann.org/epp")
        print(main.color.YELLOW +'\n')
        data = input("          Enter a domain: ")
        print(main.color.GREEN + '\n <-------------------------------------------------------------------------------------------->')
        print(os.system('curl http://api.hackertarget.com/whois/?q=' + data))
        print('\n <-------------------------------------------------------------------------------------------->')
        ans = input(main.color.CYAN + "             Back To manu(Y/N)")
        if( ans == 'Y' or ans == 'y'):
            main.Hasky.spot(self)
        if( ans == 'N' or ans == 'n'):
            exit(1)
        else:
            print(main.color.RED + "Invalid Input :)")
if __name__ == "__main__":
    whoisReturn = WhoisInfo()
    whoisReturn.whoisInfo()