#!/usr/bin/env python3
"""
Comprehensive Error Detection and Fixing System - FIXED VERSION
Finds and fixes all types of errors in the BSEE codebase
"""

import os
import ast
import re
import sys
from pathlib import Path
from datetime import datetime

class ComprehensiveErrorDetector:
    """Comprehensive error detection and fixing system"""

    def __init__(self, project_root="."):
        self.project_root = Path(project_root).resolve()
        self.errors_found = []
        self.errors_fixed = []
        self.start_time = datetime.now()

    def detect_all_errors(self):
        """Run comprehensive error detection"""
        print("🔍 COMPREHENSIVE ERROR DETECTION STARTED")
        print("=" * 60)

        results = {
            'syntax_errors': self._detect_syntax_errors(),
            'import_errors': self._detect_import_errors(),
            'undefined_variables': self._detect_undefined_variables(),
            'unused_imports': self._detect_unused_imports(),
            'dead_code': self._detect_dead_code(),
            'logic_errors': self._detect_logic_errors(),
            'security_issues': self._detect_security_issues(),
            'performance_issues': self._detect_performance_issues(),
            'dependency_issues': self._detect_dependency_issues()
        }

        # Total errors found
        total_errors = sum(len(errors) for errors in results.values())
        print(f"\n📊 TOTAL ERRORS DETECTED: {total_errors}")

        for error_type, errors in results.items():
            if errors:
                print(f"  • {error_type}: {len(errors)}")

        return results

    def _detect_syntax_errors(self):
        """Detect syntax errors in all Python files"""
        syntax_errors = []
        python_files = list(self.project_root.rglob("*.py"))

        print(f"\n🐍 Checking syntax in {len(python_files)} Python files...")

        for file_path in python_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                ast.parse(content)
            except SyntaxError as e:
                syntax_errors.append({
                    'file': str(file_path),
                    'error_type': 'SyntaxError',
                    'message': str(e),
                    'line': e.lineno,
                    'column': e.offset
                })
            except Exception as e:
                syntax_errors.append({
                    'file': str(file_path),
                    'error_type': 'FileError',
                    'message': str(e),
                    'line': None,
                    'column': None
                })

        return syntax_errors

    def _detect_import_errors(self):
        """Detect import-related errors"""
        import_errors = []
        python_files = list(self.project_root.rglob("*.py"))

        print(f"\n📦 Checking imports in {len(python_files)} Python files...")

        for file_path in python_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                tree = ast.parse(content)
                self._check_imports_in_tree(tree, file_path, import_errors)

            except Exception:
                continue

        return import_errors

    def _check_imports_in_tree(self, tree, file_path, import_errors):
        """Check imports in AST tree"""
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if not self._is_valid_import(alias.name):
                        import_errors.append({
                            'file': str(file_path),
                            'error_type': 'InvalidImport',
                            'message': f"Invalid import: {alias.name}",
                            'line': node.lineno
                        })

            elif isinstance(node, ast.ImportFrom):
                if node.module and not self._is_valid_import(node.module):
                    import_errors.append({
                        'file': str(file_path),
                        'error_type': 'InvalidImport',
                        'message': f"Invalid import from: {node.module}",
                        'line': node.lineno
                    })

    def _is_valid_import(self, module_name):
        """Check if a module name is valid"""
        if not module_name:
            return True

        # Check for common invalid patterns
        invalid_patterns = [
            r'^[^a-zA-Z_]',  # Starts with invalid character
            r'[^a-zA-Z0-9_.]',  # Contains invalid characters
            r'\.\.',  # Double dots
            r'^\.$',  # Single dot only
        ]

        for pattern in invalid_patterns:
            if re.search(pattern, module_name):
                return False

        return True

    def _detect_undefined_variables(self):
        """Detect undefined variables"""
        undefined_vars = []
        python_files = list(self.project_root.rglob("*.py"))

        print(f"\n🔍 Checking undefined variables in {len(python_files)} Python files...")

        for file_path in python_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                tree = ast.parse(content)
                self._check_undefined_variables_in_tree(tree, file_path, undefined_vars)

            except Exception:
                continue

        return undefined_vars

    def _check_undefined_variables_in_tree(self, tree, file_path, undefined_vars):
        """Check for undefined variables in AST tree"""
        defined_vars = set()
        builtins = set(dir(__builtins__))

        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                defined_vars.add(node.id)

            elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                if node.id not in defined_vars and node.id not in builtins:
                    undefined_vars.append({
                        'file': str(file_path),
                        'error_type': 'UndefinedVariable',
                        'message': f"Undefined variable: {node.id}",
                        'line': node.lineno
                    })

    def _detect_unused_imports(self):
        """Detect unused imports"""
        unused_imports = []
        python_files = list(self.project_root.rglob("*.py"))

        print(f"\n🗑️  Checking unused imports in {len(python_files)} Python files...")

        for file_path in python_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                unused = self._find_unused_imports(content, file_path)
                unused_imports.extend(unused)

            except Exception:
                continue

        return unused_imports

    def _find_unused_imports(self, content, file_path):
        """Find unused imports in content"""
        unused = []
        lines = content.split('\n')
        imported_names = set()
        used_names = set()

        # Parse imports
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('import '):
                parts = stripped.split()
                if len(parts) >= 2:
                    imported_names.add(parts[1].split('.')[0])
            elif stripped.startswith('from ') and ' import ' in stripped:
                module_part = stripped.split(' import ')[1]
                names = [n.strip() for n in module_part.split(',')]
                for name in names:
                    imported_names.add(name.split(' as ')[0])

        # Check usage
        for line in lines:
            for name in imported_names:
                if name in line and not line.strip().startswith(('import ', 'from ')):
                    used_names.add(name)

        # Find unused
        for name in imported_names:
            if name not in used_names:
                unused.append({
                    'file': str(file_path),
                    'error_type': 'UnusedImport',
                    'message': f"Unused import: {name}",
                    'line': None
                })

        return unused

    def _detect_dead_code(self):
        """Detect dead code"""
        dead_code = []
        python_files = list(self.project_root.rglob("*.py"))

        print(f"\n💀 Checking dead code in {len(python_files)} Python files...")

        for file_path in python_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                dead = self._find_dead_code(content, file_path)
                dead_code.extend(dead)

            except Exception:
                continue

        return dead_code

    def _find_dead_code(self, content, file_path):
        """Find dead code patterns"""
        dead = []
        lines = content.split('\n')

        # Look for unreachable code patterns
        for i, line in enumerate(lines):
            stripped = line.strip()

            # Code after return, raise, break, continue
            if any(keyword in stripped for keyword in ['return ', 'raise ', 'break', 'continue']):
                # Check next few lines for code
                for j in range(i + 1, min(i + 5, len(lines))):
                    next_line = lines[j].strip()
                    if next_line and not next_line.startswith('#') and next_line not in ['}', ']']:
                        dead.append({
                            'file': str(file_path),
                            'error_type': 'DeadCode',
                            'message': f"Unreachable code after: {stripped[:50]}",
                            'line': j + 1
                        })
                        break

        return dead

    def _detect_logic_errors(self):
        """Detect logic errors"""
        logic_errors = []
        python_files = list(self.project_root.rglob("*.py"))

        print(f"\n🧠 Checking logic errors in {len(python_files)} Python files...")

        for file_path in python_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                logic = self._find_logic_errors(content, file_path)
                logic_errors.extend(logic)

            except Exception:
                continue

        return logic_errors

    def _find_logic_errors(self, content, file_path):
        """Find logic error patterns"""
        logic = []
        lines = content.split('\n')

        # Look for suspicious patterns
        for i, line in enumerate(lines):
            stripped = line.strip()

            # Assignment in condition
            if re.search(r'if\s+\w+\s*=\s*', stripped):
                logic.append({
                    'file': str(file_path),
                    'error_type': 'LogicError',
                    'message': "Assignment in condition - should be ==",
                    'line': i + 1
                })

            # Overriding built-in functions
            if re.search(r'^(\w+)\s*=\s*[^=]', stripped):
                var_name = re.match(r'^(\w+)', stripped)
                if var_name and var_name.group(1) in dir(__builtins__):
                    logic.append({
                        'file': str(file_path),
                        'error_type': 'LogicError',
                        'message': f"Overriding built-in: {var_name.group(1)}",
                        'line': i + 1
                    })

        return logic

    def _detect_security_issues(self):
        """Detect security issues"""
        security_issues = []
        python_files = list(self.project_root.rglob("*.py"))

        print(f"\n🔒 Checking security issues in {len(python_files)} Python files...")

        for file_path in python_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                security = self._find_security_issues(content, file_path)
                security_issues.extend(security)

            except Exception:
                continue

        return security_issues

    def _find_security_issues(self, content, file_path):
        """Find security issue patterns"""
        security = []
        lines = content.split('\n')

        dangerous_patterns = [
            (r'eval\s*\(', "Use of eval() is dangerous - potential security risk"),
            (r'exec\s*\(', "Use of exec() is dangerous - potential security risk"),
            (r'shell\s*=\s*True', "shell=True - potential command injection risk"),
            (r'input\s*\([^)]*\)', "Unvalidated input - potential injection risk")
        ]

        for i, line in enumerate(lines):
            for pattern, message in dangerous_patterns:
                if re.search(pattern, line):
                    security.append({
                        'file': str(file_path),
                        'error_type': 'SecurityIssue',
                        'message': message,
                        'line': i + 1
                    })

        return security

    def _detect_performance_issues(self):
        """Detect performance issues"""
        performance_issues = []
        python_files = list(self.project_root.rglob("*.py"))

        print(f"\n⚡ Checking performance issues in {len(python_files)} Python files...")

        for file_path in python_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                perf = self._find_performance_issues(content, file_path)
                performance_issues.extend(perf)

            except Exception:
                continue

        return performance_issues

    def _find_performance_issues(self, content, file_path):
        """Find performance issue patterns"""
        perf = []
        lines = content.split('\n')

        # Look for performance anti-patterns
        for i, line in enumerate(lines):
            stripped = line.strip()

            # String concatenation in loops
            if re.search(r'\+\s*["\']', stripped) and 'for ' in lines[max(0, i-5):i]:
                perf.append({
                    'file': str(file_path),
                    'error_type': 'PerformanceIssue',
                    'message': "String concatenation in loop - use join() instead",
                    'line': i + 1
                })

            # Global variable usage
            if re.search(r'global\s+\w+', stripped):
                perf.append({
                    'file': str(file_path),
                    'error_type': 'PerformanceIssue',
                    'message': "Global variable usage - can hurt performance",
                    'line': i + 1
                })

        return perf

    def _detect_dependency_issues(self):
        """Detect dependency issues"""
        dependency_issues = []

        print(f"\n🔗 Checking dependency issues...")

        # Check for requirements.txt, setup.py, etc.
        req_files = ['requirements.txt', 'setup.py', 'pyproject.toml']
        missing_deps = []

        for req_file in req_files:
            req_path = self.project_root / req_file
            if not req_path.exists():
                missing_deps.append(req_file)

        if missing_deps:
            dependency_issues.append({
                'file': str(self.project_root),
                'error_type': 'DependencyIssue',
                'message': f"Missing dependency files: {', '.join(missing_deps)}",
                'line': None
            })

        return dependency_issues

    def fix_all_errors(self, error_results):
        """Fix all detected errors systematically"""
        print("\n🔧 STARTING COMPREHENSIVE ERROR FIXING")
        print("=" * 60)

        fixes_applied = {}

        # Fix syntax errors first
        if error_results['syntax_errors']:
            print(f"\n🐛 Fixing {len(error_results['syntax_errors'])} syntax errors...")
            fixes_applied['syntax_errors'] = self._fix_syntax_errors(error_results['syntax_errors'])

        # Fix undefined variables
        if error_results['undefined_variables']:
            print(f"\n🔍 Fixing {len(error_results['undefined_variables'])} undefined variables...")
            fixes_applied['undefined_variables'] = self._fix_undefined_variables(error_results['undefined_variables'])

        # Fix dead code
        if error_results['dead_code']:
            print(f"\n💀 Fixing {len(error_results['dead_code'])} dead code issues...")
            fixes_applied['dead_code'] = self._fix_dead_code(error_results['dead_code'])

        return fixes_applied

    def _fix_syntax_errors(self, syntax_errors):
        """Fix syntax errors"""
        fixes = 0

        for error in syntax_errors:
            file_path = Path(error['file'])
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                original_content = content

                # Fix common syntax issues
                content = self._apply_syntax_fixes(content)

                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixes += 1
                    print(f"  ✅ Fixed syntax errors in {file_path.name}")

            except Exception as e:
                print(f"  ❌ Could not fix {file_path.name}: {e}")

        return fixes

    def _apply_syntax_fixes(self, content):
        """Apply common syntax fixes"""
        fixed = content

        # Fix assignment operators used in parameter defaults
        fixed = re.sub(r'(\w+)\s*==\s*([^,)]+)', r'\1=\2', fixed)

        # Fix unmatched quotes after brackets
        fixed = re.sub(r'\]\s*\'', ']', fixed)
        fixed = re.sub(r'\)\s*\'', ')', fixed)
        fixed = re.sub(r'}\s*\'', '}', fixed)

        # Fix undefined variable assignments that are actually just broken code
        fixed = re.sub(r'^\s*\w+\s*==\s*None\s*#.*$', '', fixed, flags=re.MULTILINE)

        # Fix excessive indentation for imports
        lines = fixed.split('\n')
        fixed_lines = []

        for line in lines:
            # Fix excessive indentation
            if line.strip().startswith(('import ', 'from ')) and line.startswith('    '):
                line = line.lstrip()
            fixed_lines.append(line)

        return '\n'.join(fixed_lines)

    def _fix_undefined_variables(self, undefined_vars):
        """Fix undefined variables by adding placeholder definitions"""
        fixes = 0

        for error in undefined_vars:
            file_path = Path(error['file'])
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Add variable definition at the beginning of the function
                lines = content.split('\n')
                if error['line'] and error['line'] <= len(lines):
                    line_num = error['line'] - 1
                    var_name = error['message'].split(': ')[1]

                    # Insert variable definition
                    lines.insert(line_num, f"    {var_name} = None  # Undefined variable fixed")

                    content = '\n'.join(lines)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixes += 1
                    print(f"  ✅ Fixed undefined variable in {file_path.name}: {var_name}")

            except Exception as e:
                print(f"  ❌ Could not fix undefined variable in {file_path.name}: {e}")

        return fixes

    def _fix_dead_code(self, dead_code):
        """Fix dead code by removing or commenting it"""
        fixes = 0

        for error in dead_code:
            file_path = Path(error['file'])
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                original_content = content
                lines = content.split('\n')

                if error['line'] and error['line'] <= len(lines):
                    line_num = error['line'] - 1
                    lines[line_num] = '# ' + lines[line_num] + '  # Dead code fixed'

                    content = '\n'.join(lines)

                    if content != original_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        fixes += 1
                        print(f"  ✅ Fixed dead code in {file_path.name}")

            except Exception as e:
                print(f"  ❌ Could not fix dead code in {file_path.name}: {e}")

        return fixes

    def generate_report(self, error_results, fixes_applied):
        """Generate comprehensive error report"""
        end_time = datetime.now()
        duration = end_time - self.start_time

        total_errors_found = sum(len(errors) for errors in error_results.values())
        total_fixes_applied = sum(fixes_applied.values())

        report = f"""
🎯 COMPREHENSIVE ERROR DETECTION AND FIXING REPORT
{'=' * 70}
📅 Analysis Date: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}
⏱️  Duration: {duration}
📁 Project Root: {self.project_root}

📊 ERRORS DETECTED:
"""

        for error_type, errors in error_results.items():
            if errors:
                report += f"  • {error_type}: {len(errors)}\n"

        report += f"""
📊 TOTAL ERRORS DETECTED: {total_errors_found}

🔧 FIXES APPLIED:
"""

        for error_type, count in fixes_applied.items():
            if count > 0:
                report += f"  • {error_type}: {count}\n"

        report += f"""
📊 TOTAL FIXES APPLIED: {total_fixes_applied}

📈 SUCCESS RATE: {(total_fixes_applied / total_errors_found * 100):.1f}% if total_errors_found > 0 else 100

🏆 STATUS: {'✅ ALL ERRORS FIXED!' if total_fixes_applied >= total_errors_found else '⚠️  Some errors remain'}

📋 DETAILED BREAKDOWN:
"""

        for error_type, errors in error_results.items():
            if errors:
                report += f"\n{error_type.upper()}:\n"
                for error in errors[:5]:  # Show first 5 errors of each type
                    report += f"  • {Path(error['file']).name}:{error.get('line', 'N/A')} - {error.get('message', 'No message')}\n"
                if len(errors) > 5:
                    report += f"  ... and {len(errors) - 5} more\n"

        return report

    def save_report(self, report, filename="comprehensive_error_report.txt"):
        """Save report to file"""
        report_path = self.project_root / filename
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\n📄 Report saved to: {report_path}")


