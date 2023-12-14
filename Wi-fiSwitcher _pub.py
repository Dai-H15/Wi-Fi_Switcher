import subprocess
import os
import time
os.system("cls")
s = "2"
subprocess.call("netsh wlan connect XXX")
print("\n現在: XXX")
try:
    while True:
        now = time.time()
        input("ネットワークを切り替える enter:")
        os.system("cls")
        if now+3 > time.time():
            print("しばらく経ってからやり直してください")
        else:
            if s == "1":
                s = "2"
                res = subprocess.call("netsh wlan connect XXX")
                while res != 0:
                    print("Disconnecting...")
                    subprocess.call("netsh wlan disconnect", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(2)
                    print("searching...")
                    subprocess.call("netsh wlan show network", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    print("reconnecting...")
                    res = subprocess.call("netsh wlan connect XXX")
                print("\n現在: XXX")
                print(res)
                continue
            if s == "2":
                s = "1"
                os.system("cls")
                res = subprocess.call("netsh wlan connect NNNNNN")
                while res != 0:
                    print("Disconnecting...")
                    subprocess.call("netsh wlan disconnect", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(2)
                    print("searching...")
                    subprocess.call("netsh wlan show network", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    print("reconnecting...")
                    time.sleep(1)
                    res = subprocess.call("netsh wlan connect NNNNNN")
                print("\n現在: NNNNNN")
                print(res)
except KeyboardInterrupt:
    os.system("cls")
