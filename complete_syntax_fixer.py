#!/usr/bin/env python3
"""
Complete Syntax Fixer - Fix ALL remaining syntax errors in BSEE codebase
"""

import re
import ast
from pathlib import Path
from typing import List, Tuple, Dict

class CompleteSyntaxFixer:
    """Fix all remaining syntax errors in BSEE"""

    def __init__(self):
        self.fixes_applied = 0
        self.files_fixed = 0

    def fix_unmatched_parentheses(self, content: str) -> str:
        """Fix unmatched parentheses, brackets, and braces"""
        lines = content.split('\n')
        fixed_lines = []

        for line in lines:
            original_line = line

            # Count different types of brackets
            open_parens = line.count('(') - line.count(')')
            open_brackets = line.count('[') - line.count(']')
            open_braces = line.count('{') - line.count('}')

            # Fix unmatched parentheses (common in function signatures)
            if open_parens > 0:
                # Look for specific patterns like "total_cost: float, total_operations: int) -> None:"
                if re.search(r'->\s*None:\s*$', line):
                    line = line.rstrip().rstrip(')') + ')'  # Add missing parent
                    self.fixes_applied += 1
                elif open_parens > 0:
                    line += ')' * open_parens
                    self.fixes_applied += open_parens

            # Fix unmatched brackets (common in lists)
            if open_brackets > 0:
                line += ']' * open_brackets
                self.fixes_applied += open_brackets

            # Fix unmatched braces
            if open_braces > 0:
                line += '}' * open_braces
                self.fixes_applied += open_braces

            # Fix specific error patterns
            line = self.fix_specific_patterns(line)

            if line != original_line:
                self.fixes_applied += 1

            fixed_lines.append(line)

        return '\n'.join(fixed_lines)

    def fix_specific_patterns(self, line: str) -> str:
        """Fix specific known error patterns"""
        # Fix font=("TkDefaultFont", 16, "bold"))"" -> font=("TkDefaultFont", 16, "bold")
        line = re.sub(r'\)\s*""\s*$', ')', line)

        # Fix .pack(anchor=tk.W)).pack(...) -> .pack(anchor=tk.W).pack(...)
        line = re.sub(r'\)\s*\)\.pack\(', ').pack(', line)

        # Fix extra quotes at end: action: str, result: str, details: str = ""):"
        line = re.sub(r'=\s*""\s*\)\s*:', '):', line)

        # Fix ): at end of function definitions
        line = re.sub(r'\)\s*""\s*$', ')', line)

        return line

    def fix_indentation_errors(self, content: str) -> str:
        """Fix basic indentation errors"""
        lines = content.split('\n')
        fixed_lines = []

        for i, line in enumerate(lines):
            # Skip empty lines and comments
            if not line.strip() or line.strip().startswith('#'):
                fixed_lines.append(line)
                continue

            # Basic indentation fixes
            if line.startswith(' ') and not line.startswith('    '):
                # Convert inconsistent spacing to 4-space multiples
                leading_spaces = len(line) - len(line.lstrip())
                correct_spaces = (leading_spaces // 4) * 4
                fixed_line = ' ' * correct_spaces + line.lstrip()
                if fixed_line != line:
                    self.fixes_applied += 1
                fixed_lines.append(fixed_line)
            else:
                fixed_lines.append(line)

        return '\n'.join(fixed_lines)

    def fix_function_signatures(self, content: str) -> str:
        """Fix malformed function signatures"""
        lines = content.split('\n')
        fixed_lines = []

        for line in lines:
            original_line = line

            # Fix cases like: def func(self, arg):""
            line = re.sub(r':\s*""\s*$', ':', line)

            # Fix cases like: def func(self, arg) -> Type):""
            line = re.sub(r'\)\s*->\s*[^:]+\)\s*""\s*$', ') -> None:', line)

            if line != original_line:
                self.fixes_applied += 1

            fixed_lines.append(line)

        return '\n'.join(fixed_lines)

    def try_parse_ast(self, content: str) -> bool:
        """Try to parse content as AST to check if syntax is valid"""
        try:
            ast.parse(content)
            return True
        except SyntaxError:
            return False

    def fix_file(self, file_path: Path) -> bool:
        """Fix syntax errors in a single file"""
        if not file_path.exists():
            return False

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()

            fixed_content = original_content

            # Apply fixes in order
            fixed_content = self.fix_unmatched_parentheses(fixed_content)
            fixed_content = self.fix_function_signatures(fixed_content)
            fixed_content = self.fix_indentation_errors(fixed_content)

            # Try to parse to check if we fixed it
            if self.try_parse_ast(fixed_content):
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                return True
            else:
                print(f"  ⚠️  Could not fix syntax in {file_path}")
                return False

        except Exception as e:
            print(f"  ❌ Error fixing {file_path}: {e}")
            return False

    def fix_all_remaining_files(self):
        """Fix all files with remaining syntax errors"""
        # Files that still have syntax errors based on latest check
        problematic_files = [
            'docstring_fixer.py',  # Remove this broken file
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

        print("🔧 Fixing ALL Remaining Syntax Errors")
        print("=" * 60)

        # Remove broken docstring_fixer.py file
        broken_file = Path('docstring_fixer.py')
        if broken_file.exists():
            broken_file.unlink()
            print("🗑️  Removed broken docstring_fixer.py")

        results = {
            'total_files': len(problematic_files),
            'files_fixed': 0,
            'total_fixes': 0
        }

        for file_path in problematic_files:
            if file_path == 'docstring_fixer.py':
                continue

            full_path = Path(file_path)
            print(f"🔧 Fixing: {file_path}")

            if self.fix_file(full_path):
                print(f"  ✅ Fixed syntax errors")
                results['files_fixed'] += 1
            else:
                print(f"  ⚠️  Could not fix automatically")

        results['total_fixes'] = self.fixes_applied
        return results

def main():
    """Main fix function"""
    fixer = CompleteSyntaxFixer()
    results = fixer.fix_all_remaining_files()

    print("\n" + "=" * 60)
    print("📊 Complete Syntax Fix Summary:")
    print(f"  Total files processed: {results['total_files']}")
    print(f"  Files successfully fixed: {results['files_fixed']}")
    print(f"  Total syntax fixes applied: {results['total_fixes']}")

    if results['files_fixed'] > 0:
        print("\n✅ Additional syntax fixes applied!")
        print("   BSEE codebase should now have minimal syntax errors")

if __name__ == "__main__":
    main()