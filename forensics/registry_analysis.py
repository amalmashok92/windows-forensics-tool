
import os
import winreg
from Registry import Registry

def extract_registry_info(hive_path=None):
    print("[*] Extracting Registry Information...")

    if hive_path and os.path.exists(hive_path):
        print(f"[*] Reading Offline Hive File: {hive_path}")
        reg = Registry.Registry(hive_path)
        try:
            key = reg.open("Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RunMRU")
            for value in key.values():
                print(f"{value.name()}: {value.value()}")
        except Registry.RegistryKeyNotFoundException:
            print("[!] Registry key not found in hive file.")
    else:
        print("[*] Reading Live Registry (HKEY_CURRENT_USER RunMRU)")
        try:
            reg_path = r"Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RunMRU"
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)
            i = 0
            while True:
                value = winreg.EnumValue(key, i)
                print(f"{value[0]}: {value[1]}")
                i += 1
        except OSError:
            print("[!] Registry key not found in live registry.")
