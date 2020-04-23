import subprocess
from termcolor import colored
import main
import os
class macspoof:

    def change_mac(self):
        main.Hasky.clear(self)
        print('\n')
        print(os.system("figlet 'MAC SPOOFING' -f digital -c"))
        interface = str(input("[*] Enter Interface to Change Mc Address On: "))
        print('\n')
        new_mac_address = input("[*] Enter New Mac Address To Change : ")
        print('\n')
        try:
            before_change = subprocess.check_output(["sudo","ifconfig",interface])

            subprocess.call(["sudo","ifconfig",interface,"down"])
            subprocess.call(["sudo","ifconfig",interface,"hw","ether",new_mac_address])
            subprocess.call(["sudo","ifconfig",interface,"up"])

            after_change = subprocess.check_output(["sudo","ifconfig",interface])
        except Exception:
            print("Invalid :)")
        if before_change == after_change:
            print(colored("[-] Faliled To Change Mac Address : "+ new_mac_address, 'red'))
            print('\n')
        else:
            print(colored("[+] Mac Address Changed To : "+ new_mac_address,'green'))
            print('\n')
        ans = input(main.color.CYAN + "             Back To manu(Y/N)")
        if( ans == 'Y' or ans == 'y'):
            main.Hasky.spot(self)
        if( ans == 'N' or ans == 'n'):
            exit(1)
        else:
            print(main.color.RED + "Invalid Input :)")


if __name__ == "__main__":
    macspf = macspoof()
    macspf.change_mac()
