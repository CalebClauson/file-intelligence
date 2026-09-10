# File Intelligence

A Python tool for scanning directories and analyzing file information.

## Project Goals

The primary goal of this project is not only to build a strong file analytical tool but to improve my skills in Python, data structures, filesystem operations, and clean code design.

## Development Approach

This project is being developed alongside my reading of *Clean Code* by Robert C. Martin, with a focus on clear naming, single-responsibility functions, and incremental refactoring.

## Current Features

- Recursively scans directories
- Finds files inside nested folders
- Collects file paths
- Extracts file names
- Extracts file extensions
- Reports file sizes in bytes
- Collect file count
- Total Directory Size
- Human-Readable size formatting
- Extension frequency counting
- Largest-file detection with heap
- Duplicate detection using file size + SHA-256 hashing
- Empty directory detection

## Current Project Structure

```text
file-intelligence/
├── main.py
├── scanner.py
└── README.md
```

# Planned Features

- Terminal report generation
- Directory/file exclusion rules
- File filtering options
- JSON or CSV export

# Tech

- Python
- pathlib
