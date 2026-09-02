from scanner import get_file_info, scan_directory

files = scan_directory("/home/caleb/workspace/caleb_clauson")

# for file in files:
#     print(file)


for file in files[:10]:
    print(get_file_info(file))

# print("Total files:", len(files))
# print(files[:5])
