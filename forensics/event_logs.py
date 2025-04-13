import win32evtlog

def collect_event_logs():
    print("[*] Collecting Windows Event Logs: Application Log")
    server = 'localhost'
    log_type = 'Application'

    hand = win32evtlog.OpenEventLog(server, log_type)
    total = win32evtlog.GetNumberOfEventLogRecords(hand)

    events = win32evtlog.ReadEventLog(hand, win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)

    for event in events:
        print(f"Event Category: {event.EventCategory} | Source: {event.SourceName} | Event ID: {event.EventID}")
