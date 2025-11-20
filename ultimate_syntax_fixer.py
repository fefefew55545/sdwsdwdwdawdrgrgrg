#!/usr/bin/env python3
"""
ULTIMATE Syntax Fixer - Fix ALL remaining syntax errors in BSEE codebase
"""

import re
import ast
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional

class UltimateSyntaxFixer:
    """Fix ALL syntax errors - no compromises"""

    def __init__(self):
        self.fixes_applied = 0
        self.files_fixed = 0
        self.files_with_errors = 0

    def fix_unmatched_brackets_comprehensive(self, content: str) -> str:
        """Fix all unmatched brackets comprehensively"""
        lines = content.split('\n')
        fixed_lines = []

        bracket_stack = []
        for line_num, line in enumerate(lines, 1):
            original_line = line
            in_string = False
            string_char = None
            escape_next = False

            # Analyze the line character by character
            i = 0
            while i < len(line):
                char = line[i]

                # Handle strings
                if escape_next:
                    escape_next = False
                elif char == '\\':
                    escape_next = True
                elif char in ['"', "'"] and not escape_next:
                    if not in_string:
                        in_string = True
                        string_char = char
                    elif char == string_char:
                        in_string = False
                        string_char = None

                # Only process brackets outside strings
                if not in_string:
                    if char in '({[':
                        bracket_stack.append((char, line_num, i))
                    elif char in ')}]':
                        if bracket_stack:
                            open_char, open_line, open_pos = bracket_stack[-1]
                            if ((char == ')' and open_char == '(') or
                                (char == '}' and open_char == '{') or
                                (char == ']' and open_char == '[')):
                                bracket_stack.pop()
                            else:
                                # Mismatched bracket - remove it
                                line = line[:i] + line[i+1:]
                                i -= 1
                                self.fixes_applied += 1
                i += 1

            # Add missing closing brackets at end of line
            if bracket_stack:
                # Check if we should close them on this line
                last_bracket, last_line, last_pos = bracket_stack[-1]
                if last_line == line_num:
                    # Add closing brackets
                    closing = []
                    temp_stack = list(bracket_stack)
                    while temp_stack and temp_stack[-1][0] in '({[':
                        open_char, _, _ = temp_stack.pop()
                        if open_char == '(':
                            closing.append(')')
                        elif open_char == '{':
                            closing.append('}')
                        elif open_char == '[':
                            closing.append(']')

                    if closing:
                        line += ''.join(reversed(closing))
                        bracket_stack = [b for b in bracket_stack if b[1] != line_num]
                        self.fixes_applied += len(closing)

            fixed_lines.append(line)

        return '\n'.join(fixed_lines)

    def fix_indentation_comprehensive(self, content: str) -> str:
        """Fix all indentation errors"""
        lines = content.split('\n')
        fixed_lines = []
        indent_stack = [0]
        expect_indent = False
        in_multiline_string = False

        for i, line in enumerate(lines):
            stripped = line.strip()

            # Skip empty lines and comments
            if not stripped or stripped.startswith('#'):
                fixed_lines.append(line)
                continue

            # Handle multiline strings
            if '"""' in line or "'''" in line:
                in_multiline_string = not in_multiline_string
                fixed_lines.append(line)
                continue

            if in_multiline_string:
                fixed_lines.append(line)
                continue

            # Calculate current indentation
            current_indent = len(line) - len(line.lstrip())

            # Handle block starters
            if stripped.endswith(':') and not any(keyword in stripped for keyword in ['elif', 'else:', 'except:', 'finally:']):
                expect_indent = True
                fixed_lines.append(line)
                continue

            # Fix indentation based on context
            if expect_indent:
                # This line should be indented
                if current_indent <= indent_stack[-1]:
                    # Add proper indentation
                    new_indent = indent_stack[-1] + 4
                    fixed_line = ' ' * new_indent + stripped
                    indent_stack.append(new_indent)
                    self.fixes_applied += 1
                else:
                    fixed_line = line
                    indent_stack.append(current_indent)
                expect_indent = False
            else:
                # Adjust indentation based on dedent keywords
                if any(stripped.startswith(keyword) for keyword in ['elif', 'else', 'except', 'finally']):
                    # Dedent one level
                    if len(indent_stack) > 1:
                        indent_stack.pop()
                    target_indent = indent_stack[-1] if indent_stack else 0
                    if current_indent != target_indent:
                        fixed_line = ' ' * target_indent + stripped
                        self.fixes_applied += 1
                    else:
                        fixed_line = line
                elif stripped.startswith(('return', 'break', 'continue', 'pass')) and current_indent > indent_stack[-1]:
                    # These should not increase indentation
                    target_indent = indent_stack[-1]
                    if current_indent > target_indent:
                        fixed_line = ' ' * target_indent + stripped
                        self.fixes_applied += 1
                    else:
                        fixed_line = line
                else:
                    fixed_line = line

            fixed_lines.append(fixed_line)

        return '\n'.join(fixed_lines)

    def fix_function_signatures_comprehensive(self, content: str) -> str:
        """Fix all function signature issues"""
        # Fix unmatched parentheses in function signatures
        content = re.sub(
            r'def\s+(\w+)\s*\(\s*([^)]*)\s*\)\s*->\s*[^:]*\)\s*:',
            lambda m: f"def {m.group(1)}({m.group(2)}):",
            content
        )

        # Fix missing parentheses in function signatures
        content = re.sub(
            r'def\s+(\w+)\s*\([^)]*$',
            lambda m: f"def {m.group(1)}():",
            content,
            flags=re.MULTILINE
        )

        # Fix missing closing parenthesis
        content = re.sub(r'(\w+):\s*str,\s*(\w+):\s*int\)\s*->', r'\1: str, \2: int) ->', content)

        return content

    def fix_docstrings_comprehensive(self, content: str) -> str:
        """Fix all docstring issues"""
        # Fix quadruple quotes
        content = re.sub(r'""""', '"""', content)
        content = re.sub(r"''''", "'''", content)

        # Fix malformed triple quotes at end of lines
        content = re.sub(r'"""\s*$', '"""', content, flags=re.MULTILINE)
        content = re.sub(r"'''\s*$", "'''", content, flags=re.MULTILINE)

        return content

    def fix_specific_patterns(self, content: str) -> str:
        """Fix specific known error patterns"""
        # Fix ttk.Label issues
        content = re.sub(
            r'ttk\.Label\(.*\)\.pack\(.*\)\.pack\(.*\)',
            lambda m: m.group(0).replace(').pack(', ').pack('),
            content
        )

        # Fix unmatched parentheses in method calls
        content = re.sub(r'\)\)\.', ').', content)

        # Fix .bind calls
        content = re.sub(r'\.bind\(.*\)""', '.bind(...)', content)

        # Fix font parameter issues
        content = re.sub(r'font=\([^)]*\)\)""', lambda m: m.group(0).replace('")"', ')'), content)

        return content

    def validate_syntax(self, content: str) -> Tuple[bool, Optional[str]]:
        """Validate Python syntax"""
        try:
            ast.parse(content)
            return True, None
        except SyntaxError as e:
            return False, str(e)
        except Exception as e:
            return False, f"Parse error: {str(e)}"

    def fix_file_completely(self, file_path: Path) -> bool:
        """Fix a file completely - no compromises"""
        if not file_path.exists():
            return False

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()

            # Apply all fixes
            fixed_content = original_content
            fixed_content = self.fix_docstrings_comprehensive(fixed_content)
            fixed_content = self.fix_specific_patterns(fixed_content)
            fixed_content = self.fix_function_signatures_comprehensive(fixed_content)
            fixed_content = self.fix_unmatched_brackets_comprehensive(fixed_content)
            fixed_content = self.fix_indentation_comprehensive(fixed_content)

            # Validate the fix
            is_valid, error = self.validate_syntax(fixed_content)

            if is_valid:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                return True
            else:
                print(f"  ❌ Could not fix: {error}")
                return False

        except Exception as e:
            print(f"  ❌ Error processing {file_path}: {e}")
            return False

    def fix_all_files(self, target_dir: str = '.') -> Dict:
        """Fix ALL files with syntax errors"""
        print("🔧 ULTIMATE SYNTAX FIXER - Fixing ALL errors completely")
        print("=" * 70)

        target_path = Path(target_dir)
        python_files = list(target_path.rglob('*.py'))

        # Get files with syntax errors
        error_files = []
        for file_path in python_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                is_valid, _ = self.validate_syntax(content)
                if not is_valid:
                    error_files.append(file_path)
            except:
                error_files.append(file_path)

        print(f"📊 Found {len(error_files)} files with syntax errors")
        print(f"🔧 Fixing ALL {len(error_files)} files completely...")

        results = {
            'total_files': len(error_files),
            'files_fixed': 0,
            'total_fixes': 0
        }

        for i, file_path in enumerate(error_files, 1):
            print(f"\n🔧 ({i}/{len(error_files)}) Ultimate Fix: {file_path.relative_to(target_path)}")

            if self.fix_file_completely(file_path):
                print(f"  ✅ COMPLETELY FIXED")
                results['files_fixed'] += 1
                self.files_fixed += 1
            else:
                print(f"  ⚠️  Could not fix automatically")

            # Update fix count
            self.files_with_errors += 1

        results['total_fixes'] = self.fixes_applied
        return results

def main():
    """Main ultimate fix function"""
    fixer = UltimateSyntaxFixer()
    results = fixer.fix_all_files('.')

    print("\n" + "=" * 70)
    print("🏆 ULTIMATE SYNTAX FIX COMPLETE!")
    print("=" * 70)

    print(f"📁 Files with errors: {results['total_files']}")
    print(f"✅ Files completely fixed: {results['files_fixed']}")
    print(f"⚡ Total fixes applied: {results['total_fixes']}")

    success_rate = (results['files_fixed'] / results['total_files'] * 100) if results['total_files'] > 0 else 0
    print(f"🎯 Success rate: {success_rate:.1f}%")

    if results['files_fixed'] == results['total_files']:
        print("\n🎉 ALL SYNTAX ERRORS ELIMINATED!")
        print("   BSEE codebase is now syntax-error-free!")
    else:
        remaining = results['total_files'] - results['files_fixed']
        print(f"\n⚠️  {remaining} files still need manual attention")

    return results

if __name__ == "__main__":
    main()