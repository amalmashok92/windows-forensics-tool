import os
import winreg
from Registry import Registry

def extract_registry_info(hive_path=None, registry_key=None):
    print("[*] Extracting Registry Information...")

    if not registry_key:
        registry_key = r"Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RunMRU"

    if hive_path and os.path.exists(hive_path):
        print(f"[*] Reading Offline Hive File: {hive_path}")
        reg = Registry.Registry(hive_path)
        try:
            key = reg.open(registry_key)
            for value in key.values():
                print(f"{value.name()}: {value.value()}")
        except Registry.RegistryKeyNotFoundException:
            print(f"[!] Key not found in hive file: {registry_key}")

    else:
        print("[*] Reading Live Registry")
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_key)
            i = 0
            while True:
                value = winreg.EnumValue(key, i)
                print(f"{value[0]}: {value[1]}")
                i += 1
        except OSError:
            print(f"[!] Key not found in live registry: {registry_key}")
