#!/usr/bin/env python3
"""
Advanced Logical Error Detection System for BSEE Codebase
Dead code detection, data flow analysis, and sophisticated logical anti-pattern detection
"""

import ast
import re
from pathlib import Path
from typing import List, Dict, Any, Optional, Set, Tuple, Union
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

# Import base classes from existing system
import sys
sys.path.append(str(Path(__file__).parent))

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


class SymbolType(Enum):
    """Types of symbols for analysis"""
    VARIABLE = "VARIABLE"
    FUNCTION = "FUNCTION"
    CLASS = "CLASS"
    IMPORT = "IMPORT"
    PARAMETER = "PARAMETER"


@dataclass
class SymbolInfo:
    """Information about a symbol in the code"""
    name: str
    symbol_type: SymbolType
    defined_at: Tuple[int, int]  # (line, column)
    first_used: Optional[Tuple[int, int]] = None
    usage_count: int = 0
    is_used: bool = False
    scope: str = "global"
    is_exported: bool = False
    is_private: bool = False
    assigned_values: List[Any] = None
    used_in_expressions: List[str] = None

    def __post_init__(self):
        if self.assigned_values is None:
            self.assigned_values = []
        if self.used_in_expressions is None:
            self.used_in_expressions = []


class LogicalErrorDetector:
    """Advanced logical error detection system"""

    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.symbol_tables: Dict[str, Dict[str, SymbolInfo]] = {}
        self.import_graph: Dict[str, Set[str]] = {}
        self.function_call_graph: Dict[str, Set[str]] = {}

    def detect_logical_errors(self, file_path: Path) -> List[ErrorInfo]:
        """Run comprehensive logical error detection on a file"""
        errors = []

        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content)

            # Phase 1: Build symbol table and analyze usage
            symbol_table = self._build_symbol_table(tree, content)
            self.symbol_tables[str(file_path)] = symbol_table

            # Phase 2: Detect dead code
            dead_code_errors = self._detect_dead_code(file_path, symbol_table, content)
            errors.extend(dead_code_errors)

            # Phase 3: Data flow analysis
            data_flow_errors = self._detect_data_flow_issues(file_path, tree, content)
            errors.extend(data_flow_errors)

            # Phase 4: Resource leak detection
            resource_leak_errors = self._detect_resource_leaks(file_path, tree, content)
            errors.extend(resource_leak_errors)

            # Phase 5: Race condition detection
            race_condition_errors = self._detect_race_conditions(file_path, tree, content)
            errors.extend(race_condition_errors)

            # Phase 6: Advanced logical anti-patterns
            logical_pattern_errors = self._detect_logical_anti_patterns(file_path, tree, content)
            errors.extend(logical_pattern_errors)

        except SyntaxError as e:
            # Don't analyze files with syntax errors
            pass
        except Exception as e:
            errors.append(ErrorInfo(
                file_path=str(file_path.relative_to(self.project_root)),
                error_type="LogicalAnalysisError",
                error_message=f"Error during logical analysis: {str(e)}",
                severity=ErrorSeverity.LOW,
                category=ErrorCategory.LOGICAL,
                suggested_fix="Review file structure and complex constructs"
            ))

        return errors

    def _build_symbol_table(self, tree: ast.AST, content: str) -> Dict[str, SymbolInfo]:
        """Build comprehensive symbol table with usage tracking"""
        symbol_table = {}

        class SymbolVisitor(ast.NodeVisitor):
            def __init__(self):
                self.current_scope = "global"
                self.current_function = None
                self.import_names = set()
                self.function_definitions = {}
                self.class_definitions = {}

            def visit_Import(self, node: ast.Import):
                for alias in node.names:
                    name = alias.asname if alias.asname else alias.name
                    symbol_table[name] = SymbolInfo(
                        name=name,
                        symbol_type=SymbolType.IMPORT,
                        defined_at=(node.lineno, node.col_offset),
                        is_exported=True,
                        scope=self.current_scope
                    )
                self.import_names.add(alias.name)
                self.generic_visit(node)

            def visit_ImportFrom(self, node: ast.ImportFrom):
                for alias in node.names:
                    name = alias.asname if alias.asname else alias.name
                    symbol_table[name] = SymbolInfo(
                        name=name,
                        symbol_type=SymbolType.IMPORT,
                        defined_at=(node.lineno, node.col_offset),
                        is_exported=True,
                        scope=self.current_scope
                    )
                self.generic_visit(node)

            def visit_FunctionDef(self, node: ast.FunctionDef):
                old_scope = self.current_scope
                old_function = self.current_function

                self.current_scope = f"function:{node.name}"
                self.current_function = node.name

                # Add function to symbol table
                symbol_table[node.name] = SymbolInfo(
                    name=node.name,
                    symbol_type=SymbolType.FUNCTION,
                    defined_at=(node.lineno, node.col_offset),
                    is_exported=not node.name.startswith('_'),
                    is_private=node.name.startswith('_'),
                    scope=old_scope
                )

                # Add parameters
                for arg in node.args.args:
                    symbol_table[arg.arg] = SymbolInfo(
                        name=arg.arg,
                        symbol_type=SymbolType.PARAMETER,
                        defined_at=(node.lineno, node.col_offset),
                        scope=self.current_scope
                    )

                # Visit function body
                self.generic_visit(node)

                self.current_scope = old_scope
                self.current_function = old_function

            def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
                # Handle async functions the same way
                self.visit_FunctionDef(node)

            def visit_ClassDef(self, node: ast.ClassDef):
                old_scope = self.current_scope
                self.current_scope = f"class:{node.name}"

                # Add class to symbol table
                symbol_table[node.name] = SymbolInfo(
                    name=node.name,
                    symbol_type=SymbolType.CLASS,
                    defined_at=(node.lineno, node.col_offset),
                    is_exported=not node.name.startswith('_'),
                    is_private=node.name.startswith('_'),
                    scope=old_scope
                )

                self.generic_visit(node)
                self.current_scope = old_scope

            def visit_Assign(self, node: ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        name = target.id

                        if name not in symbol_table:
                            symbol_table[name] = SymbolInfo(
                                name=name,
                                symbol_type=SymbolType.VARIABLE,
                                defined_at=(node.lineno, node.col_offset),
                                is_private=name.startswith('_'),
                                scope=self.current_scope
                            )

                        # Track assignment
                        try:
                            # Try to evaluate the assigned value if it's simple
                            if isinstance(node.value, ast.Constant):
                                symbol_table[name].assigned_values.append(node.value.value)
                            else:
                                symbol_table[name].assigned_values.append(type(node.value).__name__)
                        except:
                            symbol_table[name].assigned_values.append("unknown")

                self.generic_visit(node)

            def visit_Name(self, node: ast.Name):
                if isinstance(node.ctx, ast.Load):
                    # Variable is being used
                    if node.id in symbol_table:
                        symbol_table[node.id].is_used = True
                        symbol_table[node.id].usage_count += 1
                        if symbol_table[node.id].first_used is None:
                            symbol_table[node.id].first_used = (node.lineno, node.col_offset)

                        # Track usage in expressions
                        if hasattr(node, 'parent'):
                            parent_type = type(node.parent).__name__
                            symbol_table[node.id].used_in_expressions.append(parent_type)

                self.generic_visit(node)

        # First pass: visit nodes and build initial symbol table
        visitor = SymbolVisitor()

        # We need to set parent references for context
        class ParentSetter(ast.NodeTransformer):
            def visit(self, node):
                for child in ast.iter_child_nodes(node):
                    child.parent = node
                return self.generic_visit(node)

        ParentSetter().visit(tree)
        visitor.visit(tree)

        return symbol_table

    def _detect_dead_code(self, file_path: Path, symbol_table: Dict[str, SymbolInfo], content: str) -> List[ErrorInfo]:
        """Detect various forms of dead code"""
        errors = []

        # 1. Unused variables
        for name, symbol in symbol_table.items():
            if (symbol.symbol_type in [SymbolType.VARIABLE, SymbolType.PARAMETER] and
                not symbol.is_used and
                not symbol.is_private and
                not name.startswith('_') and
                symbol.assigned_values):  # Only report if actually assigned

                errors.append(ErrorInfo(
                    file_path=str(file_path.relative_to(self.project_root)),
                    error_type="UnusedVariable",
                    error_message=f"Variable '{name}' is assigned but never used",
                    severity=ErrorSeverity.LOW,
                    category=ErrorCategory.DEAD_CODE,
                    line_number=symbol.defined_at[0],
                    context_snippet=self._get_context_line(content, symbol.defined_at[0]),
                    suggested_fix=f"Remove unused variable '{name}' or prefix with underscore if intentional"
                ))

        # 2. Unused functions
        for name, symbol in symbol_table.items():
            if (symbol.symbol_type == SymbolType.FUNCTION and
                not symbol.is_used and
                not symbol.is_exported and
                name != 'main' and
                not name.startswith('test_')):

                errors.append(ErrorInfo(
                    file_path=str(file_path.relative_to(self.project_root)),
                    error_type="UnusedFunction",
                    error_message=f"Function '{name}' is defined but never called",
                    severity=ErrorSeverity.MEDIUM,
                    category=ErrorCategory.DEAD_CODE,
                    line_number=symbol.defined_at[0],
                    context_snippet=self._get_context_line(content, symbol.defined_at[0]),
                    suggested_fix=f"Remove unused function '{name}' or mark as private with underscore prefix"
                ))

        # 3. Unused imports
        for name, symbol in symbol_table.items():
            if symbol.symbol_type == SymbolType.IMPORT and not symbol.is_used:
                errors.append(ErrorInfo(
                    file_path=str(file_path.relative_to(self.project_root)),
                    error_type="UnusedImport",
                    error_message=f"Import '{name}' is never used",
                    severity=ErrorSeverity.LOW,
                    category=ErrorCategory.DEAD_CODE,
                    line_number=symbol.defined_at[0],
                    context_snippet=self._get_context_line(content, symbol.defined_at[0]),
                    suggested_fix=f"Remove unused import '{name}'"
                ))

        # 4. Unreachable code detection
        unreachable_errors = self._detect_unreachable_code(file_path, content)
        errors.extend(unreachable_errors)

        return errors

    def _detect_unreachable_code(self, file_path: Path, content: str) -> List[ErrorInfo]:
        """Detect unreachable code paths"""
        errors = []
        lines = content.split('\n')

        try:
            tree = ast.parse(content)

            class UnreachableCodeDetector(ast.NodeVisitor):
                def visit_FunctionDef(self, node: ast.FunctionDef):
                    self._check_unreachable_in_node(node)
                    self.generic_visit(node)

                def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
                    self._check_unreachable_in_node(node)
                    self.generic_visit(node)

                def _check_unreachable_in_node(self, node):
                    """Check for unreachable code within a node"""
                    statements = list(ast.iter_child_nodes(node))

                    for i, stmt in enumerate(statements):
                        # Check for statements after unconditional return/raise
                        if self._is_unconditional_exit(stmt):
                            remaining_stmts = statements[i+1:]
                            for remaining_stmt in remaining_stmts:
                                if hasattr(remaining_stmt, 'lineno'):
                                    errors.append(ErrorInfo(
                                        file_path=str(file_path.relative_to(self.project_root)),
                                        error_type="UnreachableCode",
                                        error_message=f"Unreachable code after unconditional exit at line {remaining_stmt.lineno}",
                                        severity=ErrorSeverity.MEDIUM,
                                        category=ErrorCategory.DEAD_CODE,
                                        line_number=remaining_stmt.lineno,
                                        context_snippet=self._get_context_line(content, remaining_stmt.lineno),
                                        suggested_fix="Remove unreachable code or restructure control flow"
                                    ))
                                    break  # Only report once per block

                def _is_unconditional_exit(self, node):
                    """Check if node is an unconditional exit point"""
                    return (isinstance(node, ast.Return) and node.value is None) or \
                           (isinstance(node, ast.Raise) and not node.exc) or \
                           (isinstance(node, (ast.Break, ast.Continue)))

            detector = UnreachableCodeDetector()
            detector.visit(tree)

        except SyntaxError:
            pass  # Skip if file has syntax errors

        # Additional pattern-based unreachable code detection
        for line_num, line in enumerate(lines, 1):
            line_stripped = line.strip()

            # Check for code after return/raise/break statements
            if any(keyword in line_stripped for keyword in ['return ', 'raise ', 'break ', 'continue ']):
                # Look for code on same line after statement
                if ';' in line_stripped:
                    parts = line_stripped.split(';')
                    if len(parts) > 1 and parts[1].strip():
                        errors.append(ErrorInfo(
                            file_path=str(file_path.relative_to(self.project_root)),
                            error_type="UnreachableCode",
                            error_message=f"Unreachable code after statement on same line at line {line_num}",
                            severity=ErrorSeverity.LOW,
                            category=ErrorCategory.DEAD_CODE,
                            line_number=line_num,
                            context_snippet=line.strip(),
                            suggested_fix="Remove code after return/raise/break statements"
                        ))

        return errors

    def _detect_data_flow_issues(self, file_path: Path, tree: ast.AST, content: str) -> List[ErrorInfo]:
        """Detect data flow issues and variable scope problems"""
        errors = []

        class DataFlowAnalyzer(ast.NodeVisitor):
            def __init__(self):
                self.variable_defs = {}  # scope -> variable -> line_number
                self.variable_uses = {}  # scope -> variable -> [line_numbers]
                self.current_scope = "global"

            def visit_FunctionDef(self, node: ast.FunctionDef):
                old_scope = self.current_scope
                self.current_scope = f"function:{node.name}"

                if self.current_scope not in self.variable_defs:
                    self.variable_defs[self.current_scope] = {}
                if self.current_scope not in self.variable_uses:
                    self.variable_uses[self.current_scope] = {}

                self.generic_visit(node)
                self.current_scope = old_scope

            def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
                self.visit_FunctionDef(node)

            def visit_Name(self, node: ast.Name):
                if isinstance(node.ctx, ast.Store):
                    # Variable assignment
                    self.variable_defs.setdefault(self.current_scope, {})[node.id] = node.lineno
                elif isinstance(node.ctx, ast.Load):
                    # Variable usage
                    if self.current_scope not in self.variable_uses:
                        self.variable_uses[self.current_scope] = {}
                    self.variable_uses[self.current_scope].setdefault(node.id, []).append(node.lineno)

                self.generic_visit(node)

        analyzer = DataFlowAnalyzer()
        analyzer.visit(tree)

        # Check for variable scope issues
        for scope, variables in analyzer.variable_uses.items():
            for var_name, usage_lines in variables.items():
                # Check if variable is used before definition in this scope
                if var_name in analyzer.variable_defs.get(scope, {}):
                    def_line = analyzer.variable_defs[scope][var_name]
                    early_uses = [line for line in usage_lines if line < def_line]

                    if early_uses:
                        errors.append(ErrorInfo(
                            file_path=str(file_path.relative_to(self.project_root)),
                            error_type="VariableUsedBeforeDefinition",
                            error_message=f"Variable '{var_name}' used before definition at line {early_uses[0]}",
                            severity=ErrorSeverity.HIGH,
                            category=ErrorCategory.DATA_FLOW,
                            line_number=early_uses[0],
                            context_snippet=self._get_context_line(content, early_uses[0]),
                            suggested_fix=f"Define variable '{var_name}' before using it"
                        ))

        # Check for potential null/None dereferences
        null_deref_errors = self._detect_null_dereferences(file_path, tree, content)
        errors.extend(null_deref_errors)

        # Check for inconsistent return types
        return_type_errors = self._detect_return_type_inconsistencies(file_path, tree, content)
        errors.extend(return_type_errors)

        return errors

    def _detect_null_dereferences(self, file_path: Path, tree: ast.AST, content: str) -> List[ErrorInfo]:
        """Detect potential null/None dereferences"""
        errors = []

        class NullDerefDetector(ast.NodeVisitor):
            def visit_Attribute(self, node: ast.Attribute):
                # Check if we're accessing an attribute on potentially None value
                if isinstance(node.value, ast.Name):
                    var_name = node.value.id

                    # Look for patterns that suggest None checking is needed
                    for parent in self._get_parents(node):
                        if isinstance(parent, ast.If):
                            # Check if this is inside a None check
                            if self._is_none_check(parent, var_name):
                                return  # It's being checked, so it's okay

                # Flag potential None dereference
                errors.append(ErrorInfo(
                    file_path=str(file_path.relative_to(self.project_root)),
                    error_type="PotentialNoneDereference",
                    error_message=f"Potential None dereference of variable '{node.value.id}' at line {node.lineno}",
                    severity=ErrorSeverity.MEDIUM,
                    category=ErrorCategory.DATA_FLOW,
                    line_number=node.lineno,
                    context_snippet=self._get_context_line(content, node.lineno),
                    suggested_fix=f"Add None check before accessing attribute on '{node.value.id}'"
                ))

                self.generic_visit(node)

            def _get_parents(self, node):
                """Get all parent nodes (requires parent references to be set)"""
                parents = []
                current = node
                while hasattr(current, 'parent'):
                    current = current.parent
                    parents.append(current)
                return parents

            def _is_none_check(self, node: ast.If, var_name: str) -> bool:
                """Check if this is an if statement checking for None"""
                return (isinstance(node.test, ast.Compare) and
                        isinstance(node.test.left, ast.Name) and
                        node.test.left.id == var_name and
                        any(isinstance(op, ast.Is) for op in node.test.ops) and
                        any(isinstance(comp, ast.Constant) and comp.value is None for comp in node.test.comparators))

        # Set parent references
        class ParentSetter(ast.NodeTransformer):
            def visit(self, node):
                for child in ast.iter_child_nodes(node):
                    child.parent = node
                return self.generic_visit(node)

        ParentSetter().visit(tree)

        detector = NullDerefDetector()
        detector.visit(tree)

        return errors

    def _detect_return_type_inconsistencies(self, file_path: Path, tree: ast.AST, content: str) -> List[ErrorInfo]:
        """Detect inconsistent return types in functions"""
        errors = []

        class ReturnAnalyzer(ast.NodeVisitor):
            def __init__(self):
                self.function_returns = {}  # function_name -> [return_types]
                self.current_function = None

            def visit_FunctionDef(self, node: ast.FunctionDef):
                self.current_function = node.name
                self.function_returns[node.name] = []

                self.generic_visit(node)

                # Analyze return types for this function
                return_types = self.function_returns[node.name]
                if len(return_types) > 1:
                    unique_types = set(return_types)
                    if len(unique_types) > 2 or (len(unique_types) == 2 and None not in unique_types):
                        errors.append(ErrorInfo(
                            file_path=str(file_path.relative_to(self.project_root)),
                            error_type="InconsistentReturnType",
                            error_message=f"Function '{node.name}' returns inconsistent types: {unique_types}",
                            severity=ErrorSeverity.MEDIUM,
                            category=ErrorCategory.DATA_FLOW,
                            line_number=node.lineno,
                            context_snippet=self._get_context_line(content, node.lineno),
                            suggested_fix=f"Make function '{node.name}' return consistent types"
                        ))

                self.current_function = None

            def visit_Return(self, node: ast.Return):
                if self.current_function and node.value:
                    return_type = self._infer_type(node.value)
                    self.function_returns[self.current_function].append(return_type)
                elif self.current_function:
                    # Return without value (None)
                    self.function_returns[self.current_function].append(None)

                self.generic_visit(node)

            def _infer_type(self, node: ast.AST) -> str:
                """Infer the type of an AST node"""
                if isinstance(node, ast.Constant):
                    return type(node.value).__name__
                elif isinstance(node, ast.List):
                    return "list"
                elif isinstance(node, ast.Dict):
                    return "dict"
                elif isinstance(node, ast.Tuple):
                    return "tuple"
                elif isinstance(node, ast.Call):
                    return "function_call"
                elif isinstance(node, ast.Name):
                    return "variable"
                else:
                    return "unknown"

        analyzer = ReturnAnalyzer()
        analyzer.visit(tree)

        return errors

    def _detect_resource_leaks(self, file_path: Path, tree: ast.AST, content: str) -> List[ErrorInfo]:
        """Detect potential resource leaks (files, connections, etc.)"""
        errors = []

        class ResourceLeakDetector(ast.NodeVisitor):
            def __init__(self):
                self.open_resources = {}  # line_number -> resource_info
                self.context_managers = []

            def visit_With(self, node: ast.With):
                # This is a context manager - resources are properly managed
                for item in node.items:
                    if isinstance(item.context_expr, ast.Call):
                        func_name = self._get_function_name(item.context_expr)
                        if func_name in ['open', 'file', 'connect', 'cursor']:
                            # Properly managed with context manager
                            pass

                self.context_managers.append(node)
                self.generic_visit(node)
                self.context_managers.pop()

            def visit_Call(self, node: ast.Call):
                func_name = self._get_function_name(node)

                # Check for resource opening without context manager
                if func_name in ['open', 'file']:
                    # Check if this call is part of a 'with' statement
                    if not self._is_in_context_manager(node):
                        errors.append(ErrorInfo(
                            file_path=str(file_path.relative_to(self.project_root)),
                            error_type="PotentialResourceLeak",
                            error_message=f"File opened without context manager at line {node.lineno}",
                            severity=ErrorSeverity.HIGH,
                            category=ErrorCategory.RESOURCE_LEAK,
                            line_number=node.lineno,
                            context_snippet=self._get_context_line(content, node.lineno),
                            suggested_fix="Use 'with' statement or ensure file is properly closed"
                        ))

                # Check for database connections
                elif func_name in ['connect', 'cursor', 'execute']:
                    if not self._is_in_context_manager(node):
                        errors.append(ErrorInfo(
                            file_path=str(file_path.relative_to(self.project_root)),
                            error_type="PotentialResourceLeak",
                            error_message=f"Database resource opened without context manager at line {node.lineno}",
                            severity=ErrorSeverity.HIGH,
                            category=ErrorCategory.RESOURCE_LEAK,
                            line_number=node.lineno,
                            context_snippet=self._get_context_line(content, node.lineno),
                            suggested_fix="Use context manager or ensure resource is properly closed"
                        ))

                self.generic_visit(node)

            def _get_function_name(self, node: ast.Call) -> Optional[str]:
                """Extract function name from call node"""
                if isinstance(node.func, ast.Name):
                    return node.func.id
                elif isinstance(node.func, ast.Attribute):
                    return node.func.attr
                return None

            def _is_in_context_manager(self, node) -> bool:
                """Check if node is within a 'with' statement"""
                current = node
                while hasattr(current, 'parent'):
                    current = current.parent
                    if isinstance(current, ast.With):
                        return True
                return False

        # Set parent references
        class ParentSetter(ast.NodeTransformer):
            def visit(self, node):
                for child in ast.iter_child_nodes(node):
                    child.parent = node
                return self.generic_visit(node)

        ParentSetter().visit(tree)

        detector = ResourceLeakDetector()
        detector.visit(tree)

        return errors

    def _detect_race_conditions(self, file_path: Path, tree: ast.AST, content: str) -> List[ErrorInfo]:
        """Detect potential race conditions and threading issues"""
        errors = []

        # Pattern-based detection for common race condition patterns
        lines = content.split('\n')

        # Look for threading-related imports and patterns
        has_threading = False
        for line_num, line in enumerate(lines, 1):
            if any(keyword in line for keyword in ['import threading', 'from threading', 'import asyncio', 'from asyncio', 'import multiprocessing']):
                has_threading = True
                break

        if has_threading:
            race_errors = self._analyze_threading_patterns(file_path, content, lines)
            errors.extend(race_errors)

        return errors

    def _analyze_threading_patterns(self, file_path: Path, content: str, lines: List[str]) -> List[ErrorInfo]:
        """Analyze threading patterns for race conditions"""
        errors = []

        class ThreadingPatternDetector(ast.NodeVisitor):
            def __init__(self):
                self.global_variables = set()
                self.shared_state_access = []

            def visit_Global(self, node: ast.Global):
                for name in node.names:
                    self.global_variables.add(name)
                self.generic_visit(node)

            def visit_FunctionDef(self, node: ast.FunctionDef):
                # Check if function modifies global state
                has_global_access = False
                for child in ast.walk(node):
                    if isinstance(child, ast.Global):
                        has_global_access = True
                        break
                    elif isinstance(child, ast.Name) and child.id in self.global_variables:
                        if isinstance(child.ctx, ast.Store):
                            has_global_access = True
                            break

                if has_global_access:
                    # Check if function might be called from multiple threads
                    if self._is_potentially_threaded_function(node):
                        errors.append(ErrorInfo(
                            file_path=str(file_path.relative_to(self.project_root)),
                            error_type="PotentialRaceCondition",
                            error_message=f"Function '{node.name}' modifies global state without synchronization at line {node.lineno}",
                            severity=ErrorSeverity.HIGH,
                            category=ErrorCategory.RACE_CONDITION,
                            line_number=node.lineno,
                            context_snippet=self._get_context_line(content, node.lineno),
                            suggested_fix=f"Use threading.Lock() or other synchronization for function '{node.name}'"
                        ))

                self.generic_visit(node)

            def _is_potentially_threaded_function(self, node: ast.FunctionDef) -> bool:
                """Check if function might be called from multiple threads"""
                # Look for patterns suggesting this is a threaded function
                function_names = ['run', 'start', 'worker', 'thread', 'task', 'process']
                return any(name in node.name.lower() for name in function_names)

        try:
            tree = ast.parse(content)
            detector = ThreadingPatternDetector()
            detector.visit(tree)
        except SyntaxError:
            pass

        # Pattern-based detection in source code
        for line_num, line in enumerate(lines, 1):
            line_stripped = line.strip()

            # Check for shared state access patterns
            if ('global ' in line_stripped and
                any(keyword in line_stripped for keyword in ['+=', '-=', '*=', '/=', '='])):

                errors.append(ErrorInfo(
                    file_path=str(file_path.relative_to(self.project_root)),
                    error_type="PotentialRaceCondition",
                    error_message=f"Global variable modification without synchronization at line {line_num}",
                    severity=ErrorSeverity.HIGH,
                    category=ErrorCategory.RACE_CONDITION,
                    line_number=line_num,
                    context_snippet=line.strip(),
                    suggested_fix="Use threading.Lock() or atomic operations for global variable access"
                ))

        return errors

    def _detect_logical_anti_patterns(self, file_path: Path, tree: ast.AST, content: str) -> List[ErrorInfo]:
        """Detect advanced logical anti-patterns"""
        errors = []

        # Pattern-based detection
        anti_patterns = [
            # (pattern, description, severity, fix_suggestion)
            (r'if\s+True\s*:', "Always-true condition", ErrorSeverity.MEDIUM, "Remove unnecessary condition or fix logic"),
            (r'if\s+False\s*:', "Always-false condition", ErrorSeverity.MEDIUM, "Remove dead code or fix condition"),
            (r'except\s*:', "Bare exception handler", ErrorSeverity.HIGH, "Catch specific exceptions"),
            (r'except\s+Exception\s*:', "Overly broad exception handler", ErrorSeverity.MEDIUM, "Catch more specific exceptions"),
            (r'assert\s+.*[=!]=.*False', "Inverted assertion", ErrorSeverity.LOW, "Simplify assertion logic"),
            (r'if\s+.*\s+==\s+True\s*:', "Unnecessary comparison with True", ErrorSeverity.LOW, "Remove '== True' comparison"),
            (r'if\s+.*\s+==\s+False\s*:', "Unnecessary comparison with False", ErrorSeverity.LOW, "Use 'not' operator or 'is False'"),
            (r'while\s+True\s*:', "Potentially infinite loop", ErrorSeverity.MEDIUM, "Add break condition or timeout"),
            (r'for\s+.*\s+in\s+range\(.*\)\s*:', "Loop without break condition", ErrorSeverity.LOW, "Verify loop termination"),
        ]

        lines = content.split('\n')
        for line_num, line in enumerate(lines, 1):
            line_stripped = line.strip()

            # Skip comments and empty lines
            if line_stripped.startswith('#') or not line_stripped:
                continue

            for pattern, description, severity, fix_suggestion in anti_patterns:
                if re.search(pattern, line_stripped):
                    errors.append(ErrorInfo(
                        file_path=str(file_path.relative_to(self.project_root)),
                        error_type="LogicalAntiPattern",
                        error_message=f"{description} at line {line_num}: {line[:80]}...",
                        severity=severity,
                        category=ErrorCategory.LOGICAL,
                        line_number=line_num,
                        context_snippet=line.strip(),
                        suggested_fix=fix_suggestion
                    ))

        # AST-based detection
        ast_errors = self._detect_ast_logical_patterns(file_path, tree, content)
        errors.extend(ast_errors)

        return errors

    def _detect_ast_logical_patterns(self, file_path: Path, tree: ast.AST, content: str) -> List[ErrorInfo]:
        """Detect logical patterns using AST analysis"""
        errors = []

        class LogicalPatternDetector(ast.NodeVisitor):
            def visit_Compare(self, node: ast.Compare):
                # Check for problematic comparison chains
                if len(node.ops) > 1:
                    for i, op in enumerate(node.ops):
                        if isinstance(op, (ast.Eq, ast.NotEq)):
                            # Chaining equality comparisons can be problematic
                            if i < len(node.ops) - 1:
                                errors.append(ErrorInfo(
                                    file_path=str(file_path.relative_to(self.project_root)),
                                    error_type="ComparisonChainIssue",
                                    error_message=f"Problematic comparison chain at line {node.lineno}",
                                    severity=ErrorSeverity.LOW,
                                    category=ErrorCategory.LOGICAL,
                                    line_number=node.lineno,
                                    context_snippet=self._get_context_line(content, node.lineno),
                                    suggested_fix="Use explicit logical operators for clarity"
                                ))

                self.generic_visit(node)

            def visit_Try(self, node: ast.Try):
                # Check for empty except blocks
                for handler in node.handlers:
                    if not handler.body or (len(handler.body) == 1 and
                                          isinstance(handler.body[0], ast.Pass)):
                        errors.append(ErrorInfo(
                            file_path=str(file_path.relative_to(self.project_root)),
                            error_type="EmptyExceptBlock",
                            error_message=f"Empty exception handler at line {node.lineno}",
                            severity=ErrorSeverity.MEDIUM,
                            category=ErrorCategory.LOGICAL,
                            line_number=handler.lineno,
                            context_snippet=self._get_context_line(content, handler.lineno),
                            suggested_fix="Add proper error handling or remove the try-except block"
                        ))

                self.generic_visit(node)

        try:
            detector = LogicalPatternDetector()
            detector.visit(tree)
        except Exception:
            pass

        return errors

    def _get_context_line(self, content: str, line_num: int, context_lines: int = 3) -> str:
        """Get context lines around an error"""
        try:
            lines = content.split('\n')

            start = max(0, line_num - context_lines - 1)
            end = min(len(lines), line_num + context_lines)

            context = []
            for i in range(start, end):
                marker = ">>> " if i == line_num - 1 else "    "
                context.append(f"{marker}{lines[i].rstrip()}")

            return '\n'.join(context)
        except Exception:
            return "Context not available"


def main():
    """Main function for logical error detection"""
    import argparse

    parser = argparse.ArgumentParser(description="Advanced logical error detection")
    parser.add_argument("--project-root", default=".", help="Root directory of the project")
    parser.add_argument("--file", help="Specific file to analyze")
    parser.add_argument("--output", help="Output file for results")

    args = parser.parse_args()

    detector = LogicalErrorDetector(args.project_root)

    if args.file:
        file_path = Path(args.file)
        if file_path.exists():
            errors = detector.detect_logical_errors(file_path)
            print(f"Found {len(errors)} logical errors in {args.file}")
            for error in errors:
                print(f"  {error.error_type}: {error.error_message}")
        else:
            print(f"File not found: {args.file}")
    else:
        print("Please specify a file with --file")

    return []


if __name__ == "__main__":
    main()