import heapq
from pathlib import Path
import hashlib
import json

# Helpers
def format_size(bytes):
    units = ["B", "KB", "MB", "GB", "TB"]
    unit_index = 0
    while bytes >= 1024 and unit_index < len(units) - 1:
        bytes = bytes / 1024
        unit_index += 1
    return round(bytes, 2), units[unit_index]

# Primary Functions
def scan_directory(path):
    path = Path(path)
    scan_results = []
    for item in path.rglob("*"):
        if item.is_file():
            scan_results.append(item)
    return scan_results


def get_file_info(file_path):
    file_path = Path(file_path)
    file_info = {
        "name": file_path.name,
        "path": str(file_path),
        "extension": file_path.suffix,
        "size": file_path.stat().st_size,
    }
    return file_info


def count_files(files):
    return len(files)


def total_size(files):
    total_size = 0
    for file in files:
        total_size += file.stat().st_size
    return format_size(total_size)
    


def count_by_extension(files):
    file_type = {}
    for file in files:
        extension = file.suffix
        file_type[extension] = file_type.get(extension, 0) + 1
    return file_type

# Large File Cluster Functions
def get_largest_files(files, limit=10):
    largest_files = []
    for file in files:
        file_size = file.stat().st_size
        entry = (file_size, file)
        if len(largest_files) < limit:
            heapq.heappush(largest_files, entry)
        elif file_size > largest_files[0][0]:
            heapq.heapreplace(largest_files, entry)
    return largest_files

def sort_largest_files(largest_files):
    heap_copy = largest_files.copy()
    sorted_largest_files = []
    while heap_copy:
        sorted_largest_files.append(heapq.heappop(heap_copy))
    sorted_largest_files.reverse()
    return sorted_largest_files

def format_largest_files(sorted_largest_files):
    formatted_largest_files = []
    for file_size, file_path in sorted_largest_files:
        formatted_size, unit = format_size(file_size)
        file_info = { "size": formatted_size, "unit": unit, "path": str(file_path)}
        formatted_largest_files.append(file_info)
    return formatted_largest_files

def build_largest_file_report(files):
    largest_files = get_largest_files(files)
    sorted_files = sort_largest_files(largest_files)
    formatted_files = format_largest_files(sorted_files)
    return formatted_files

# Cluster End

def hash_file(file_path):
    file_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            file_hash.update(chunk)
    return file_hash.hexdigest()


# Dupe Cluster of functions
def group_by_size(files):
    file_size_groups = {}
    for file in files:
        file_size = file.stat().st_size

        if file_size in file_size_groups:
            file_size_groups[file_size].append(file)
        else:
            file_size_groups[file_size] = [file]
    return file_size_groups

def hash_duplicates(file_size_groups):
    hash_groups = {}
    
    for group in file_size_groups.values():
        if len(group) == 1:
            continue
    
        for file in group:
            file_hash = hash_file(file)
    
            if file_hash in hash_groups:
                hash_groups[file_hash].append(file)
            else:
                hash_groups[file_hash] = [file]
    
    return hash_groups 
            
def filter_duplicates(hash_groups):
    duplicates = {}

    for file_hash, grouped_files in hash_groups.items():
        if len(grouped_files) > 1:
            duplicates[file_hash] = grouped_files

    return duplicates

def format_duplicate_paths(duplicates):
    formatted_duplicates = {}

    for file_hash, grouped_files in duplicates.items():
        formatted_duplicates[file_hash] = [
            str(file) for file in grouped_files
        ]

    return formatted_duplicates

def find_duplicates(files):
    file_size_groups = group_by_size(files)
    hash_groups = hash_duplicates(file_size_groups)
    duplicates = filter_duplicates(hash_groups)
    formatted_duplicates = format_duplicate_paths(duplicates)

    return formatted_duplicates

# Cluster End
    

def find_empty_directories(path):
    path = Path(path)
    empty_directories = []
    
    for directory in path.rglob("*"):
        if directory.is_dir():
            if not any(directory.iterdir()):
                empty_directories.append(str(directory))
                
    return empty_directories

def generate_report(files, path):
    report = {
        "path": str(path),
        "total_files": count_files(files),
        "total_size": total_size(files),
        "extensions": count_by_extension(files),
        "largest_files": build_largest_file_report(files),
        "duplicates": find_duplicates(files),
        "empty_directories": find_empty_directories(path)
    }
    return report

def print_report(report):
    for key, value in report.items():
        print(f"{key}: {value}")

def print_report_execute(files, path):
    report = generate_report(files, path)
    print_report(report)

def json_dump(report):
    output_path = Path("output/report.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

def export_report_json(files, path):
    report = generate_report(files, path)
    json_dump(report)
    print("Report has been generated...")
    