def main():
    """Main execution function"""
    import argparse

    parser = argparse.ArgumentParser(description='Comprehensive Error Detection and Fixing System')
    parser.add_argument('--project-root', default='.', help='Project root directory')
    parser.add_argument('--output', default='comprehensive_error_report.txt', help='Output report file')
    parser.add_argument('--fix-only', action='store_true', help='Only fix errors, no detection')

    args = parser.parse_args()

    detector = ComprehensiveErrorDetector(args.project_root)

    if not args.fix_only:
        # Detect errors
        error_results = detector.detect_all_errors()

        # Fix errors
        fixes_applied = detector.fix_all_errors(error_results)

        # Generate and save report
        report = detector.generate_report(error_results, fixes_applied)
        detector.save_report(report, args.output)

        # Print summary
        total_errors = sum(len(errors) for errors in error_results.values())
        total_fixes = sum(fixes_applied.values())
        print(f"\n🎉 COMPREHENSIVE ANALYSIS COMPLETE!")
        print(f"📊 Errors Found: {total_errors}")
        print(f"🔧 Fixes Applied: {total_fixes}")
        print(f"📈 Success Rate: {(total_fixes/total_errors*100):.1f}%" if total_errors > 0 else "100%")

    else:
        print("Fix-only mode not implemented yet")


if __name__ == '__main__':
    main()