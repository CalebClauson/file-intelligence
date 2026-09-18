from scanner import print_report, scan_directory, generate_report, is_valid_directory, json_dump

def run_terminal_ui():
    while True:
        print_main_menu()
        choice = request_menu_choice()
    
        if choice == "1":
            directory_path = request_directory()
            run_directory_scan(directory_path)
                
        elif choice == "2":
            return
        else:
            print("Invalid option. Please choose 1 or 2.")
    


def print_main_menu():
    print("\n\033[36m"
          "╔══════════════════════════════╗\n"
          "║      FILE INTELLIGENCE       ║\n"
          "╚══════════════════════════════╝"
          "\033[0m")
    print("  1. Scan a directory")
    print("  2. Exit")
    print()

def request_menu_choice():
    return input("Choose an option: ").strip()

def request_directory():
    return input("Enter folder path: ").strip()

def run_directory_scan(directory_path):
    if not is_valid_directory(directory_path):
        print("Invalid directory. Please enter an existing folder.")
    else:
        files = scan_directory(directory_path)
        report = generate_report(files, directory_path)
        print("\n\033[36m──────────────────────────────\033[0m")
        print_report(report)
        print("\n\033[36m──────────────────────────────\033[0m")
        export_choice(report)

def export_choice(report):
    export_choice = input("\nExport report as JSON? [y/N]: ").strip().lower()
    
    if export_choice == "y":
        json_dump(report)
        print("Report saved to output/report.json")
