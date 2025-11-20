#!/usr/bin/env python3
"""
Critical Syntax Fixer for BSEE - Instant Fix for Batch File Closing Issue
"""

import re
from pathlib import Path
from typing import List, Tuple, Dict

class CriticalSyntaxFixer:
    """Fix critical syntax errors that prevent BSEE from starting"""

    def __init__(self):
        self.fixes_applied = 0

    def fix_unclosed_brackets(self, content: str) -> str:
        """Fix unclosed brackets and braces"""
        lines = content.split('\n')
        fixed_lines = []

        for line in lines:
            original_line = line
            # Count brackets
            open_parens = line.count('(') - line.count(')')
            open_brackets = line.count('[') - line.count(']')
            open_braces = line.count('{') - line.count('}')

            # Fix by adding missing closing brackets
            if open_parens > 0:
                line += ')' * open_parens
                self.fixes_applied += open_parens
            if open_brackets > 0:
                line += ']' * open_brackets
                self.fixes_applied += open_brackets
            if open_braces > 0:
                line += '}' * open_braces
                self.fixes_applied += open_braces

            fixed_lines.append(line)

        return '\n'.join(fixed_lines)

    def fix_misformatted_lists(self, content: str) -> str:
        """Fix malformed list syntax"""
        # Fix cases like:
        # directories = []
        #     item1,''
        #     item2,''
        # ]
        lines = content.split('\n')
        fixed_lines = []
        in_list = False
        list_indent = 0

        for i, line in enumerate(lines):
            # Detect malformed list
            if re.search(r'\[\s*$', line.rstrip()):
                in_list = True
                list_indent = len(line) - len(line.lstrip())
                fixed_lines.append(line)
                continue

            if in_list and line.strip() == ']':
                in_list = False
                fixed_lines.append(line)
                continue

            if in_list:
                # Fix malformed list items
                # Remove trailing commas and quotes that shouldn't be there
                fixed_line = re.sub(r",\s*''\s*$", ",", line)
                fixed_line = re.sub(r",\s*''\s*$", "", fixed_line)  # Remove if last item
                # Add proper indentation
                if line.strip():
                    current_indent = len(line) - len(line.lstrip())
                    if current_indent <= list_indent:
                        # Item is at same or lower level than list start
                        # Add proper indentation
                        fixed_line = ' ' * (list_indent + 4) + line.strip()

                fixed_lines.append(fixed_line)
            else:
                fixed_lines.append(line)

        return '\n'.join(fixed_lines)

    def fix_unclosed_quotes(self, content: str) -> str:
        """Fix unclosed triple quotes and regular quotes"""
        # Fix triple quotes
        content = re.sub(r'""""\s*$', '"""', content, flags=re.MULTILINE)
        content = re.sub(r'^\s*""""', '"""', content, flags=re.MULTILINE)

        # Fix unmatched quotes at end of lines
        lines = content.split('\n')
        fixed_lines = []

        for line in lines:
            # Count quotes (excluding escaped ones)
            single_quotes = line.count("'") - line.count("\\'")
            double_quotes = line.count('"') - line.count('\\"')

            # Fix by adding missing closing quote
            if single_quotes % 2 == 1:
                line += "'"
                self.fixes_applied += 1
            if double_quotes % 2 == 1:
                line += '"'
                self.fixes_applied += 1

            fixed_lines.append(line)

        return '\n'.join(fixed_lines)

    def fix_function_signatures(self, content: str) -> str:
        """Fix malformed function signatures"""
        # Fix cases like: def func(self, arg):""
        content = re.sub(r':\s*""\s*$', ':', content, flags=re.MULTILINE)

        # Fix cases like: def func(self, arg) -> Type):""
        content = re.sub(r'\)\s*->\s*[^:]+\)\s*""\s*$', ') -> None:', content, flags=re.MULTILINE)

        return content

    def fix_misplaced_punctuation(self, content: str) -> str:
        """Fix misplaced punctuation and syntax"""
        # Fix cases like: ):"" instead of ):
        content = re.sub(r'\)\s*""\s*$', ')', content, flags=re.MULTILINE)

        # Fix cases like: item,'' instead of item,
        content = re.sub(r',\s*""\s*$', ',', content, flags=re.MULTILINE)

        # Fix cases like: ]'' instead of ]
        content = re.sub(r'\]\s*""\s*$', ']', content, flags=re.MULTILINE)

        # Fix cases like: }'' instead of }
        content = re.sub(r'\}\s*""\s*$', '}', content, flags=re.MULTILINE)

        return content

    def fix_file(self, file_path: Path) -> bool:
        """Fix a single file, return True if changes were made"""
        if not file_path.exists():
            return False

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()

            fixed_content = original_content

            # Apply fixes in order
            fixed_content = self.fix_unclosed_quotes(fixed_content)
            fixed_content = self.fix_misplaced_punctuation(fixed_content)
            fixed_content = self.fix_function_signatures(fixed_content)
            fixed_content = self.fix_misformatted_lists(fixed_content)
            fixed_content = self.fix_unclosed_brackets(fixed_content)

            # Write back if changed
            if fixed_content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                return True

        except Exception as e:
            print(f"Error fixing {file_path}: {e}")

        return False

    def fix_all_critical_files(self) -> Dict[str, int]:
        """Fix all files with critical syntax errors"""
        # Files mentioned in syntax check output
        critical_files = [
            'legacy/setup_windows.py',
            'tests/test_error_detection.py',
            'tests/run_tests.py',
            'tests/gui_test_suite.py',
            'tests/run_phase4_tests.py',
            'tests/test_smoke.py',
            'tests/test_phase2_simple.py',
            'tests/fix_progress_tracker.py',
            'tests/test_ai_integration.py',
            'gui/panels/file_panel.py',
            'gui/panels/metrics_panel.py',
            'config/presets/__init__.py',
            'bsee/strategies/annealing_strategy.py',
            'bsee/strategies/heuristic_strategy.py',
            'bsee/strategies/genetic_strategy.py',
            'bsee/strategies/homogeneity_mcts_strategy.py',
            'bsee/strategies/mcts_strategy.py',
            'bsee/scoring/__init__.py',
            'bsee/scoring/scorer.py',
            'bsee/results/exporter.py',
            'bsee/results/formatter.py',
            'bsee/utils/validators.py',
            'bsee/policies/custom/multi_objective_policy.py',
            'bsee/policies/custom/__init__.py',
            'tests/error_tools/windows_simulator.py',
            'tests/error_tools/smart_fix_system.py',
            'tests/error_tools/error_detector.py',
            'tests/validation/component_validator.py'
        ]

        results = {
            'total_files': len(critical_files),
            'files_fixed': 0,
            'total_fixes': 0
        }

        print("🔧 Applying Critical Syntax Fixes")
        print("=" * 50)

        for file_path in critical_files:
            full_path = Path(file_path)
            print(f"🔧 Fixing: {file_path}")

            if self.fix_file(full_path):
                print(f"  ✅ Fixed syntax errors")
                results['files_fixed'] += 1
            else:
                print(f"  ℹ️  No fixes needed or failed to fix")

        results['total_fixes'] = self.fixes_applied
        return results

def main():
    """Main fix function"""
    fixer = CriticalSyntaxFixer()
    results = fixer.fix_all_critical_files()

    print("\n" + "=" * 50)
    print("📊 Critical Fix Summary:")
    print(f"  Total files processed: {results['total_files']}")
    print(f"  Files fixed: {results['files_fixed']}")
    print(f"  Total syntax fixes applied: {results['total_fixes']}")

    if results['files_fixed'] > 0:
        print("\n✅ Critical syntax fixes applied!")
        print("   BSEE.bat should now start without instant closing")
    else:
        print("\nℹ️  No critical fixes were needed")

if __name__ == "__main__":
    main()