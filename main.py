# Data collection program. Built for either stress testing or simple collection.

import time
import ping

def stress():
    print("starting...")
    time.sleep(3)
    instances = int(input("Input number of instances. The number must be greater than 0.(Number format)"))
    time.sleep(1)
    while instances != 0:
        ping = subprocess.Popen(['ping', localhost], stdout=subprocess.PIPE)
        pingresult = ping.stdout.read()
        pingresult = str(pingresult)
        

def data():
    print("starting...")
    

def regstart():
    print("This is the start block of code.")
    time.sleep(2)
    collection = input("Stress test or data collection? (ST or DC)")
    if collection == "st" or collection == "ST":
        print("OK")
        time.sleep(2)
        stress()
    elif collection == "dc" or collection == "DC":
        print("ok")
        time.sleep(2)
        data()
    else:
        print("Unrecognized input.")
        time.sleep(2)
        regstart()

regstart()
