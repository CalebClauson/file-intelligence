from pathlib import Path
import json

# would like to make a full execution that runs all test cases and does a scoring system; IF failed append to a list or container to print and SUBTRACT from 100 - 1.

from scanner import (format_size, scan_directory, get_file_info, count_files, total_size, count_by_extension, get_largest_files, group_by_size, filter_duplicates, find_duplicates, find_empty_directories, generate_report, json_dump,)

score = 100
error = []

def test_format_size_bytes():
    result = format_size(500)
    assert result == (500, "B"), "format_size_byte ERROR"


def test_format_size_kilobytes():
    result = format_size(1500)
    assert result == (1.46, "KB"), "format_size_kilobyte ERROR"


def test_count_files():
    pass


def test_count_by_extension():
    pass


def test_count_by_extension_no_extension():
    pass


def test_scan_directory_finds_nested_files():
    pass


def test_get_file_info():
    pass


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