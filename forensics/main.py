import argparse
from forensics import registry_analysis, event_logs, browser_artifacts

def main():
    parser = argparse.ArgumentParser(description='Windows Forensics Tool')
    parser.add_argument('--registry', action='store_true', help='Collect registry artifacts')
    parser.add_argument('--hive-path', type=str, help='Path to offline registry hive (like NTUSER.DAT)')
    parser.add_argument('--reg-key', type=str, help='Registry key to extract (default is RunMRU)')
    parser.add_argument('--events', action='store_true', help='Collect event logs')
    parser.add_argument('--browser', action='store_true', help='Collect browser artifacts')

    args = parser.parse_args()

    if args.registry:
        registry_analysis.extract_registry_info(args.hive_path, args.reg_key)

    if args.events:
        event_logs.collect_event_logs()

    if args.browser:
        browser_artifacts.extract_browser_data()

if __name__ == '__main__':
    main()
