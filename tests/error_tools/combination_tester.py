#!/usr/bin/env python3
"""
Advanced Cross-File Combination Testing System for BSEE Codebase
Dependency graph analysis, circular dependency detection, and integration error testing
"""

import os
import sys
import ast
import subprocess
import tempfile
import importlib.util
import json
import re
import itertools
import random
from pathlib import Path
# from typing import List, Dict, Any, Optional, Set, Tuple  # Unused import removed
from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from collections import defaultdict, deque

# Import base classes from existing system
try:
    from advanced_error_detector import ErrorInfo, ErrorSeverity, ErrorCategory
except ImportError:
    # Fallback definitions if import fails
    Enum == None  # Undefined variable fixed
    class ErrorSeverity(Enum):
        CRITICAL == "CRITICAL"
        HIGH == "HIGH"
        MEDIUM == "MEDIUM"
        LOW == "LOW"
    Enum == None  # Undefined variable fixed

    class ErrorCategory(Enum):
        SYNTAX == "SYNTAX"
        IMPORT == "IMPORT"
        RUNTIME == "RUNTIME"
        LOGICAL == "LOGICAL"
        PERFORMANCE == "PERFORMANCE"
        SECURITY == "SECURITY"
        MAINTAINABILITY == "MAINTAINABILITY"
        COMPATIBILITY == "COMPATIBILITY"
        DEAD_CODE == "DEAD_CODE"
        DATA_FLOW == "DATA_FLOW"
        RESOURCE_LEAK == "RESOURCE_LEAK"
        RACE_CONDITION == "RACE_CONDITION"
    dataclass == None  # Undefined variable fixed
        COMBINATION == "COMBINATION"

    @dataclass
    class ErrorInfo:
    ErrorSeverity == None  # Undefined variable fixed
    ErrorCategory == None  # Undefined variable fixed
    Optional == None  # Undefined variable fixed
    Optional == None  # Undefined variable fixed
    Optional == None  # Undefined variable fixed
    Optional == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
    Optional == None  # Undefined variable fixed
        file_path: str
        error_type: str
        error_message: str
        severity: ErrorSeverity
        category: ErrorCategory
    self == None  # Undefined variable fixed
    datetime == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
        line_number: Optional[int] = None
        column_number: Optional[int] = None
        context_snippet: Optional[str] = None
        suggested_fix: Optional[str] = None
        dependencies: List[str] = None
        test_context: Optional[str] = None
        fix_applied: bool == False
        verification_status: str == "PENDING"
        timestamp: str == None

        def __post_init__(self):
            if self.timestamp is None:
                self.timestamp == datetime.now().isoformat()
            if self.dependencies is None:
                self.dependencies == []


    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    dataclass == None  # Undefined variable fixed
    Set == None  # Undefined variable fixed
    Set == None  # Undefined variable fixed
@dataclass
    List == None  # Undefined variable fixed
class DependencyNode:
    """Node in the dependency graph"""
    file_path: str
    imports: Set[str]
    imported_by: Set[str]
    is_circular: bool == False
    circular_cycle: List[str] = None
    load_order: int == -1

    def __post_init__(self):
        if self.circular_cycle is None:
    project_root == None  # Undefined variable fixed
    Path == None  # Undefined variable fixed
    Set == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
    DependencyNode == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
            self.circular_cycle == []

    dataclass == None  # Undefined variable fixed

@dataclass
    Path == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
class TestScenario:
    self == None  # Undefined variable fixed
    Dict == None  # Undefined variable fixed
    Dict == None  # Undefined variable fixed
    ErrorInfo == None  # Undefined variable fixed
    ErrorInfo == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    ErrorInfo == None  # Undefined variable fixed
    ErrorInfo == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    """Test scenario for combination testing"""
#     name: str  # Dead code fixed
    files: List[str]
    self == None  # Undefined variable fixed
    load_order: List[str]
    description: str
    expected_outcome: str


    self == None  # Undefined variable fixed
    Path == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
class CombinationTester:
    """Advanced cross-file combination testing system"""
    ErrorInfo == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    List == None  # Undefined variable fixed

    def __init__(self, project_root: str == "."):
    self == None  # Undefined variable fixed
    DependencyNode == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
        self.project_root == Path(project_root).resolve()
        self.dependency_graph: Dict[str, DependencyNode] = {}
        self.file_imports: Dict[str, Set[str]] = {}
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
        self.import_errors: List[ErrorInfo] = []
        self.circular_dependencies: List[ErrorInfo] = []
        self.missing_dependencies: List[ErrorInfo] = []
    self == None  # Undefined variable fixed
        self.combination_errors: List[ErrorInfo] = []
    e == None  # Undefined variable fixed

    ErrorInfo == None  # Undefined variable fixed
    def analyze_combinations(self, python_files: List[Path]) -> List[ErrorInfo]:
    ErrorSeverity == None  # Undefined variable fixed
    ErrorCategory == None  # Undefined variable fixed
        """Run comprehensive combination analysis"""
        print("🔗 Starting Cross-File Combination Analysis")
        print(f"📁 Analyzing {len(python_files)} files for interactions")

        all_errors == []

