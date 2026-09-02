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
