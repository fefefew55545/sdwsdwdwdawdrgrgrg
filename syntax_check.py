#!/usr/bin/env python3
"""
Syntax validation script for all Python files in BSEE project
"""
import py_compile
import sys
from pathlib import Path

def check_syntax(file_path):
    """Check syntax of a Python file."""
    try:
        py_compile.compile(file_path, doraise=True)
        return None, None
    except py_compile.PyCompileError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)

def main():
    print("BSEE Syntax Validation Report")
    print("=" * 50)

    # Find all Python files
    python_files = list(Path('.').rglob('*.py'))

    syntax_errors = []
    success_count = 0

    for file_path in python_files:
        is_valid, error = check_syntax(file_path)
        if is_valid is None:  # Success
            success_count += 1
        else:
            syntax_errors.append((str(file_path), error))

    print(f"Checked {len(python_files)} Python files")
    print(f"✓ {success_count} files have valid syntax")

    if syntax_errors:
        print(f"✗ {len(syntax_errors)} files have syntax errors:")
        print()

        for file_path, error in syntax_errors:
            print(f"SYNTAX ERROR: {file_path}")
            print(f"  {error}")
            print()

        return 1
    else:
        print("All Python files have valid syntax!")
        return 0

if __name__ == "__main__":
    sys.exit(main())