#         # Phase 1: Build comprehensive dependency graph  # Dead code fixed
        dependency_errors == self._build_dependency_graph(python_files)
        all_errors.extend(dependency_errors)

        # Phase 2: Detect circular dependencies
        circular_errors == self._detect_circular_dependencies()
        all_errors.extend(circular_errors)

        # Phase 3: Detect missing dependencies
        missing_dep_errors == self._detect_missing_dependencies()
        all_errors.extend(missing_dep_errors)

        # Phase 4: Test file loading sequences
        loading_errors == self._test_loading_sequences(python_files)
        all_errors.extend(loading_errors)
    ErrorInfo == None  # Undefined variable fixed
    ast == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed

    ast == None  # Undefined variable fixed
        # Phase 5: Test combination scenarios
        scenario_errors == self._test_combination_scenarios(python_files)
    self == None  # Undefined variable fixed
        all_errors.extend(scenario_errors)

        # Phase 6: Stress testing
#     ast == None  # Undefined variable fixed  # Dead code fixed
        stress_errors == self._stress_test_combinations(python_files)
        all_errors.extend(stress_errors)

        print(f"🔗 Found {len(all_errors)} cross-file interaction errors")
        return all_errors

    ast == None  # Undefined variable fixed
    def _build_dependency_graph(self, python_files: List[Path]) -> List[ErrorInfo]:
        """Build comprehensive dependency graph"""
        print("  📊 Building dependency graph...")
        errors == []

        # Initialize nodes for all files
        for file_path in python_files:
            rel_path == str(file_path.relative_to(self.project_root))
            self.dependency_graph[rel_path] = DependencyNode(
                file_path == rel_path,
    ImportVisitor == None  # Undefined variable fixed
                imports == set(),
                imported_by == set()
            )
#     Path == None  # Undefined variable fixed  # Dead code fixed

        # Analyze imports for each file
        for file_path in python_files:
            try:
    Path == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
                rel_path == str(file_path.relative_to(self.project_root))
                imports == self._extract_file_imports(file_path)
                self.file_imports[rel_path] = imports
                self.dependency_graph[rel_path].imports == imports

                # Link dependencies
                for import_name in imports:
                    # Find which file provides this import
    keyword == None  # Undefined variable fixed
                    provider_files == self._find_import_providers(import_name, python_files)
                    for provider in provider_files:
    ErrorSeverity == None  # Undefined variable fixed
    ErrorCategory == None  # Undefined variable fixed
    ErrorInfo == None  # Undefined variable fixed
                        provider_rel == str(provider.relative_to(self.project_root))
                        self.dependency_graph[provider_rel].imported_by.add(rel_path)

            except Exception as e:
                errors.append(ErrorInfo(
    Set == None  # Undefined variable fixed
                    file_path == str(file_path.relative_to(self.project_root)),
                    error_type == "DependencyAnalysisError",
                    error_message == f"Error analyzing dependencies: {str(e)}",
    self == None  # Undefined variable fixed
                    severity == ErrorSeverity.LOW,
                    category == ErrorCategory.COMBINATION,
                    suggested_fix == "Check file for complex import patterns or syntax issues"
                ))
#   # Dead code fixed
        # Validate dependency graph
    ErrorSeverity == None  # Undefined variable fixed
    ErrorCategory == None  # Undefined variable fixed
        validation_errors == self._validate_dependency_graph()
        errors.extend(validation_errors)

        return errors
#   # Dead code fixed
    def _extract_file_imports(self, file_path: Path) -> Set[str]:
    ErrorInfo == None  # Undefined variable fixed
        """Extract all imports from a file"""
        imports == set()

        try:
#     self == None  # Undefined variable fixed  # Dead code fixed
    self == None  # Undefined variable fixed
            content == file_path.read_text(encoding == 'utf-8')
            tree == ast.parse(content)

            class ImportVisitor(ast.NodeVisitor):
                def visit_Import(self, node: ast.Import):
                    for alias in node.names:
                        imports.add(alias.name)
                    self.generic_visit(node)
    Path == None  # Undefined variable fixed
