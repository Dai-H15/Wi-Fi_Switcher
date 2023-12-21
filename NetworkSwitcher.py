import subprocess
import tkinter as tk
from tkinter import messagebox
import time
import pyi_splash
import re


def GetSSID():
    return re.search(r'SSID \d+ : (\S+)', subprocess.check_output("netsh wlan show network").decode('utf-8', errors='ignore'))[1]


current_ssid = GetSSID()


def connect_wifi(ssid):
    global current_ssid
    status_label.config(text=f"接続しています: {ssid}")
    status_label.update_idletasks()
    res = subprocess.call(f"netsh wlan connect {ssid}", shell=True)
    c = 0
    if res != 0:
        while (res != 0) and (c < 5):
            c += 1
            status_label.config(text="接続に失敗しました")
            status_label.update_idletasks()
            time.sleep(1)
            status_label.config(text="Disconnecting...")
            status_label.update_idletasks()
            subprocess.call("netsh wlan disconnect", shell=True)
            status_label.config(text="searching...")
            status_label.update_idletasks()
            time.sleep(2)
            subprocess.call("netsh wlan show network", shell=True)
            status_label.config(text="reconnecting...")
            status_label.update_idletasks()
            res = subprocess.call(f"netsh wlan connect {ssid}", shell=True)
        if res != 0:
            messagebox.showerror("接続失敗", "接続に失敗しました。\nSSIDを見直し、WiFiが使用可能か確認してください")
            switch_network()
    status_label.config(text=f"現在接続しているネットワーク: {current_ssid}")
    status_label.update_idletasks()


def switch_network():
    global current_ssid, last_attempt_time
    now = time.time()

    if last_attempt_time and now - last_attempt_time < 2:
        messagebox.showerror("エラー", "しばらく経ってからやり直してください")
        return
    # SSID
    last_attempt_time = now
    status_label.config(text="")
    status_label.update_idletasks()
    connect_wifi(current_ssid)


root = tk.Tk()
root.title("Wi-Fi Switcher")
root.geometry("270x80")
root.resizable(False, False)
root.attributes('-topmost', True)

last_attempt_time = None
status_label = tk.Label(root, text=f"現在のSSID: {GetSSID()}")
status_label.pack()

switch_button = tk.Button(root, text="ネットワークを切り替える", command=switch_network)
switch_button.place(x=135, y=40)
pyi_splash.close()
switch_network()

root.mainloop()
