from scanner import count_files, get_file_info, scan_directory, total_size

files = scan_directory("/home/caleb/workspace/caleb_clauson")

# for file in files:
#     print(file)


# for file in files[:10]:
#     print(get_file_info(file))

print("Total size of files:", total_size(files))
print("Total files:", count_files(files))
# print("Total files:", len(files))
# print(files[:5])
