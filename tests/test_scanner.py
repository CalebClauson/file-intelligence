from pathlib import Path
import json

from scanner import (format_size, scan_directory, get_file_info, count_files, total_size, count_by_extension, get_largest_files, group_by_size, filter_duplicates, find_duplicates, find_empty_directories, generate_report, json_dump,)


def test_format_size_bytes():
    result = format_size(500)
    assert result == (500, "B"), "format_size_byte ERROR"


def test_format_size_kilobytes():
    result = format_size(1500)
    assert result == (1.46, "KB"), "format_size_kilobyte ERROR"


def test_count_files():
    path = Path("tests/test_cases/test_data")
    files = scan_directory(path)
    result = count_files(files)
    assert result == (4), "count_files ERROR"


def test_count_by_extension():
    path = Path("tests/test_cases/test_data")
    files = scan_directory(path)
    result = count_by_extension(files)
    assert result == ({'.txt': 4}), "count_by_extension ERROR"


def test_count_by_extension_no_extension():
    path = Path("tests/test_cases/test_data_extension")
    files = scan_directory(path)
    result = count_by_extension(files)
    assert result == ({"": 1}), "count_by_extension_no_extension ERROR"

# TODO ISSUE NESTED ARENT SCANNED
# def test_scan_directory_finds_nested_files():
#     path = Path("tests/test_cases/test_data_nested")
#     result = scan_directory(path)
#     expected = [Path("tests/test_cases/test_data_nested/test.txt"), Path("tests/test_cases/test_data_nested/nested/test2.txt")]
    
#     assert result == expected, "scan_directory_finds_nested_files ERROR"


def test_get_file_info():
    file = Path("tests/test_cases/test_data/file1.txt")
    result = get_file_info(file)
    expected = {
    'name': 'file1.txt',
    'path': 'tests/test_cases/test_data/file1.txt',
    'extension': '.txt',
    'size': 17,
    }
    assert result == expected, "get_file_info ERROR"


def test_total_size():
    pass


def test_group_by_size():
    pass


def test_filter_duplicates():
    pass


def test_find_duplicates():
    pass


def test_find_empty_directories():
    pass


def test_get_largest_files():
    pass


def test_generate_report_contains_expected_keys():
    pass


def test_json_export_creates_report_file():
    pass