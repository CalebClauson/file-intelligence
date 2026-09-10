from scanner import count_by_extension, count_files, format_largest_files, get_file_info, scan_directory, total_size, get_largest_files, build_largest_file_report, format_largest_files


files = scan_directory("/home/caleb/workspace/caleb_clauson")
extension_counts = count_by_extension(files)
sorted_counts = sorted(extension_counts.items(), key=lambda item: item[1], reverse=True)
largest = build_largest_file_report(files)
# for file in files:
#     print(file)


# for file in files[:10]:
#     print(get_file_info(file))

print("Total size of files:", total_size(files))
print("Total files:", count_files(files))
# print("Total files:", len(files))
# print(files[:5])

# Sorted Arrangment
for extension, count in sorted_counts:
    label = extension if extension else "No extension"
    print(f"{label}: {count}")

print("10 Largest:", largest)