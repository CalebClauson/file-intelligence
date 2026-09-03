from pathlib import Path


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
    units = ["B", "KB", "MB", "GB", "TB"]
    unit_index = 0
    total_size = 0
    for file in files:
        total_size += file.stat().st_size

    while total_size >= 1024 and unit_index < len(units) - 1:
        total_size = total_size / 1024
        unit_index += 1

    total_size = round(total_size, 2)
    return total_size, units[unit_index]