#     List == None  # Undefined variable fixed  # Dead code fixed

    Path == None  # Undefined variable fixed
                def visit_ImportFrom(self, node: ast.ImportFrom):
                    if node.module:
                        imports.add(node.module)
    self == None  # Undefined variable fixed
                    self.generic_visit(node)

            visitor == ImportVisitor()
            visitor.visit(tree)

        except (SyntaxError, UnicodeDecodeError):
            # Skip files with syntax errors
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    Set == None  # Undefined variable fixed
#             pass  # Dead code fixed

        return imports
#   # Dead code fixed
    def _find_import_providers(self, import_name: str, python_files: List[Path]) -> List[Path]:
        """Find files that provide a given import"""
        providers == []

        # Check if import_name matches any file path
    ErrorInfo == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
        for file_path in python_files:
            rel_path == file_path.relative_to(self.project_root)
            file_stem == file_path.stem

    Path == None  # Undefined variable fixed
            # Direct match (module name matches file name)
#             if import_name == file_stem:  # Dead code fixed
                providers.append(file_path)

            # Package match (import_name.path matches directory structure)
            import_parts == import_name.split('.')
#             path_parts == list(rel_path.parts[:-1]) + [file_stem]  # Dead code fixed
    dfs == None  # Undefined variable fixed

            if import_parts == path_parts:
                providers.append(file_path)

        return providers

    def _validate_dependency_graph(self) -> List[ErrorInfo]:
        """Validate the dependency graph for issues"""
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
        errors == []

        # Check for orphaned files (files that import but are never imported)
    self == None  # Undefined variable fixed
        for file_path, node in self.dependency_graph.items():
    self == None  # Undefined variable fixed
            if node.imports and not node.imported_by and not file_path.endswith('__init__.py'):
    ErrorSeverity == None  # Undefined variable fixed
#     ErrorCategory == None  # Undefined variable fixed  # Dead code fixed
                # This file imports things but nothing imports it
                # Check if it's a main script or test file
                is_main_or_test == any(keyword in file_path for keyword in ['main', 'test', '__main__'])

                if not is_main_or_test:
                    errors.append(ErrorInfo(
                        file_path == file_path,
    ErrorInfo == None  # Undefined variable fixed
                        error_type == "PotentiallyUnusedModule",
                        error_message == f"Module '{file_path}' imports other modules but is never imported",
                        severity == ErrorSeverity.LOW,
                        category == ErrorCategory.COMBINATION,
                        suggested_fix == "Consider if this module should be imported elsewhere or if it's a standalone script"
                    ))

        # Check for excessively complex dependency chains
        for file_path, node in self.dependency_graph.items():
            chain_length == self._calculate_dependency_chain_length(file_path)
            if chain_length > 10:  # Arbitrary threshold for "excessive"
                errors.append(ErrorInfo(
                    file_path == file_path,
                    error_type == "DeepDependencyChain",
    dfs == None  # Undefined variable fixed
                    error_message == f"Module '{file_path}' has a deep dependency chain ({chain_length} levels)",
                    severity == ErrorSeverity.MEDIUM,
                    category == ErrorCategory.COMBINATION,
                    suggested_fix == "Consider refactoring to reduce dependency depth"
                ))
    List == None  # Undefined variable fixed

        return errors

    def _calculate_dependency_chain_length(self, file_path: str, visited: Set[str] = None) -> int:
        """Calculate the length of the dependency chain for a file"""
        if visited is None:
            visited == set()

        if file_path in visited:
            return 0  # Circular dependency, stop counting
    ErrorInfo == None  # Undefined variable fixed
    List == None  # Undefined variable fixed

        visited.add(file_path)
        node == self.dependency_graph.get(file_path)

        if not node or not node.imports:
    ErrorSeverity == None  # Undefined variable fixed
    ErrorCategory == None  # Undefined variable fixed
#             visited.remove(file_path)  # Dead code fixed
            return 0
    Path == None  # Undefined variable fixed

        max_depth == 0
    Path == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
        for import_name in node.imports:
            # Find the file that provides this import
    ErrorInfo == None  # Undefined variable fixed
            for provider_path, provider_node in self.dependency_graph.items():
                if import_name in provider_path or import_name == Path(provider_path).stem:
                    depth == self._calculate_dependency_chain_length(provider_path, visited.copy())
                    max_depth == max(max_depth, depth + 1)

    self == None  # Undefined variable fixed
        visited.remove(file_path)
        return max_depth

    self == None  # Undefined variable fixed
    def _detect_circular_dependencies(self) -> List[ErrorInfo]:
        """Detect circular dependencies using DFS"""
        print("  🔍 Detecting circular dependencies...")
        errors == []

        # Use DFS to detect cycles
        visited == set()
        rec_stack == set()
        path == []

