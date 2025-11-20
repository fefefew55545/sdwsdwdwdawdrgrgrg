#!/usr/bin/env python3
"""
Advanced Runtime Interaction Analysis System for BSEE Codebase
Global state pollution detection, side effect analysis, and runtime behavior monitoring
"""

import os
import sys
import ast
import subprocess
import tempfile
import importlib.util
import threading
import time
import json
import re
import gc
import psutil
from pathlib import Path
from typing import List, Dict, Any, Optional, Set, Tuple, Callable
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
from contextlib import contextmanager
from collections import defaultdict, deque
import weakref

# Import base classes from existing system
try:
    from advanced_error_detector import ErrorInfo, ErrorSeverity, ErrorCategory
except ImportError:
    # Fallback definitions if import fails
    class ErrorSeverity(Enum):
        CRITICAL = "CRITICAL"
        HIGH = "HIGH"
        MEDIUM = "MEDIUM"
        LOW = "LOW"

    class ErrorCategory(Enum):
        SYNTAX = "SYNTAX"
        IMPORT = "IMPORT"
        RUNTIME = "RUNTIME"
        LOGICAL = "LOGICAL"
        PERFORMANCE = "PERFORMANCE"
        SECURITY = "SECURITY"
        MAINTAINABILITY = "MAINTAINABILITY"
        COMPATIBILITY = "COMPATIBILITY"
        DEAD_CODE = "DEAD_CODE"
        DATA_FLOW = "DATA_FLOW"
        RESOURCE_LEAK = "RESOURCE_LEAK"
        RACE_CONDITION = "RACE_CONDITION"
        COMBINATION = "COMBINATION"

    @dataclass
    class ErrorInfo:
        file_path: str
        error_type: str
        error_message: str
        severity: ErrorSeverity
        category: ErrorCategory
        line_number: Optional[int] = None
        column_number: Optional[int] = None
        context_snippet: Optional[str] = None
        suggested_fix: Optional[str] = None
        dependencies: List[str] = None
        test_context: Optional[str] = None
        fix_applied: bool = False
        verification_status: str = "PENDING"
        timestamp: str = None

        def __post_init__(self):
            if self.timestamp is None:
                self.timestamp = datetime.now().isoformat()
            if self.dependencies is None:
                self.dependencies = []


@dataclass
class RuntimeState:
    """Represents runtime state at a point in time"""
    timestamp: float
    global_variables: Dict[str, Any] = field(default_factory=dict)
    module_attributes: Dict[str, Set[str]] = field(default_factory=dict)
    memory_usage: float = 0.0
    open_files: List[str] = field(default_factory=list)
    thread_count: int = 0
    loaded_modules: Set[str] = field(default_factory=set)


@dataclass
class SideEffectInfo:
    """Information about detected side effects"""
    type: str
    target: str
    source_function: str
    source_file: str
    line_number: int
    timestamp: float
    details: Dict[str, Any] = field(default_factory=dict)


