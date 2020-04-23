
import pyfiglet as pi
import os
import platform
import requests
import main
class DNSfoot:
    
    def clear(self):
        if platform.system() == 'Linux':
            os.system("clear")
        if platform.system() == 'Windows':
            os.system('cls')
            os.system('color a')
        else:
            pass
        
    def DNSfootprint(self):
        self.clear()
        print('\n')
        print(os.system("figlet 'DNS FootPrinting' -f digital -c"))
        domain = input('             Enter The Domain name:')
        print(main.color.GREEN + '\n <-------------------------------------------------------------------------------------------->')

        print("" + str(os.system("curl https://api.hackertarget.com/hostsearch/?q="+ domain)))
        print(main.color.GREEN + '\n <-------------------------------------------------------------------------------------------->')
        coun = input(main.color.CYAN + '             Back to Manu(Y/N):')
        print('\n')
        if(coun == 'Y' or coun == 'y'):
            main.Hasky.spot(self)
        if(coun == 'N' or coun == 'n'):
            print('             Bye Bye')
            exit(1)    
        else:
            print("             Invalid Input:")
            exit(2)
if __name__ == "__main__":
    dnsfoot = DNSfoot()
    dnsfoot.DNSfootprint()
