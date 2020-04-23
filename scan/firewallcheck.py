import main
import os
import sys
class firewallcheck:
	
	def firewall(self):
		main.Hasky.clear(self)
		domain = input("		Enter Domain:")
		print(os.system("wafw00f "+ domain))

		ans = input(main.color.CYAN + "             Back To manu(Y/N)")
		if( ans == 'Y' or ans == 'y'):
		    main.Hasky.spot(self)
		if( ans == 'N' or ans == 'n'):
		    exit(1)
		else:
		    print(main.color.RED + "Invalid Input :)")


if __name__ == "__main__":
	check = firewallcheck()
	check.firewall()
