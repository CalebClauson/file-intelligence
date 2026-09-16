from scanner import count_by_extension, count_files, format_largest_files, get_file_info, scan_directory, total_size, get_largest_files, build_largest_file_report, format_largest_files, export_report_json, hash_file, print_report_execute
from pathlib import Path
# sorted_counts = sorted(extension_counts.items(), key=lambda item: item[1], reverse=True)
# largest = build_largest_file_report(files)
# # for file in files:
# #     print(file)


# # for file in files[:10]:
# #     print(get_file_info(file))

# print("10 Largest:", largest)

test_path = Path("test_data")
files = scan_directory(test_path)

extension_counts = count_by_extension(files)
print(extension_counts)


export_report_json(files, test_path)
print_report_execute(files, test_path)