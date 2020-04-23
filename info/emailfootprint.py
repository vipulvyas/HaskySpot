import pyfiglet as pi
import os
import platform
import requests
from extract_emails import ExtractEmails
import main
class emailfoot:
	def emailfootprint(self):
		main.Hasky.clear(self)
		print('\n')
		print(os.system("figlet 'Email Extracter' -f digital -c"))
		try:
			url = input('             Enter The Domain Name (with http://  EX: http://example.com ):')
			em = ExtractEmails(url, depth=10, print_log=False, ssl_verify=True, user_agent="random", request_delay=0.0)
			emails = em.emails
			print(main.color.GREEN + '\n <-------------------------------------------------------------------------------------------->')
			if len(emails) != 0:
				for i in emails:
					print(i)
			else:
				print("				**	Email Not Found  **")
		except Exception:
			print("Invalid URL  :)")
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
    emailfoot = emailfoot()
    emailfoot.emailfootprint()
