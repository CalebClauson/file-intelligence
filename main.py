from scanner import count_by_extension, count_files, format_largest_files, get_file_info, scan_directory, total_size, get_largest_files, build_largest_file_report, format_largest_files, export_report_json, hash_file, print_report_execute
from pathlib import Path
from terminal_ui import run_terminal_ui


if __name__ == "__main__":
    run_terminal_ui()