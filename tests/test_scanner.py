from pathlib import Path
import json

from scanner import (format_size, scan_directory, get_file_info, count_files, total_size, count_by_extension, get_largest_files, group_by_size, filter_duplicates, find_duplicates, find_empty_directories, generate_report, json_dump, export_report_json)


def test_format_size_bytes():
    result = format_size(500)
    expected = (500, "B")
    assert result == expected, "format_size_byte ERROR"


def test_format_size_kilobytes():
    result = format_size(1500)
    expected = (1.46, "KB")
    assert result == expected, "format_size_kilobyte ERROR"


def test_count_files():
    path = Path("tests/test_cases/test_data")
    files = scan_directory(path)
    result = count_files(files)
    expected = 4
    assert result == expected, "count_files ERROR"


def test_count_by_extension():
    path = Path("tests/test_cases/test_data")
    files = scan_directory(path)
    result = count_by_extension(files)
    expected = {'.txt': 4}
    assert result == expected, "count_by_extension ERROR"


def test_count_by_extension_no_extension():
    path = Path("tests/test_cases/test_data_extension")
    files = scan_directory(path)
    result = count_by_extension(files)
    assert result == ({"": 1}), "count_by_extension_no_extension ERROR"

# TODO ISSUE NESTED ARENT SCANNED
def test_scan_directory_finds_nested_files():
     path = Path("tests/test_cases/test_data_nested")
     result = scan_directory(path)
     expected = [Path("tests/test_cases/test_data_nested/test.txt"), Path("tests/test_cases/test_data_nested/nested/test2.txt")]
    
     assert result == expected, "scan_directory_finds_nested_files ERROR"


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
    path = Path("tests/test_cases/test_data")
    files = scan_directory(path)
    result = total_size(files)
    expected = (65,'B')
    assert result == expected, "total_size ERROR"


def test_group_by_size():
    path = Path("tests/test_cases/test_data")
    files = scan_directory(path)
    result = group_by_size(files)
    expected = {
        10: [Path("tests/test_cases/test_data/duplicate2.txt"),Path("tests/test_cases/test_data/duplicate1.txt"),],
        28: [Path("tests/test_cases/test_data/file2.txt"),],
        17: [Path("tests/test_cases/test_data/file1.txt"),],
        }
    assert result == expected, "group_by_size ERROR"


def test_filter_duplicates():
    hash_groups = {
        "hash_a": [Path("tests/test_cases/test_data/duplicate2.txt"), Path("tests/test_cases/test_data/duplicate1.txt")],
        "hash_b": [Path("tests/test_cases/test_data/file2.txt")],
    }
    result = filter_duplicates(hash_groups)
    expected = {
            f'hash_a': [
            Path('tests/test_cases/test_data/duplicate2.txt'),
            Path('tests/test_cases/test_data/duplicate1.txt'),
     ],}
    assert result == expected, "filter_duplicates ERROR"


def test_find_duplicates():
    path = Path("tests/test_cases/test_data")
    files = scan_directory(path)
    result = find_duplicates(files)
    # hash : files matching hash
    expected = (
    {
        "b822f1cd2dcfc685b47e83e3980289fd5d8e3ff3a82def24d7d1d68bb272eb32": [
            "tests/test_cases/test_data/duplicate2.txt",
            "tests/test_cases/test_data/duplicate1.txt",
        ]
    })
    assert result == expected, "find_duplicates ERROR"


def test_find_empty_directories():
    path = Path("tests/test_cases/test_data")
    result = find_empty_directories(path)
    expected = ([
        'tests/test_cases/test_data/empty_folder'
    ])
    assert result == expected, "find_empty_directories ERROR"


def test_get_largest_files():
    path = Path("tests/test_cases/test_data")
    files = scan_directory(path)
    result = get_largest_files(files, 1)
    expected = [(
        28, Path('tests/test_cases/test_data/file2.txt')    
    )]
    assert result == expected, "get_largest_files ERROR"


def test_generate_report_contains_expected_keys():
    path = Path("tests/test_cases/test_data")
    files = scan_directory(path)
    result = generate_report(files, path)
    expected = {
        "path",
        "total_files",
        "total_size",
        "extensions",
        "largest_files",
        "duplicates",
        "empty_directories",
    }
    assert set(result.keys()) == expected, "generate_report_contains_expected_keys ERROR"


def test_json_export_creates_report_file():
    output_path = Path("output/report.json")
    path = Path("tests/test_cases/test_data")
    files = scan_directory(path)

    if output_path.exists():
        output_path.unlink()
        
    export_report_json(files, path)
    assert output_path.is_file(), "json_export_creates_report_file ERROR"
