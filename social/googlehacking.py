import requests
import platform
import os
import sys
import webbrowser
import main
class googlehacking:

    def googlehack(self):
        main.Hasky.clear(self)
        print('\n')
        print(os.system("figlet 'Google Dorking' -f digital -c"))

        #nhoctrum.com
        print(main.color.YELLOW +'\n')
        print ("""
[ Google Hacking Menu ]
\t01) Directory Listing
\t02) Configuration Files
\t03) Database Files
\t04) Log Files
\t05) Backup and Old Files
\t06) Login Pages
\t07) SQL Errors
\t08) Publicly Exposed Documents
\t09) phpinfo()
\t10) Google Hacking Database
\t99) Back To Menu
\tOR) CTRL + C
	""")
        print(main.color.GREEN + "\n")


        try:
            choice = int(input('Select Option: '))
            print('\n')
            google_hacking = 'https://www.google.com/search?q='
            url = input("Enter URL (without http://): ")
        except ValueError:
            print ('[+] - Please enter a valid integer.')
            googlehacking.googlehack(self)
        except EOFError:
            print ('\n[+] - Exiting.')
            sys.exit()
        except KeyboardInterrupt:
            print ('\n[+] - Exiting.')
            sys.exit()
        if choice == 1:
            webbrowser.open_new_tab(google_hacking + 'site:' + url + '+intitle:index.of')
            googlehacking.googlehack(self)
        elif choice == 2:
            webbrowser.open_new_tab(google_hacking + 'site:' + url + '+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini')
            googlehacking.googlehack(self)
        elif choice == 3:
            webbrowser.open_new_tab(google_hacking + 'site:' + url + '+ext:sql+|+ext:dbf+|+ext:mdb')
            googlehacking.googlehack(self)
        elif choice == 4:
            webbrowser.open_new_tab(google_hacking + 'site:' + url + '+ext:log')
            googlehacking.googlehack(self)
        elif choice == 5:
            webbrowser.open_new_tab(google_hacking + 'site:' + url + ' intitle:"index of"+|+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup')
            googlehacking.googlehack(self)
        elif choice == 6:
            webbrowser.open_new_tab(google_hacking + 'site:' + url + '+inurl:login | admin | user | cpanel | account | moderator | /cp')
            googlehacking.googlehack(self)
        elif choice == 7:
            webbrowser.open_new_tab(google_hacking + 'site:' + url + '+intext:"sql+syntax+near"+|+intext:"syntax+error+has+occurred"+|+intext:"incorrect+syntax+near"+|+intext:"unexpected+end+of+SQL+command"+|+intext:"Warning:+mysql_connect()"+|+intext:"Warning:+mysql_query()"+|+intext:"Warning:+pg_connect()"')
            googlehacking.googlehack(self)
        elif choice == 8:
            webbrowser.open_new_tab(google_hacking + 'site:' + url + '+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv')
            googlehacking.googlehack(self)
        elif choice == 9:
            webbrowser.open_new_tab(google_hacking + 'site:' + url + '+ext:php+intitle:phpinfo+"published+by+the+PHP+Group"')
            googlehacking.googlehack(self)
        elif choice == 10:
            webbrowser.open_new_tab('https://www.exploit-db.com/google-hacking-database/')
            googlehacking.googlehack(self)
        elif choice == 99:
            main.Hasky.spot(self)
        else:
            print ('[!] - Unknown error has occured.')
            googlehacking.googlehack(self)

if __name__ == "__main__":
    gd = googlehacking()
    gd.googlehack()
