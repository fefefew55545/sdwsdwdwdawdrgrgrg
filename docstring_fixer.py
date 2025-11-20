#!/usr/bin/env python3
"""
Fix docstring syntax errors - convert """ to """
"""

from pathlib import Path

class DocstringFixer:
    """Fix docstring syntax errors"""

    def __init__(self):
        self.files_fixed = 0

    def fix_docstrings_in_file(self, file_path: Path) -> bool:
        """Fix docstrings in a single file"""
        if not file_path.exists():
            return False

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Fix the main issue: replace """ with """
            original_content = content
            content = content.replace('"""', '"""')

            # Also fix common docstring issues
            content = content.replace('"""\n', '"""\n')
            content = content.replace('"""\r', '"""\r')

            # Write back if changed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True

        except Exception as e:
            print(f"Error fixing {file_path}: {e}")

        return False

    def fix_all_docstrings(self):
        """Fix docstrings in all problematic files"""
        # Files with docstring issues
        problematic_files = [
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

        print("🔧 Fixing Docstring Syntax Errors")
        print("=" * 50)

        for file_path in problematic_files:
            full_path = Path(file_path)
            print(f"🔧 Fixing: {file_path}")

            if self.fix_docstrings_in_file(full_path):
                print(f"  ✅ Fixed docstring syntax")
                self.files_fixed += 1
            else:
                print(f"  ℹ️  No fixes needed")

        return self.files_fixed

def main():
    """Main fix function"""
    fixer = DocstringFixer()
    files_fixed = fixer.fix_all_docstrings()

    print(f"\n✅ Fixed docstring syntax in {files_fixed} files!")
    print("   All files should now have valid docstring syntax")

if __name__ == "__main__":
    main()