import heapq
from pathlib import Path
import hashlib

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
        "path": file_path,
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
        file_info = { "size": formatted_size, "unit": unit, "path": file_path}
        formatted_largest_files.append(file_info)
    return formatted_largest_files

def build_largest_file_report(files):
    largest_files = get_largest_files(files)
    sorted_files = sort_largest_files(largest_files)
    formatted_files = format_largest_files(sorted_files)
    return formatted_files

def hash_file(file_path):
    file_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            file_hash.update(chunk)
    return file_hash.hexdigest()

def find_duplicates(files):
    # a bit more complicated to try to not hash anything unneccessary  
    hash_groups = {}
    file_size_groups = {}
    duplicates = {}

    # Group files by size first
    for file in files:
        file_size = file.stat().st_size

        if file_size in file_size_groups:
            file_size_groups[file_size].append(file)
        else:
            file_size_groups[file_size] = [file]

    # Only hash files that share a size with another file
    for file_size in file_size_groups:
        grouped_files = file_size_groups[file_size]

        if len(grouped_files) == 1:
            continue

        for grouped_file in grouped_files:
            file_hash = hash_file(grouped_file)

            if file_hash in hash_groups:
                hash_groups[file_hash].append(grouped_file)
            else:
                hash_groups[file_hash] = [grouped_file]             
        
    # Keep only actual duplicate groups
    for file_hash, grouped_files in hash_groups.items():
        if len(grouped_files) > 1:
            duplicates[file_hash] = grouped_files
    
    return duplicates

def find_empty_directories(path):
    path = Path(path)
    empty_directories = []
    
    for directory in path.rglob("*"):
        if directory.is_dir():
            if not any(directory.iterdir()):
                empty_directories.append(directory)
        else:
            print("Not empty")
                
    return empty_directories

def generate_report():
    return

def print_report(report):
    return

