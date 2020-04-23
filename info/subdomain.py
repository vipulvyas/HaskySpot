import requests
from threading import Thread
from queue import Queue
import os, platform
q = Queue()


class subdomainclass:
    try:
        def scan_subdomains(self, domain):
            global q
            try:
                while True:
                    # get the subdomain from the queue
                    subdomain = q.get()
                    # scan the subdomain
                    url = f"http://{subdomain}.{domain}"
                    try:
                        requests.get(url)
                    except requests.ConnectionError:
                        pass
                    else:
                        #f.write(url)
                        print("		[+] Discovered subdomain:", url)

                    # we're done with scanning that subdomain

                    q.task_done()
            except KeyboardInterrupt:
                os.system("python3 main.py")

        def main_subdomain(self, domain, n_threads, wordlist):
            global q

            subdomains = open(wordlist).read().splitlines()
            # fill the queue with all the subdomains
            for subdomain in subdomains:
                q.put(subdomain)
            print("         <---------------------------------------------------->")
            try:
                for t in range(n_threads):
                    # start all threads

                    worker = Thread(
                        target=subdomainclass.scan_subdomains, args=(self, domain,))
                    worker.daemon = True
                    worker.start()
            except KeyboardInterrupt:
                print("User Entrupted :")
                
                    #f.close()
    except KeyboardInterrupt:
        os.system("exit")
if __name__ == "__main__":
    if platform.system() == 'Linux':
        os.system("clear")
    if platform.system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass
    try:
        print(os.system("figlet 'Sub Domain Finder' -f digital -c"))
        subdom = subdomainclass()
        domain = input(
            "	Enter Domain to scan for subdomains without protocol (e.g without 'http://' or 'https://'): ")
        wordlist = input(
            "	 Enter Word List(Default subdomain.txt): ") or "./info/subdomain.txt"
        num_threads = int(input("	Enter The Threads(default 10): ") or "10")
        #f = open(domain + ".txt", "a+")
        subdom.main_subdomain(domain, num_threads, wordlist)
        q.join()
    except KeyboardInterrupt:
        os.system("exit")