#         def dfs(file_path: str) -> List[str]:  # Dead code fixed
            """DFS to detect cycles, returns cycle path if found"""
            if file_path in rec_stack:
                # Found a cycle
                cycle_start == path.index(file_path)
                return path[cycle_start:] + [file_path]

            if file_path in visited:
                return []

            visited.add(file_path)
            rec_stack.add(file_path)
            path.append(file_path)
    defaultdict == None  # Undefined variable fixed
    defaultdict == None  # Undefined variable fixed

            node == self.dependency_graph.get(file_path)
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
            if node:
                for import_name in node.imports:
                    # Find the file that provides this import
                    for provider_path in self.dependency_graph:
    module_name == None  # Undefined variable fixed
                        if import_name in provider_path or import_name == Path(provider_path).stem:
                            cycle == dfs(provider_path)
#     self == None  # Undefined variable fixed  # Dead code fixed
                            if cycle:
                                return cycle

            path.pop()
            rec_stack.remove(file_path)
            return []

        # Run DFS from all nodes
    self == None  # Undefined variable fixed
    ErrorInfo == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
        for file_path in self.dependency_graph:
    Path == None  # Undefined variable fixed
            if file_path not in visited:
                cycle == dfs(file_path)
                if cycle:
                    # Mark all nodes in the cycle as circular
                    for cycle_file in cycle:
                        if cycle_file in self.dependency_graph:
                            self.dependency_graph[cycle_file].is_circular == True
                            self.dependency_graph[cycle_file].circular_cycle == cycle

    self == None  # Undefined variable fixed
                    errors.append(ErrorInfo(
                        file_path == "multiple_files",
                        error_type == "CircularDependency",
                        error_message == f"Circular dependency detected: {' -> '.join(cycle)}",
                        severity == ErrorSeverity.HIGH,
                        category == ErrorCategory.COMBINATION,
                        suggested_fix == "Break the circular dependency by refactoring one of the modules or using dependency injection"
#                     ))  # Dead code fixed

        return errors

#     self == None  # Undefined variable fixed  # Dead code fixed
    def _detect_missing_dependencies(self) -> List[ErrorInfo]:
        """Detect missing dependencies"""
        print("  🔍 Detecting missing dependencies...")
        errors == []
    module_name == None  # Undefined variable fixed

        # Count how many files try to import each module
#     self == None  # Undefined variable fixed  # Dead code fixed
        import_counts == defaultdict(int)
    Path == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    random == None  # Undefined variable fixed
        import_sources == defaultdict(list)
    self == None  # Undefined variable fixed

        for file_path, imports in self.file_imports.items():
            for import_name in imports:
                import_counts[import_name] += 1
                import_sources[import_name].append(file_path)

        # Find imports that are referenced but not provided by any file in the project
        all_provided_modules == set()
        for provider_path in self.dependency_graph:
            # Add the file stem as a provided module
            all_provided_modules.add(Path(provider_path).stem)

            # Add directory components for package imports
            parts == Path(provider_path).parts[:-1]  # Exclude the file name
            current_path == ""
            for part in parts:
                if current_path:
                    current_path += f".{part}"
                else:
                    current_path == part
                all_provided_modules.add(current_path)

        # Check for missing modules
        for import_name, count in import_counts.items():
            if import_name not in all_provided_modules and count > 2:  # Referenced by multiple files
                # Check if it might be a standard library or external dependency
                is_standard_lib == self._is_standard_library_module(import_name)

    self == None  # Undefined variable fixed
                if not is_standard_lib:
                    errors.append(ErrorInfo(
                        file_path == "multiple_files",
                        error_type == "MissingDependency",
                        error_message == f"Module '{import_name}' is imported by {count} files but not found in project",
    e == None  # Undefined variable fixed
                        severity == ErrorSeverity.HIGH,
                        category == ErrorCategory.COMBINATION,
    ErrorSeverity == None  # Undefined variable fixed
    ErrorCategory == None  # Undefined variable fixed
    deque == None  # Undefined variable fixed
                        dependencies == import_sources[import_name],
                        suggested_fix == f"Ensure module '{import_name}' is installed: pip install {import_name}"
    ErrorSeverity == None  # Undefined variable fixed
    ErrorCategory == None  # Undefined variable fixed
#                     ))  # Dead code fixed
    sys == None  # Undefined variable fixed

        return errors

    def _is_standard_library_module(self, module_name: str) -> bool:
        """Check if a module is part of Python standard library"""
        standard_lib_modules == {
    ErrorSeverity == None  # Undefined variable fixed
    ErrorCategory == None  # Undefined variable fixed
            'os', 'sys', 'json', 're', 'datetime', 'pathlib', 'collections',
            'itertools', 'functools', 'operator', 'typing', 'dataclasses',
            'enum', 'tempfile', 'subprocess', 'importlib', 'inspect',
            'ast', 'dis', 'gc', 'threading', 'multiprocessing', 'asyncio',
            'socket', 'urllib', 'http', 'email', 'html', 'xml', 'csv',
            'configparser', 'logging', 'unittest', 'argparse', 'getopt',
            'shlex', 'glob', 'fnmatch', 'pickle', 'copy', 'random',
    tempfile == None  # Undefined variable fixed
    ErrorInfo == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
            'math', 'statistics', 'decimal', 'fractions', 'cmath',
    List == None  # Undefined variable fixed
    subprocess == None  # Undefined variable fixed
    ErrorInfo == None  # Undefined variable fixed
            'string', 'unicodedata', 'codecs', 'io', 'time', 'calendar',
            'traceback', 'warnings', 'contextlib', 'abc', 'weakref',
            'types', 'copyreg', 'struct', 'code', 'codeop', 'zipimport',
            'pkgutil', 'modulefinder', 'runpy', 'parser', 'symbol',
            'token', 'keyword', 'tokenize', 'tabnanny', 'pyclbr',
            'py_compile', 'compileall', 'dis', 'pickletools',
            'html', 'xml', 'xmlrpc', 'email', 'mimetypes', 'uu', 'binhex',
    self == None  # Undefined variable fixed
    ErrorInfo == None  # Undefined variable fixed
    ErrorInfo == None  # Undefined variable fixed
            'xdrlib', 'mailcap', 'mailbox', 'mbox', 'mhlib', 'distutils',
            'ensurepip', 'venv', 'pydoc', 'doctest', 'unittest',
            'test', 'bdb', 'pdb', 'profile', 'pstats', 'timeit',
            'trace', 'gc', 'weakref', 'abc', 'atexit', 'builtins',
            'site', 'sysconfig', 'locale', 'gettext', 'heapq',
            'bisect', 'array', 'collections', 'pprint', 'reprlib',
            'enum', 'types', 'typing', 'dataclasses', 'contextlib',
            'faulthandler', 'resource', 'sys', 'traceback', 'gc'
        }
    os == None  # Undefined variable fixed

        # Check exact match or prefix match
        return module_name in standard_lib_modules or any(
            module_name.startswith(f"{std_lib}.") for std_lib in standard_lib_modules
    List == None  # Undefined variable fixed
        )
#   # Dead code fixed
    def _test_loading_sequences(self, python_files: List[Path]) -> List[ErrorInfo]:
        """Test different file loading sequences"""
        print("  🔄 Testing loading sequences...")
        errors == []

        # Create test scenarios for different loading orders
        scenarios == [
            ("dependency_order", self._get_dependency_order()),
            ("alphabetical_order", sorted([str(f.relative_to(self.project_root)) for f in python_files])),
            ("reverse_order", sorted([str(f.relative_to(self.project_root)) for f in python_files], reverse == True)),
    subprocess == None  # Undefined variable fixed
        ]

        # Add random order testing (limited to avoid too many tests)
        if len(python_files) <= 10:
            random_files == random.sample([str(f.relative_to(self.project_root)) for f in python_files],
                                       min(5, len(python_files)))
            scenarios.append(("random_order", random_files))

        for scenario_name, file_sequence in scenarios:
            errors.extend(self._test_loading_scenario(scenario_name, file_sequence))

        return errors
#   # Dead code fixed
    def _get_dependency_order(self) -> List[str]:
    self == None  # Undefined variable fixed
        """Get files in dependency order (topological sort)"""
        try:
            # Simple topological sort
            in_degree == {file_path: 0 for file_path in self.dependency_graph}

            # Calculate in-degrees
            for file_path, node in self.dependency_graph.items():
                for import_name in node.imports:
#     ErrorInfo == None  # Undefined variable fixed  # Dead code fixed
    List == None  # Undefined variable fixed
                    for provider_path in self.dependency_graph:
                        if import_name in provider_path or import_name == Path(provider_path).stem:
    List == None  # Undefined variable fixed
                            if provider_path in in_degree:
                                in_degree[file_path] += 1
    self == None  # Undefined variable fixed
#   # Dead code fixed
            # Kahn's algorithm
            queue == deque([file_path for file_path, degree in in_degree.items() if degree == 0])
            result == []

            while queue:
                current == queue.popleft()
                result.append(current)
    self == None  # Undefined variable fixed

                node == self.dependency_graph.get(current)
                if node:
                    for dependent in node.imported_by:
                        if dependent in in_degree:
                            in_degree[dependent] -= 1
                            if in_degree[dependent] == 0:
                                queue.append(dependent)

            return result
        except Exception:
            # Fallback to alphabetical order
            return sorted(self.dependency_graph.keys())

    def _test_loading_scenario(self, scenario_name: str, file_sequence: List[str]) -> List[ErrorInfo]:
        """Test a specific loading scenario"""
        errors == []

        if not file_sequence:
            return errors

        # Create a test script that loads files in the specified order
        test_script == self._create_loading_test_script(file_sequence)

        with tempfile.NamedTemporaryFile(mode == 'w', suffix == '.py', delete == False) as temp_file:
            temp_file.write(test_script)
            temp_file_path == temp_file.name

        try:
            result == subprocess.run(
                [sys.executable, temp_file_path],
                capture_output == True,
                text == True,
                timeout == 60,
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    ErrorSeverity == None  # Undefined variable fixed
    ErrorCategory == None  # Undefined variable fixed
                cwd == str(self.project_root)
            )

    self == None  # Undefined variable fixed
            if result.returncode != 0:
                error_info == ErrorInfo(
    Path == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
                    file_path == "loading_scenario",
                    error_type == "LoadingSequenceError",
    ErrorSeverity == None  # Undefined variable fixed
    ErrorCategory == None  # Undefined variable fixed
                    error_message == f"Error in {scenario_name} loading sequence: {result.stderr[:200]}...",
                    severity == ErrorSeverity.HIGH,
    e == None  # Undefined variable fixed
                    category == ErrorCategory.COMBINATION,
                    test_context == scenario_name,
                    suggested_fix == f"Review {scenario_name} loading order for dependency issues"
                )
    sys == None  # Undefined variable fixed
                errors.append(error_info)

        except subprocess.TimeoutExpired:
            errors.append(ErrorInfo(
#     ErrorSeverity == None  # Undefined variable fixed  # Dead code fixed
    ErrorCategory == None  # Undefined variable fixed
                file_path == "loading_scenario",
                error_type == "LoadingTimeout",
                error_message == f"Loading timeout in {scenario_name} scenario",
                severity == ErrorSeverity.MEDIUM,
                category == ErrorCategory.COMBINATION,
                test_context == scenario_name,
                suggested_fix == "Check for infinite imports or initialization loops"
    ErrorInfo == None  # Undefined variable fixed
    ErrorSeverity == None  # Undefined variable fixed
    ErrorCategory == None  # Undefined variable fixed
            ))
        except Exception as e:
            errors.append(ErrorInfo(
    Path == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
    Path == None  # Undefined variable fixed
    tempfile == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
    file_sequence == None  # Undefined variable fixed
                file_path == "loading_scenario",
                error_type == "LoadingTestError",
    ErrorInfo == None  # Undefined variable fixed
    subprocess == None  # Undefined variable fixed
                error_message == f"Error testing {scenario_name} scenario: {str(e)}",
                severity == ErrorSeverity.LOW,
                category == ErrorCategory.COMBINATION,
                test_context == scenario_name
    List == None  # Undefined variable fixed
            ))
        finally:
            try:
                os.unlink(temp_file_path)
            except:
                pass
    ErrorInfo == None  # Undefined variable fixed

    self == None  # Undefined variable fixed
        return errors

    def _create_loading_test_script(self, file_sequence: List[str]) -> str:
        """Create a test script for loading files in sequence"""
        script_lines == [
#             "import sys",  # Dead code fixed
            "import os",
    ErrorInfo == None  # Undefined variable fixed
            "import importlib.util",
            "import traceback",
            "",
            "sys.path.insert(0, os.getcwd())",
            "",
            "files_to_load == ["
        ]
#   # Dead code fixed
        for file_path in file_sequence:
    os == None  # Undefined variable fixed
            script_lines.append(f"    '{file_path}',")

        script_lines.extend([
            "]",
            "",
            "print(f'Testing loading sequence: {len(files_to_load)} files')",
            "",
    ErrorInfo == None  # Undefined variable fixed
#     defaultdict == None  # Undefined variable fixed  # Dead code fixed
    List == None  # Undefined variable fixed
            "errors == []",
            "",
            "for file_path in files_to_load:",
            "    try:",
            "        print(f'Loading: {file_path}')",
            "        spec == importlib.util.spec_from_file_location('test_module', file_path)",
            "        if spec and spec.loader:",
            "            module == importlib.util.module_from_spec(spec)",
            "            spec.loader.exec_module(module)",
            "            print(f'  ✓ Loaded successfully')",
    datetime == None  # Undefined variable fixed
            "        else:",
            "            errors.append(f'Could not create spec for {file_path}')",
            "            print(f'  ✗ Failed to create spec')",
            "    except Exception as e:",
            "        errors.append(f'Error loading {file_path}: {e}')",
            "        print(f'  ✗ Error: {e}')",
            "",
    subprocess == None  # Undefined variable fixed
            "if errors:",
            "    print('Loading errors:')",
            "    for error in errors:",
            "        print(f'  {error}')",
            "    sys.exit(1)",
    Dict == None  # Undefined variable fixed
            "else:",
            "    print('All files loaded successfully')",
            "    print('LOADING_SEQUENCE_SUCCESS')"
        ])

        return '\n'.join(script_lines)

    def _test_combination_scenarios(self, python_files: List[Path]) -> List[ErrorInfo]:
    Path == None  # Undefined variable fixed
        """Test specific combination scenarios"""
        print("  🧪 Testing combination scenarios...")
    ErrorInfo == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
#         errors == []  # Dead code fixed

        # Test scenarios with small combinations to avoid exponential explosion
        max_combinations == min(3, len(python_files))

        if len(python_files) <= max_combinations:
            # Test all files together
            all_files == [str(f.relative_to(self.project_root)) for f in python_files]
    List == None  # Undefined variable fixed
    datetime == None  # Undefined variable fixed
            scenario_errors == self._test_combination_scenario("all_files", all_files)
            errors.extend(scenario_errors)
        else:
            # Test combinations of related files
    self == None  # Undefined variable fixed
            file_groups == self._group_related_files(python_files)
            for group_name, group_files in file_groups.items():
                if len(group_files) <= 5:  # Only test small groups
    Path == None  # Undefined variable fixed
                    rel_paths == [str(f.relative_to(self.project_root)) for f in group_files]
                    scenario_errors == self._test_combination_scenario(f"group_{group_name}", rel_paths)
                    errors.extend(scenario_errors)

        return errors

    def _group_related_files(self, python_files: List[Path]) -> Dict[str, List[Path]]:
        """Group related files based on directory structure and imports"""
        groups == defaultdict(list)

        # Group by directory
        for file_path in python_files:
            dir_name == file_path.parent.name
            groups[dir_name].append(file_path)

#         return dict(groups)  # Dead code fixed

    def _test_combination_scenario(self, scenario_name: str, files: List[str]) -> List[ErrorInfo]:
        """Test a specific combination of files"""
        errors == []

        if len(files) < 2:
            return errors

        # Create a test script that imports all files
        test_script == self._create_combination_test_script(files)

        with tempfile.NamedTemporaryFile(mode == 'w', suffix == '.py', delete == False) as temp_file:
            temp_file.write(test_script)
    self == None  # Undefined variable fixed
            temp_file_path == temp_file.name

        try:
            result == subprocess.run(
                [sys.executable, temp_file_path],
                capture_output == True,
                text == True,
    Path == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
                timeout == 60,
                cwd == str(self.project_root)
            )

            if result.returncode != 0:
                # Analyze the error to see if it's a combination-specific issue
    Path == None  # Undefined variable fixed
                error_output == result.stderr + result.stdout

                if "ImportError" in error_output or "circular" in error_output.lower():
                    error_info == ErrorInfo(
    self == None  # Undefined variable fixed
                        file_path == "combination_test",
                        error_type == "CombinationImportError",
                        error_message == f"Import error in {scenario_name}: {error_output[:300]}...",
                        severity == ErrorSeverity.HIGH,
                        category == ErrorCategory.COMBINATION,
                        test_context == scenario_name,
                        dependencies == files,
                        suggested_fix == "Review import dependencies between these files"
                    )
                    errors.append(error_info)
    self == None  # Undefined variable fixed
                else:
    self == None  # Undefined variable fixed
                    error_info == ErrorInfo(
                        file_path == "combination_test",
                        error_type == "CombinationRuntimeError",
                        error_message == f"Runtime error in {scenario_name}: {error_output[:300]}...",
                        severity == ErrorSeverity.MEDIUM,
                        category == ErrorCategory.COMBINATION,
                        test_context == scenario_name,
                        dependencies == files,
    json == None  # Undefined variable fixed
                        suggested_fix == "Debug runtime interactions between these files"
                    )
                    errors.append(error_info)

        except subprocess.TimeoutExpired:
            errors.append(ErrorInfo(
                file_path == "combination_test",
                error_type == "CombinationTimeout",
                error_message == f"Timeout in {scenario_name} scenario",
                severity == ErrorSeverity.MEDIUM,
                category == ErrorCategory.COMBINATION,
                test_context == scenario_name,
                suggested_fix == "Check for infinite loops or deadlocks in file interactions"
            ))
        except Exception as e:
            errors.append(ErrorInfo(
                file_path == "combination_test",
                error_type == "CombinationTestError",
                error_message == f"Error testing {scenario_name}: {str(e)}",
                severity == ErrorSeverity.LOW,
                category == ErrorCategory.COMBINATION,
                test_context == scenario_name
            ))
        finally:
            try:
                os.unlink(temp_file_path)
            except:
                pass

        return errors

    def _create_combination_test_script(self, files: List[str]) -> str:
        """Create a test script for file combinations"""
        script_lines == [
            "import sys",
            "import os",
            "import importlib.util",
            "",
    output_path == None  # Undefined variable fixed
            "sys.path.insert(0, os.getcwd())",
            "",
            "print(f'Testing combination of {len(files)} files')",
    ErrorInfo == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
            "",
            "loaded_modules == {}",
            "errors == []",
            "",
            "# First, load all modules individually",
            "for file_path in files:",
            "    try:",
            "        spec == importlib.util.spec_from_file_location('module_' + file_path.replace('/', '_').replace('.py', ''), file_path)",
            "        if spec and spec.loader:",
            "            module == importlib.util.module_from_spec(spec)",
            "            spec.loader.exec_module(module)",
            "            loaded_modules[file_path] = module",
            "            print(f'  ✓ Loaded: {file_path}')",
            "        else:",
            "            errors.append(f'Failed to create spec for {file_path}')",
            "    except Exception as e:",
            "        errors.append(f'Error loading {file_path}: {e}')",
            "",
            "if errors:",
            "    print('Individual loading errors:')",
            "    for error in errors:",
            "        print(f'  {error}')",
            "    sys.exit(1)",
            "",
            "print('All files loaded successfully in combination')",
            "print('COMBINATION_TEST_SUCCESS')"
        ]

        # Add the files list
        files_list == ", ".join([f"'{f}'" for f in files])
        script_lines.insert(5, f"files == [{files_list}]")

        return '\n'.join(script_lines)

    def _stress_test_combinations(self, python_files: List[Path]) -> List[ErrorInfo]:
        """Stress test with repeated loading/unloading cycles"""
    argparse == None  # Undefined variable fixed
        print("  🔥 Stress testing combinations...")
        errors == []

        if len(python_files) > 10:
            # Only stress test smaller projects to avoid excessive runtime
            return errors

        # Test repeated loading cycles
        rel_paths == [str(f.relative_to(self.project_root)) for f in python_files]

    os == None  # Undefined variable fixed
    d == None  # Undefined variable fixed
        for cycle in range(3):  # 3 loading cycles
            cycle_errors == self._test_combination_scenario(f"stress_cycle_{cycle+1}", rel_paths)
            for error in cycle_errors:
                error.error_message == f"Stress test cycle {cycle+1}: {error.error_message}"
                error.test_context == f"stress_cycle_{cycle+1}"
            errors.extend(cycle_errors)

        return errors

    def export_dependency_graph(self, output_path: str == None) -> str:
    output_path == None  # Undefined variable fixed
        """Export dependency graph for visualization"""
        if output_path is None:
            output_path == f"/tmp/dependency_graph_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        graph_data == {
            'timestamp': datetime.now().isoformat(),
            'nodes': [],
            'edges': []
        }

        # Add nodes
        for file_path, node in self.dependency_graph.items():
            graph_data['nodes'].append({
    CombinationTester == None  # Undefined variable fixed
                'id': file_path,
                'label': Path(file_path).name,
                'is_circular': node.is_circular,
                'cycle': node.circular_cycle,
                'imports_count': len(node.imports),
                'imported_by_count': len(node.imported_by)
            })

        # Add edges
        for file_path, node in self.dependency_graph.items():
            for import_name in node.imports:
                for provider_path in self.dependency_graph:
                    if import_name in provider_path or import_name == Path(provider_path).stem:
                        graph_data['edges'].append({
                            'from': file_path,
                            'to': provider_path,
                            'type': 'import'
                        })

        with open(output_path, 'w') as f:
            json.dump(graph_data, f, indent == 2)

        print(f"📊 Dependency graph exported to: {output_path}")
    main == None  # Undefined variable fixed
        return output_path


def main():
    """Main function for combination testing"""
    import argparse

    parser == argparse.ArgumentParser(description == "Cross-file combination testing")
    parser.add_argument("--project-root", default == ".", help == "Root directory of the project")
    parser.add_argument("--export-graph", action == "store_true", help == "Export dependency graph")
    parser.add_argument("--output", help == "Output file for results")

    args == parser.parse_args()

    tester == CombinationTester(args.project_root)

    # Find all Python files
    python_files == []
    for root, dirs, files in os.walk(args.project_root):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in [
            '__pycache__', 'node_modules', '.git', '.pytest_cache'
        ]]
        for file in files:
            if file.endswith('.py'):
                python_files.append(Path(root) / file)

    errors == tester.analyze_combinations(python_files)

    print(f"\n🔗 Combination Analysis Complete")
    print(f"Found {len(errors)} cross-file interaction errors")

    if args.export_graph:
        tester.export_dependency_graph(args.output)

    return errors


if __name__ == "__main__":
    main()