from bs4 import BeautifulSoup
import requests
import os
import main
class hiddenfield:
    def hidden(self):
        main.Hasky.clear(self)
        print('\n')
        print(os.system("figlet 'Hidden Field Scrapper' -f digital -c"))
        try:
            url = input("Enter The Url: ")
            page = requests.get(url)
        except Exception:
            print("Some thing went wrong try later")
        else:
            res = BeautifulSoup(page.content,"html.parser")
            tags = res.findAll("input", {"type": "hidden"})
            i=0
            print(main.color.GREEN + '\n <-------------------------------------------------------------------------------------------->')
            
            with open(url[8:] + '.txt','a') as f:
                for tag in tags:
                    i+=1
                    f.writelines(str(tag))
                    print(main.color.CYAN)
                    print(i," ) " + str(tag))
                    print(main.color.GREEN + '\n <-------------------------------------------------------------------------------------------->')
                f.close()
            
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
    h = hiddenfield()
    h.hidden()