class RuntimeAnalyzer:
    """Advanced runtime interaction analysis system"""

    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.runtime_errors: List[ErrorInfo] = []
        self.global_state_snapshots: List[RuntimeState] = []
        self.detected_side_effects: List[SideEffectInfo] = []
        self.state_pollution_patterns: Dict[str, List[str]] = defaultdict(list)
        self.interface_compatibility_issues: List[ErrorInfo] = []
        self.memory_leak_candidates: List[str] = []

    def analyze_runtime_interactions(self, python_files: List[Path]) -> List[ErrorInfo]:
        """Run comprehensive runtime interaction analysis"""
        print("⚡ Starting Runtime Interaction Analysis")
        print(f"🔍 Analyzing {len(python_files)} files for runtime behavior")

        all_errors = []

        # Phase 1: Static analysis for runtime patterns
        static_errors = self._analyze_runtime_static_patterns(python_files)
        all_errors.extend(static_errors)

        # Phase 2: Dynamic analysis with safe execution
        dynamic_errors = self._analyze_runtime_dynamic_behavior(python_files)
        all_errors.extend(dynamic_errors)

        # Phase 3: Global state pollution analysis
        pollution_errors = self._analyze_global_state_pollution(python_files)
        all_errors.extend(pollution_errors)

        # Phase 4: Side effect detection
        side_effect_errors = self._detect_side_effects(python_files)
        all_errors.extend(side_effect_errors)

        # Phase 5: Interface compatibility analysis
        interface_errors = self._analyze_interface_compatibility(python_files)
        all_errors.extend(interface_errors)

        # Phase 6: Error propagation analysis
        propagation_errors = self._analyze_error_propagation(python_files)
        all_errors.extend(propagation_errors)

        print(f"⚡ Found {len(all_errors)} runtime interaction issues")
        return all_errors

    def _analyze_runtime_static_patterns(self, python_files: List[Path]) -> List[ErrorInfo]:
        """Static analysis for runtime patterns"""
        print("  📊 Analyzing static runtime patterns...")
        errors = []

        for file_path in python_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                tree = ast.parse(content)

                # Analyze for potential runtime issues
                file_errors = self._analyze_file_runtime_patterns(file_path, tree, content)
                errors.extend(file_errors)

            except (SyntaxError, UnicodeDecodeError):
                continue
            except Exception as e:
                errors.append(ErrorInfo(
                    file_path=str(file_path.relative_to(self.project_root)),
                    error_type="StaticRuntimeAnalysisError",
                    error_message=f"Error during static runtime analysis: {str(e)}",
                    severity=ErrorSeverity.LOW,
                    category=ErrorCategory.RUNTIME,
                    suggested_fix="Check file for complex constructs that may interfere with analysis"
                ))

        return errors

    def _analyze_file_runtime_patterns(self, file_path: Path, tree: ast.AST, content: str) -> List[ErrorInfo]:
        """Analyze a single file for runtime patterns"""
        errors = []
        rel_path = str(file_path.relative_to(self.project_root))

        class RuntimePatternAnalyzer(ast.NodeVisitor):
            def __init__(self):
                self.global_modifications = []
                self.function_calls = []
                self.class_modifications = []
                self.import_at_runtime = []

            def visit_Assign(self, node: ast.Assign):
                # Check for global variable modifications
                if isinstance(node.targets[0], ast.Name):
                    var_name = node.targets[0].id
                    # Check if it's a common global pattern
                    if var_name.isupper() or var_name.startswith('global_'):
                        self.global_modifications.append((var_name, node.lineno))

                self.generic_visit(node)

            def visit_Call(self, node: ast.Call):
                # Track function calls
                if isinstance(node.func, ast.Name):
                    self.function_calls.append((node.func.id, node.lineno))
                elif isinstance(node.func, ast.Attribute):
                    self.function_calls.append((node.func.attr, node.lineno))

                # Check for runtime imports
                if isinstance(node.func, ast.Name) and node.func.id == 'import':
                    self.import_at_runtime.append(('import', node.lineno))
                elif isinstance(node.func, ast.Name) and node.func.id == '__import__':
                    self.import_at_runtime.append(('__import__', node.lineno))

                self.generic_visit(node)

            def visit_Import(self, node: ast.Import):
                # Regular imports at module level are fine
                self.generic_visit(node)

            def visit_ImportFrom(self, node: ast.ImportFrom):
                # Regular from imports at module level are fine
                self.generic_visit(node)

        analyzer = RuntimePatternAnalyzer()
        analyzer.visit(tree)

        # Analyze collected patterns
        for var_name, line_num in analyzer.global_modifications:
            errors.append(ErrorInfo(
                file_path=rel_path,
                error_type="GlobalVariableModification",
                error_message=f"Potential global variable modification: '{var_name}' at line {line_num}",
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                line_number=line_num,
                suggested_fix=f"Consider if modification of '{var_name}' is intentional or use dependency injection"
            ))

        # Check for runtime imports
        for import_type, line_num in analyzer.import_at_runtime:
            errors.append(ErrorInfo(
                file_path=rel_path,
                error_type="RuntimeImport",
                error_message=f"Runtime import detected at line {line_num} using {import_type}",
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                line_number=line_num,
                suggested_fix="Move imports to module level or use lazy loading patterns"
            ))

        # Check for potentially problematic function calls
        problematic_calls = ['exec', 'eval', 'compile', 'open', 'subprocess.run', 'os.system']
        for func_name, line_num in analyzer.function_calls:
            if func_name in problematic_calls:
                severity = ErrorSeverity.HIGH if func_name in ['exec', 'eval'] else ErrorSeverity.MEDIUM
                errors.append(ErrorInfo(
                    file_path=rel_path,
                    error_type="PotentiallyDangerousCall",
                    error_message=f"Potentially dangerous function call: '{func_name}()' at line {line_num}",
                    severity=severity,
                    category=ErrorCategory.RUNTIME,
                    line_number=line_num,
                    suggested_fix=f"Review usage of '{func_name}' for security implications"
                ))

        return errors

    def _analyze_runtime_dynamic_behavior(self, python_files: List[Path]) -> List[ErrorInfo]:
        """Dynamic analysis with safe execution"""
        print("  🧪 Analyzing dynamic runtime behavior...")
        errors = []

        # Limit the number of files for dynamic analysis to avoid timeout
        max_files = min(5, len(python_files))
        selected_files = python_files[:max_files]

        for file_path in selected_files:
            try:
                file_errors = self._safe_dynamic_analysis(file_path)
                errors.extend(file_errors)
            except Exception as e:
                errors.append(ErrorInfo(
                    file_path=str(file_path.relative_to(self.project_root)),
                    error_type="DynamicAnalysisError",
                    error_message=f"Error during dynamic analysis: {str(e)}",
                    severity=ErrorSeverity.LOW,
                    category=ErrorCategory.RUNTIME,
                    suggested_fix="Check file for unsafe execution patterns"
                ))

        return errors

    def _safe_dynamic_analysis(self, file_path: Path) -> List[ErrorInfo]:
        """Safe dynamic analysis of a single file"""
        errors = []
        rel_path = str(file_path.relative_to(self.project_root))

        # Create a sandboxed environment for testing
        test_script = f"""
import sys
import os
import importlib.util
import warnings
import builtins

# Capture dangerous builtins
original_exec = builtins.exec
original_eval = builtins.eval
dangerous_calls = []

def safe_exec(*args, **kwargs):
    dangerous_calls.append(('exec', args[0] if args else 'None'))
    return original_exec(*args, **kwargs)

def safe_eval(*args, **kwargs):
    dangerous_calls.append(('eval', args[0] if args else 'None'))
    return original_eval(*args, **kwargs)

# Override dangerous builtins
builtins.exec = safe_exec
builtins.eval = safe_eval

# Ignore warnings during analysis
warnings.filterwarnings('ignore')

# Set up path
sys.path.insert(0, os.getcwd())

# Module state tracking
module_globals = {{}}
module_state = []

def track_module_state(name, globals_dict):
    module_state.append({{
        'name': name,
        'globals_count': len(globals_dict),
        'keys': list(globals_dict.keys())
    }})

try:
    # Load and execute the module
    spec = importlib.util.spec_from_file_location('test_module', '{file_path}')
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)

        # Track initial state
        track_module_state('initial', module.__dict__)

        # Execute the module
        spec.loader.exec_module(module)

        # Track final state
        track_module_state('final', module.__dict__)

        # Print results
        print("MODULE_LOADED_SUCCESSFULLY")
        print(f"DANGEROUS_CALLS: {{len(dangerous_calls)}}")
        print(f"MODULE_STATE_CHANGES: {{len(module_state)}}")

        for call in dangerous_calls:
            print(f"DANGEROUS_CALL: {{call[0]}} - {{call[1][:100]}}...")

        for state in module_state:
            print(f"STATE: {{state}}")

except Exception as e:
    print(f"EXECUTION_ERROR: {{e}}")
    import traceback
    traceback.print_exc()

# Restore original builtins
builtins.exec = original_exec
builtins.eval = original_eval
"""

        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
            temp_file.write(test_script)
            temp_file_path = temp_file.name

        try:
            result = subprocess.run(
                [sys.executable, temp_file_path],
                capture_output=True,
                text=True,
                timeout=30,  # Short timeout for safety
                cwd=str(self.project_root)
            )

            output = result.stdout + result.stderr

            # Analyze the output for runtime issues
            if "EXECUTION_ERROR" in output:
                error_lines = [line for line in output.split('\n') if line.startswith('EXECUTION_ERROR:')]
                if error_lines:
                    error_msg = error_lines[0].split(':', 1)[1].strip()
                    errors.append(ErrorInfo(
                        file_path=rel_path,
                        error_type="RuntimeExecutionError",
                        error_message=f"Runtime execution error: {error_msg}",
                        severity=ErrorSeverity.HIGH,
                        category=ErrorCategory.RUNTIME,
                        suggested_fix="Debug runtime error in the module"
                    ))

            if "DANGEROUS_CALLS:" in output:
                call_count_match = re.search(r'DANGEROUS_CALLS:\s*(\d+)', output)
                if call_count_match and int(call_count_match.group(1)) > 0:
                    errors.append(ErrorInfo(
                        file_path=rel_path,
                        error_type="DangerousFunctionUsage",
                        error_message=f"Module uses {call_count_match.group(1)} dangerous functions (exec/eval)",
                        severity=ErrorSeverity.MEDIUM,
                        category=ErrorCategory.RUNTIME,
                        suggested_fix="Review and replace dangerous function usage"
                    ))

            if "MODULE_STATE_CHANGES:" in output:
                # Check for excessive global state changes
                state_lines = [line for line in output.split('\n') if line.startswith('STATE:')]
                if len(state_lines) > 2:  # More than just initial and final
                    errors.append(ErrorInfo(
                        file_path=rel_path,
                        error_type="ExcessiveGlobalState",
                        error_message=f"Module shows excessive global state changes during execution",
                        severity=ErrorSeverity.LOW,
                        category=ErrorCategory.RUNTIME,
                        suggested_fix="Consider reducing global state usage"
                    ))

        except subprocess.TimeoutExpired:
            errors.append(ErrorInfo(
                file_path=rel_path,
                error_type="RuntimeTimeout",
                error_message="Module execution timed out during analysis",
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                suggested_fix="Check for infinite loops or blocking operations"
            ))
        except Exception as e:
            errors.append(ErrorInfo(
                file_path=rel_path,
                error_type="DynamicAnalysisError",
                error_message=f"Error during dynamic analysis: {str(e)}",
                severity=ErrorSeverity.LOW,
                category=ErrorCategory.RUNTIME
            ))
        finally:
            try:
                os.unlink(temp_file_path)
            except:
                pass

        return errors

    def _analyze_global_state_pollution(self, python_files: List[Path]) -> List[ErrorInfo]:
        """Analyze global state pollution patterns"""
        print("  🌍 Analyzing global state pollution...")
        errors = []

        # Analyze files for global state patterns
        for file_path in python_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                tree = ast.parse(content)

                file_errors = self._analyze_file_global_pollution(file_path, tree, content)
                errors.extend(file_errors)

            except (SyntaxError, UnicodeDecodeError):
                continue
            except Exception as e:
                errors.append(ErrorInfo(
                    file_path=str(file_path.relative_to(self.project_root)),
                    error_type="GlobalStateAnalysisError",
                    error_message=f"Error analyzing global state: {str(e)}",
                    severity=ErrorSeverity.LOW,
                    category=ErrorCategory.RUNTIME
                ))

        return errors

    def _analyze_file_global_pollution(self, file_path: Path, tree: ast.AST, content: str) -> List[ErrorInfo]:
        """Analyze a single file for global state pollution"""
        errors = []
        rel_path = str(file_path.relative_to(self.project_root))

        class GlobalStateAnalyzer(ast.NodeVisitor):
            def __init__(self):
                self.global_modifications = []
                self.function_global_declarations = []
                self.class_level_modifications = []
                self.module_level_assignments = []

            def visit_Global(self, node: ast.Global):
                for name in node.names:
                    self.function_global_declarations.append((name, node.lineno))
                self.generic_visit(node)

            def visit_Assign(self, node: ast.Assign):
                # Check if this is at module level
                if hasattr(node, 'parent'):
                    parent = node.parent
                    # Check if we're at module level (not inside a function or class)
                    if not isinstance(parent, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                        if isinstance(node.targets[0], ast.Name):
                            self.module_level_assignments.append((node.targets[0].id, node.lineno))

                self.generic_visit(node)

            def visit_Attribute(self, node: ast.Attribute):
                # Check for modifications to module-level attributes
                if isinstance(node.ctx, ast.Store):
                    if isinstance(node.value, ast.Name) and node.value.id in ['sys', 'os', 'builtins']:
                        self.class_level_modifications.append((f"{node.value.id}.{node.attr}", node.lineno))

                self.global_visit(node)

        # Set parent references
        class ParentSetter(ast.NodeTransformer):
            def visit(self, node):
                for child in ast.iter_child_nodes(node):
                    child.parent = node
                return self.generic_visit(node)

        ParentSetter().visit(tree)

        analyzer = GlobalStateAnalyzer()
        analyzer.visit(tree)

        # Check for module-level variable pollution
        for var_name, line_num in analyzer.module_level_assignments:
            if var_name.isupper() or '_' in var_name:
                # Likely intentional global constants
                continue

            errors.append(ErrorInfo(
                file_path=rel_path,
                error_type="ModuleLevelVariable",
                error_message=f"Module-level variable assignment: '{var_name}' at line {line_num}",
                severity=ErrorSeverity.LOW,
                category=ErrorCategory.RUNTIME,
                line_number=line_num,
                suggested_fix=f"Consider if '{var_name}' should be inside a function or class"
            ))

        # Check for global declarations
        for var_name, line_num in analyzer.function_global_declarations:
            errors.append(ErrorInfo(
                file_path=rel_path,
                error_type="GlobalDeclaration",
                error_message=f"Global variable declaration: '{var_name}' at line {line_num}",
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                line_number=line_num,
                suggested_fix=f"Consider refactoring to avoid global variables or use dependency injection"
            ))

        # Check for modifications to system modules
        for target, line_num in analyzer.class_level_modifications:
            errors.append(ErrorInfo(
                file_path=rel_path,
                error_type="SystemModuleModification",
                error_message=f"Modification to system module: '{target}' at line {line_num}",
                severity=ErrorSeverity.HIGH,
                category=ErrorCategory.RUNTIME,
                line_number=line_num,
                suggested_fix="Avoid modifying system modules at runtime"
            ))

        return errors

    def _detect_side_effects(self, python_files: List[Path]) -> List[ErrorInfo]:
        """Detect functions with side effects"""
        print("  🔍 Detecting side effects...")
        errors = []

        for file_path in python_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                tree = ast.parse(content)

                file_errors = self._detect_file_side_effects(file_path, tree, content)
                errors.extend(file_errors)

            except (SyntaxError, UnicodeDecodeError):
                continue
            except Exception as e:
                errors.append(ErrorInfo(
                    file_path=str(file_path.relative_to(self.project_root)),
                    error_type="SideEffectAnalysisError",
                    error_message=f"Error detecting side effects: {str(e)}",
                    severity=ErrorSeverity.LOW,
                    category=ErrorCategory.RUNTIME
                ))

        return errors

    def _detect_file_side_effects(self, file_path: Path, tree: ast.AST, content: str) -> List[ErrorInfo]:
        """Detect side effects in a single file"""
        errors = []
        rel_path = str(file_path.relative_to(self.project_root))

        class SideEffectDetector(ast.NodeVisitor):
            def __init__(self):
                self.side_effect_functions = []
                self.pure_function_candidates = []

            def visit_FunctionDef(self, node: ast.FunctionDef):
                has_side_effects = self._analyze_function_side_effects(node)
                if has_side_effects:
                    self.side_effect_functions.append((node.name, node.lineno))
                else:
                    # Check if function name suggests it should be pure
                    if self._should_be_pure(node.name):
                        self.pure_function_candidates.append((node.name, node.lineno))

                self.generic_visit(node)

            def _analyze_function_side_effects(self, node: ast.FunctionDef) -> bool:
                """Analyze if a function has side effects"""
                side_effect_indicators = [
                    'open(', 'write(', 'read(', 'close(',
                    'print(', 'input(', 'sys.stdout', 'sys.stderr',
                    'os.environ', 'os.mkdir', 'os.remove', 'os.rename',
                    'subprocess.', 'os.system',
                    'global ', 'nonlocal ',
                    'threading.', 'multiprocessing.',
                    'socket.', 'urllib.', 'http.',
                    'json.dump(', 'json.load(',
                    'pickle.dump(', 'pickle.load('
                ]

                function_source = ast.get_source_segment(content, node)
                if function_source:
                    for indicator in side_effect_indicators:
                        if indicator in function_source:
                            return True

                return False

            def _should_be_pure(self, function_name: str) -> bool:
                """Check if function name suggests it should be pure"""
                pure_patterns = [
                    'get_', 'find_', 'calculate_', 'compute_', 'is_', 'has_', 'should_',
                    'validate_', 'check_', 'test_', 'parse_', 'format_', 'transform_'
                ]
                return any(function_name.startswith(pattern) for pattern in pure_patterns)

        detector = SideEffectDetector()
        detector.visit(tree)

        # Report functions with side effects
        for func_name, line_num in detector.side_effect_functions:
            errors.append(ErrorInfo(
                file_path=rel_path,
                error_type="FunctionWithSideEffects",
                error_message=f"Function '{func_name}' appears to have side effects",
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                line_number=line_num,
                suggested_fix=f"Consider making '{func_name}' pure or documenting its side effects"
            ))

        # Report functions that should be pure but aren't
        for func_name, line_num in detector.pure_function_candidates:
            # This is just a warning since they might actually be pure
            pass  # Don't report as error since they might be fine

        return errors

    def _analyze_interface_compatibility(self, python_files: List[Path]) -> List[ErrorInfo]:
        """Analyze interface compatibility issues"""
        print("  🔌 Analyzing interface compatibility...")
        errors = []

        # Build function signature database
        function_signatures = {}
        class_methods = defaultdict(dict)

        for file_path in python_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                tree = ast.parse(content)

                self._extract_signatures(file_path, tree, function_signatures, class_methods)

            except (SyntaxError, UnicodeDecodeError):
                continue
            except Exception as e:
                errors.append(ErrorInfo(
                    file_path=str(file_path.relative_to(self.project_root)),
                    error_type="InterfaceAnalysisError",
                    error_message=f"Error analyzing interfaces: {str(e)}",
                    severity=ErrorSeverity.LOW,
                    category=ErrorCategory.RUNTIME
                ))

        # Check for compatibility issues
        compatibility_errors = self._check_interface_compatibility(
            function_signatures, class_methods, python_files
        )
        errors.extend(compatibility_errors)

        return errors

    def _extract_signatures(self, file_path: Path, tree: ast.AST,
                          function_signatures: Dict[str, List[Tuple]],
                          class_methods: Dict[str, Dict[str, List[Tuple]]]):
        """Extract function and method signatures"""
        rel_path = str(file_path.relative_to(self.project_root))

        class SignatureExtractor(ast.NodeVisitor):
            def visit_FunctionDef(self, node: ast.FunctionDef):
                signature = self._get_signature(node)
                function_signatures.setdefault(node.name, []).append((rel_path, node.lineno, signature))

                # If inside a class, also add to class methods
                if hasattr(node, 'parent'):
                    parent = node.parent
                    if isinstance(parent, ast.ClassDef):
                        class_methods[parent.name][node.name] = (rel_path, node.lineno, signature)

                self.generic_visit(node)

            def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
                self.visit_FunctionDef(node)

            def _get_signature(self, node) -> str:
                args = [arg.arg for arg in node.args.args]
                returns = ast.unparse(node.returns) if hasattr(node, 'returns') and node.returns else "None"
                return f"({', '.join(args)}) -> {returns}"

        extractor = SignatureExtractor()
        extractor.visit(tree)

    def _check_interface_compatibility(self, function_signatures: Dict[str, List[Tuple]],
                                     class_methods: Dict[str, Dict[str, List[Tuple]]],
                                     python_files: List[Path]) -> List[ErrorInfo]:
        """Check for interface compatibility issues"""
        errors = []

        # Check for function signature inconsistencies
        for func_name, implementations in function_signatures.items():
            if len(implementations) > 1:
                signatures = [impl[2] for impl in implementations]
                unique_signatures = set(signatures)

                if len(unique_signatures) > 1:
                    # Multiple different signatures for the same function name
                    error_info = ErrorInfo(
                        file_path="multiple_files",
                        error_type="InconsistentFunctionSignature",
                        error_message=f"Function '{func_name}' has inconsistent signatures across files: {unique_signatures}",
                        severity=ErrorSeverity.MEDIUM,
                        category=ErrorCategory.RUNTIME,
                        dependencies=[impl[0] for impl in implementations],
                        suggested_fix=f"Standardize the signature for function '{func_name}' across all implementations"
                    )
                    errors.append(error_info)

        # Check for class method signature inconsistencies
        for class_name, methods in class_methods.items():
            if len(methods) > 1:  # Class defined in multiple files
                for method_name, implementations in methods.items():
                    if isinstance(implementations, list) and len(implementations) > 1:
                        signatures = [impl[2] for impl in implementations]
                        unique_signatures = set(signatures)

                        if len(unique_signatures) > 1:
                            error_info = ErrorInfo(
                                file_path="multiple_files",
                                error_type="InconsistentMethodSignature",
                                error_message=f"Method '{class_name}.{method_name}' has inconsistent signatures: {unique_signatures}",
                                severity=ErrorSeverity.MEDIUM,
                                category=ErrorCategory.RUNTIME,
                                dependencies=[impl[0] for impl in implementations],
                                suggested_fix=f"Standardize method signature for '{class_name}.{method_name}'"
                            )
                            errors.append(error_info)

        return errors

    def _analyze_error_propagation(self, python_files: List[Path]) -> List[ErrorInfo]:
        """Analyze error propagation patterns"""
        print("  🚨 Analyzing error propagation...")
        errors = []

        for file_path in python_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                tree = ast.parse(content)

                file_errors = self._analyze_file_error_propagation(file_path, tree, content)
                errors.extend(file_errors)

            except (SyntaxError, UnicodeDecodeError):
                continue
            except Exception as e:
                errors.append(ErrorInfo(
                    file_path=str(file_path.relative_to(self.project_root)),
                    error_type="ErrorPropagationAnalysisError",
                    error_message=f"Error analyzing error propagation: {str(e)}",
                    severity=ErrorSeverity.LOW,
                    category=ErrorCategory.RUNTIME
                ))

        return errors

    def _analyze_file_error_propagation(self, file_path: Path, tree: ast.AST, content: str) -> List[ErrorInfo]:
        """Analyze error propagation in a single file"""
        errors = []
        rel_path = str(file_path.relative_to(self.project_root))

        class ErrorPropagationAnalyzer(ast.NodeVisitor):
            def __init__(self):
                self.exception_handlers = []
                self.raises = []
                self.function_error_patterns = []

            def visit_FunctionDef(self, node: ast.FunctionDef):
                # Analyze function for error handling patterns
                handlers = self._find_exception_handlers(node)
                raises = self._find_raises(node)

                if handlers and not raises:
                    # Function handles exceptions but doesn't raise any
                    self.function_error_patterns.append(('error_handling_only', node.name, node.lineno))
                elif raises and not handlers:
                    # Function raises exceptions but doesn't handle any
                    self.function_error_patterns.append(('error_raising_only', node.name, node.lineno))
                elif not handlers and not raises:
                    # Function has no explicit error handling
                    if 'test' not in node.name.lower():  # Skip test functions
                        self.function_error_patterns.append(('no_error_handling', node.name, node.lineno))

                self.generic_visit(node)

            def visit_Try(self, node: ast.Try):
                for handler in node.handlers:
                    if not handler.body or (len(handler.body) == 1 and isinstance(handler.body[0], ast.Pass)):
                        self.exception_handlers.append(('empty_handler', handler.lineno))
                    elif handler.type is None:
                        self.exception_handlers.append(('bare_except', handler.lineno))
                    elif isinstance(handler.type, ast.Name) and handler.type.id == 'Exception':
                        self.exception_handlers.append(('broad_exception', handler.lineno))

                self.generic_visit(node)

            def visit_Raise(self, node: ast.Raise):
                if node.exc:
                    self.raises.append(('explicit_raise', node.lineno))
                else:
                    self.raises.append(('bare_raise', node.lineno))

                self.generic_visit(node)

            def _find_exception_handlers(self, node: ast.FunctionDef) -> List[ast.ExceptHandler]:
                handlers = []
                for child in ast.walk(node):
                    if isinstance(child, ast.ExceptHandler):
                        handlers.append(child)
                return handlers

            def _find_raises(self, node: ast.FunctionDef) -> List[ast.Raise]:
                raises = []
                for child in ast.walk(node):
                    if isinstance(child, ast.Raise):
                        raises.append(child)
                return raises

        analyzer = ErrorPropagationAnalyzer()
        analyzer.visit(tree)

        # Report error handling issues
        for pattern_type, func_name, line_num in analyzer.function_error_patterns:
            if pattern_type == 'no_error_handling':
                errors.append(ErrorInfo(
                    file_path=rel_path,
                    error_type="NoErrorHandling",
                    error_message=f"Function '{func_name}' has no explicit error handling",
                    severity=ErrorSeverity.LOW,
                    category=ErrorCategory.RUNTIME,
                    line_number=line_num,
                    suggested_fix=f"Consider adding error handling to '{func_name}' if it may encounter errors"
                ))

        for handler_type, line_num in analyzer.exception_handlers:
            if handler_type == 'empty_handler':
                errors.append(ErrorInfo(
                    file_path=rel_path,
                    error_type="EmptyExceptionHandler",
                    error_message=f"Empty exception handler at line {line_num}",
                    severity=ErrorSeverity.MEDIUM,
                    category=ErrorCategory.RUNTIME,
                    line_number=line_num,
                    suggested_fix="Add proper error handling or remove the exception handler"
                ))
            elif handler_type == 'bare_except':
                errors.append(ErrorInfo(
                    file_path=rel_path,
                    error_type="BareExceptHandler",
                    error_message=f"Bare except handler at line {line_num}",
                    severity=ErrorSeverity.HIGH,
                    category=ErrorCategory.RUNTIME,
                    line_number=line_num,
                    suggested_fix="Catch specific exceptions instead of bare except"
                ))
            elif handler_type == 'broad_exception':
                errors.append(ErrorInfo(
                    file_path=rel_path,
                    error_type="BroadExceptionHandler",
                    error_message=f"Broad exception handler (catches Exception) at line {line_num}",
                    severity=ErrorSeverity.MEDIUM,
                    category=ErrorCategory.RUNTIME,
                    line_number=line_num,
                    suggested_fix="Catch more specific exception types"
                ))

        return errors


def main():
    """Main function for runtime analysis"""
    import argparse

    parser = argparse.ArgumentParser(description="Runtime interaction analysis")
    parser.add_argument("--project-root", default=".", help="Root directory of the project")
    parser.add_argument("--file", help="Specific file to analyze")

    args = parser.parse_args()

    analyzer = RuntimeAnalyzer(args.project_root)

    if args.file:
        file_path = Path(args.file)
        if file_path.exists():
            errors = analyzer.analyze_runtime_interactions([file_path])
            print(f"Found {len(errors)} runtime interaction issues in {args.file}")
            for error in errors:
                print(f"  {error.error_type}: {error.error_message}")
        else:
            print(f"File not found: {args.file}")
    else:
        # Find all Python files
        python_files = []
        for root, dirs, files in os.walk(args.project_root):
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in [
                '__pycache__', 'node_modules', '.git', '.pytest_cache'
            ]]
            for file in files:
                if file.endswith('.py'):
                    python_files.append(Path(root) / file)

        errors = analyzer.analyze_runtime_interactions(python_files)
        print(f"\n⚡ Runtime Analysis Complete")
        print(f"Found {len(errors)} runtime interaction issues")

    return errors


if __name__ == "__main__":
    main()