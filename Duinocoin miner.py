print("this is a modifaction of minimal pc miner")
print("modified by superpythonguy")
print("OPEN source grab code at https://github.com/superpythonguy/python_adventure.git")
import hashlib
import os
from socket import socket
import sys
import time
import ssl
import select
from json import load as jsonload
import requests
import random
time.sleep(1)
print("this is my first shot at a useful python project pls dont bully me :)")
print("could be more optimised for old PCs (yet to test)")
soc = socket()
rgreetings = ("Hello and thanks for using me Experimental duinocoin miner", "DUINOCOINSSS!!", "DuinoCoin made is a coin made by Revox and many others")
print(random.choice(rgreetings))

def current_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time

duinousername = input('your duino coin Username pls?\n> ')
diff_choice = input(
    'Use lower difficulty? (press y for rasp. PIs or old PCs) Y/N \n> ')
if diff_choice.lower == "n":
    UseLowerDiff = False
else:
    UseLowerDiff = True

def fetch_pools():
    while True:
        try:
            response = requests.get(
                "https://server.duinocoin.com/getPool"
            ).json()
            NODE_IP = response["ip"]
            PORT = response["port"]

            return NODE_IP, PORT
        except Exception as e:
            print (f'{current_time()} : Error retrieving mining node, retrying in 5s')
            time.sleep(5)

while True:
    try:
        print(f'{current_time()} : finding for fastest connection to the server')
        try:
            NODE_IP, PORT = fetch_pools()
        except Exception as e:
            NODE_IP = "server.duinocoin.com"
            PORT = 2813
            print(f'{current_time()} : getting default server port and address get ready to mine :)')
        soc.connect((str(NODE_IP), int(PORT)))
        print(f'{current_time()} : Fastest connection has been found')
        server_version = soc.recv(100).decode()
        print (f'{current_time()} : Server Version is: '+ server_version)
        while True:
            if UseLowerDiff:
                soc.send(bytes(
                    "JOB,"
                    + str(duinousername)
                    + ",MEDIUM",
                    encoding="utf8"))
            else:
                # Send job request
                soc.send(bytes(
                    "JOB,"
                    + str(duinousername),
                    encoding="utf8"))

            # Receive work
            job = soc.recv(1024).decode().rstrip("\n")
            # Split received data to job and difficulty
            job = job.split(",")
            difficulty = job[2]

            hashingStartTime = time.time()
            base_hash = hashlib.sha1(str(job[0]).encode('ascii'))
            temp_hash = None

            for result in range(100 * int(difficulty) + 1):
                # Calculate hash with difficulty
                temp_hash = base_hash.copy()
                temp_hash.update(str(result).encode('ascii'))
                ducos1 = temp_hash.hexdigest()

                if job[1] == ducos1:
                    hashingStopTime = time.time()
                    timeDifference = hashingStopTime - hashingStartTime
                    hashrate = result / timeDifference

                    soc.send(bytes(
                        str(result)
                        + ","
                        + str(hashrate)
                        + ",[miners name here]",
                        encoding="utf8"))

                    feedback = soc.recv(1024).decode().rstrip("\n")
                    if feedback == "GOOD":
                        print(f'{current_time()} : share is accepted',
                              result,
                              "Hashrate",
                              int(hashrate/1000),
                              "kH/s (unit used to measure hash per second)",
                              "Difficulty is",
                              difficulty)
                        break
                    elif feedback == "BAD":
                        print(f'{current_time()} : share is Rejected',
                              result,
                              "Hashrate",
                              int(hashrate/1000),
                              "kH/s",
                              "Difficulty is",
                              difficulty)
                        break

    except Exception as e:
        print(f'{current_time()} : Error occured: ' + str(e) + ", restarting in 3s.")
        time.sleep(3)
        os.execl(sys.executable, sys.executable, *sys.argv)