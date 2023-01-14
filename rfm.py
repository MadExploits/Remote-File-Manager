#!/usr/bin/python3

import requests as req
from os import system, name
from colorama import *
from os.path import exists
from multiprocessing.dummy import Pool

# clear command line linux/windows
if name == "nt":
    system("cls")
else:
    system("clear")


def remote_file_manager(value):
    DIR = [
        '/assets/filemanager/',
        '/assets/file-manager/',
        '/assets/filemanagers/',
        '/assets/filemanager/dialog.php',
        '/asset/filemanager/dialog.php',
        '/asset/filemanager/',
        '/asset/file-manager/',
        '/asset/filemanagers/',
        '/filemanager/',
        '/filemanager/dialog.php'
        '/assets/admin/js/filemanager/',
        '/admin/assets/filemanager/',
        '/dashboard/assets/filemanager/',
        '/media/filemanager/dialog.php',
        '/assets/plugins/filemanager/dialog.php',
        '/assets/admin/js/tinymce/plugins/filemanager/dialog.php',
        '/plugins/filemanager/dialog.php',
        '/plugins/filemanager/',
        '/filemanager/',
        '/contents/filemanager/dialog.php',
        '/templates/filemanager/dialog.php',
        '/file-manager/dialog.php',
        '/fileman/dialog.php',
        '/vendor/filemanager/dialog.php',
        '/api/vendor/filemanager/',
        '/api/vendor/filemanager/dialog.php'
    ]
    # source from https://github.com/MadExploits/UserAgent-random
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
    }
    for x in range(0, len(DIR)):
        try:
            r = req.get(f"{value}{DIR[x]}", headers=header, timeout=30)
            if r.status_code == 200 and "File Manager" in r.text:
                print(Fore.GREEN + f"[+] {value}{DIR[0]}" + Style.RESET_ALL)
            else:
                pass
        except:
            pass

    print(Fore.RED + f"[!] {value} NOT FOUND" + Style.RESET_ALL)


def main():
    print(Fore.GREEN + """
    +----------[ REMOTE FILE MANAGER ]----------+ 
    + Github   : github.com/MadExploits         +
    + Telegram : t.me/@MadShells                +
    + Remote File Manager Scanner               +
    +-------------------------------------------+
    """ + Style.RESET_ALL)
    choosen = input("[!] Scan URL or List of URLs? [1/2]: ")
    if choosen == "1":
        URL = input("URL : ")
        U = [
            '{}'.format(URL)
        ]
        with Pool(int(120)) as Th:
            Th.map(remote_file_manager, U)
            Th.close()
            Th.join()
    elif choosen == "2":
        Lst = input("LIST : ")
        if exists(Lst):
            with open(Lst, "r") as L:
                read = L.read()
                pch = read.split("\n")
                with Pool(int(120)) as Ts:
                    Ts.map(remote_file_manager, pch)
                    Ts.close()
                    Ts.join()
        else:
            print(Fore.RED + f"\n[!] File Not Found!")
    else:
        print(Fore.RED + "\n[!] Please Choose Number 1/2")


if __name__ == "__main__":
    main()
