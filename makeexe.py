import subprocess
import os
import re


def make_exe():
    wifi1 = input("接続させたい1つ目のWi-FiのSSIDを入力してください: ")
    wifi2 = input("接続させたい2つ目のWi-FiのSSIDを入力してください: ")
    with open(os.path.join(os.getcwd(), "NetworkSwitcher_customed.py"), "w+", encoding="utf-8")as u:
        print("抽出")
        for fs in open(os.path.join(os.getcwd(), "NetworkSwitcher.py"), "r", encoding="utf-8").readlines():
            if re.search(r"#*+\s+SSID", fs) is not None:
                s = re.sub(r"#*+\s+SSID", f"current_ssid = '{wifi1}' if current_ssid == '{wifi2}' else '{wifi2}'\n", fs)
                print(f"置換:from→{fs}  to→{s}")
                u.write(s)
            else:
                u.write(fs)
    print("生成")
    print("\nキャッシュを使用: 1\nクリーン環境から作成: 2")
    howto = input("生成方法を選択 >>>")
    if howto == "1":
        print("\nキャッシュを使用")
        subprocess.run("pyinstaller NetworkSwitcher_customed.py --onefile --noconsole --splash ./statics/splash.png --i ./statics/data.png -n NetworkSwitcher")
    elif howto == "2":
        print("\nクリーン環境から作成")
        subprocess.run("pyinstaller NetworkSwitcher_customed.py --onefile --noconsole --splash ./statics/splash.png --i ./statics/data.png --clean -n NetworkSwitcher")
    else:
        return 1
    print("EXE作成完了")
    os.remove(os.path.join(os.getcwd(), "NetworkSwitcher_customed.py"))
    print("テスト起動\nコマンドプロンプトは閉じないでください")
    subprocess.run("./dist/NetworkSwitcher.exe")


print("initializing...")


while True:
    if subprocess.call("pip show pyinstaller") == 1:
        os.system('cls')
        print("おっと、Pyinstallerが必要ですが、インストールされていないようです")
        if input("インストールしますか? y/n : ") == "y":
            subprocess.call("pip install pyinstaller")
    else:
        os.system('cls')
        make_exe()
        if input("正常に動作しましたか？ y/n: ") != "y":
            print("再生成")
            continue
        break
