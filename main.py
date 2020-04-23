import pyfiglet as fi
import os
import click
import sys
import platform
import time
import datetime
import info.emailfootprint as emailfootprint
import info.dnsfootprint as dnsfootprint
import scan.macspoof as macspf
import info.whoisInfo as whois
import info.infobanner as infobanner
import scan.preproxy as preproxy
import scan.scanbanner as scanbanner
import scan.networkscan as networkscan
import scan.firewallcheck as firewallcheck
import social.socialbanner as socialbanner
import social.googlehacking as googlehacking
import social.hiddenfield as hiddenfield
import sniff.sniffbanner as sniffbanner
import dos.dosbanner as dosbanner
import dos.portchange as pc

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Hasky:

    def clear(self):
        if platform.system() == 'Linux':
            os.system("clear")
        if platform.system() == 'Windows':
            os.system('cls')
            os.system('color a')
        else:
            pass

    def spot(self):
        self.clear()
        print("\n\n")
        print(os.system(
            "toilet -f ivrit 'Hasky Spot !' | boxes -d dog -a hc -p h8 | lolcat -a -d 1 -s 300"))

        print(color.BOLD + color.RED +
              "                    I am NOT responsible for any damages caused or any crimes committed by using this tool.")
        print("\n")
        print(color.GREEN + "         version = 0.1 ")
        print("         author  = Vipul (Hasky)")
        print("         Github = https://github.com/vipulvyas/HaskySpot")

        print("         date = " + str(datetime.datetime.now()))
        print("\n")
        try:
            print(color.YELLOW + "             [1] Information Gathering")
            print("             [2] Scaning")
            print("             [3] Social Engineering")
            print("             [4] Sniffing")
            print("             [5] Denial Of Service Attack")
            print("             [6] exit")
            print('\n')
            option = input(color.GREEN + "Select: ")

            if option == '1':
                self.clear()
                infobanner.info_banner()
                print(color.CYAN + "             [1] Email Extracter")
                print("             [2] Whois Information")
                print("             [3] DNS Foot Printing")
                print("             [4] Sub Domain")
                print("             [5] Back")
                info_option = input(color.YELLOW + "Select: ")

                if info_option == '1':
                    emailfootprint.emailfoot.emailfootprint(self)
                elif info_option == '2':
                    whois.WhoisInfo.whoisInfo(self)
                elif info_option == '3':
                    dnsfootprint.DNSfoot.DNSfootprint(self)
                elif info_option == '4':
                    os.system("python3 ./info/subdomain.py")
                    # subdomain.subdomainclass()
                elif info_option == '5':
                    self.spot()
                else:
                    print("[!] invalid Selection")
                    self.spot()

            elif option == '2':
                self.clear()
                scanbanner.scanbanner()
                print(color.CYAN + "             [1] Prepare Proxy")
                print("             [2] Mac Spoofing")
                print("             [3] Network Scanning")
                print("             [4] Fire Wall Check (wefw00f)")
                print("             [5] Back")
                scan_option = input(color.YELLOW + "Select: ")
                if scan_option == '1':
                    preproxy.preproxy.torproxy(self)
                elif scan_option == '2':
                    macspf.macspoof.change_mac(self)
                elif scan_option == '3':
                    networkscan.networkscan.networkscaning(self)
                elif scan_option == '4':
                    firewallcheck.firewallcheck.firewall(self)
                elif scan_option == '5':
                    self.spot()
                else:
                    print("[!] invalid Selection")
                    self.spot()
            elif option == '3':
                self.clear()
                socialbanner.socialbanner()
                print(color.CYAN +
                      "             [1] Google Hackinng(Goodle Dorking)")
                print("             [2] Find Hidden Fields")
                print("             [3] Email Spoof")
                print("             [4] Back")
                social_option = input(color.YELLOW + "Select: ")
                if social_option == '1':
                    googlehacking.googlehacking.googlehack(self)
                elif social_option == '2':
                    hiddenfield.hiddenfield.hidden(self)
                elif social_option == '3':
                    self.clear()
                    os.system("python Send_mail.py")
                elif social_option == '4':
                    self.spot()
                else:
                    print("[!] invalid Selection")
                    self.spot()
            elif option == '4':
                self.clear()
                sniffbanner.sniffbanner()
                print(color.CYAN + "             [1] Sniff TCP/UDP/ICMP/HTTP traffic")
                print(color.CYAN + "             [2] Credential Sniff")
                print(color.CYAN + "             [3] Back")
                sniff_option = input(color.YELLOW + "Select: ")

                if sniff_option == '1':
                    os.system("sudo python3 ./sniff/sniffer.py")
                elif sniff_option == '2':
                    os.system("sudo python ./sniff/cred.py")
                elif sniff_option == '3':
                    self.spot()
                else:
                    print("[!] invalid Selection")
                    self.spot()
                print("4")
            elif option == '5':
                self.clear()
                dosbanner.dosbanner()
                print(color.CYAN + "             [1] Memcrashed DDOS")
                print("             [2] Ping Of Death")
                print("             [3] Port Changeing DDOS")
                print("             [4] Back")
                dos_option = input(color.YELLOW + "Select: ")

                if dos_option == '1':
                    os.system("sudo python3 ./dos/Memcrashed.py")
                   
                elif dos_option == '2':
                    os.system("sudo python3 ./dos/pingofdeath.py")
                    
                elif dos_option == '3':
                    pc.portchange.attack(self)
                elif dos_option == '4':
                    self.spot()
                else:
                    print("[!] invalid Selection")
                    self.spot()
            elif option == '6':
                print(color.GREEN + "Bye Bye")
                sys.exit(2)
            else:
                print(color.RED+"\n[!] Invalid Selection.")
                self.spot()
        except KeyboardInterrupt:
            print(color.RED+"\n[!] You Press Ctrl + C! To Quit.")
            sys.exit(1)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    hasky = Hasky()
    hasky.spot()
