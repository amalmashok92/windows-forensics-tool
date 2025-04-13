from browser_history import get_history

def extract_browser_data():
    print("[*] Extracting Browser History")
    outputs = get_history()
    history = outputs.histories
    for item in history:
        print(f"URL: {item[1]} | Time: {item[0]}")
