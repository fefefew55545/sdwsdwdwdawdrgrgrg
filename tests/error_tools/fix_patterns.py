#!/usr/bin/env python3
"""
Comprehensive Fix Pattern Library for BSEE Codebase
Advanced AST-based fixes, context-aware transformations, and multi-step coordinated fixes
"""

import os
import sys
import ast
import re
import json
import difflib
from pathlib import Path
from typing import List, Dict, Any, Optional, Set, Tuple, Union, Callable
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
from collections import defaultdict

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


class FixType(Enum):
    """Types of fixes"""
    TEXT_REPLACEMENT = "TEXT_REPLACEMENT"      # Simple text replacement
    AST_TRANSFORMATION = "AST_TRANSFORMATION"   # AST-based transformation
    MULTI_STEP = "MULTI_STEP"                 # Multi-step coordinated fixes
    CONTEXT_AWARE = "CONTEXT_AWARE"           # Context-aware intelligent fixes
    PATTERN_BASED = "PATTERN_BASED"           # Pattern-based fixes


@dataclass
class FixResult:
    """Result of applying a fix"""
    success: bool
    file_path: str
    original_code: str
    fixed_code: str
    changes_made: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    rollback_data: Optional[str] = None
    verification_needed: bool = False


@dataclass
class FixPattern:
    """Represents a fix pattern"""
    pattern_id: str
    name: str
    description: str
    error_types: Set[str]
    categories: Set[ErrorCategory]
    fix_type: FixType
    confidence: float
    priority: int
    fix_function: Callable[[ErrorInfo, str, Optional[Dict]], FixResult]
    verification_function: Optional[Callable[[str, ErrorInfo], bool]] = None
    dependencies: List[str] = field(default_factory=list)
    prerequisites: List[str] = field(default_factory=list)
    rollback_supported: bool = True


class ContextAwareFixEngine:
    """Advanced context-aware fix engine with AST transformations"""

    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.fix_patterns: Dict[str, FixPattern] = {}
        self.fix_history: List[Dict[str, Any]] = []
        self.rollback_stack: List[Dict[str, Any]] = []
        self._initialize_fix_patterns()

    def _initialize_fix_patterns(self):
        """Initialize all fix patterns"""
        # Import fixes
        self._register_import_fixes()

        # Syntax fixes
        self._register_syntax_fixes()

        # Logic fixes
        self._register_logic_fixes()

        # Resource management fixes
        self._register_resource_fixes()

        # Security fixes
        self._register_security_fixes()

        # Performance fixes
        self._register_performance_fixes()

        # Style fixes
        self._register_style_fixes()

    def apply_fix(self, error: ErrorInfo, file_content: str, context: Optional[Dict] = None) -> FixResult:
        """Apply appropriate fix for an error"""
        if context is None:
            context = {}

        # Find matching fix patterns
        matching_patterns = self._find_matching_patterns(error)

        if not matching_patterns:
            return FixResult(
                success=False,
                file_path=error.file_path,
                original_code=file_content,
                fixed_code=file_content,
                warnings=[f"No fix pattern found for error type: {error.error_type}"]
            )

        # Try patterns in order of priority and confidence
        for pattern in sorted(matching_patterns, key=lambda p: (p.priority, p.confidence), reverse=True):
            try:
                # Check prerequisites
                if not self._check_prerequisites(pattern, context):
                    continue

                # Apply fix
                fix_result = pattern.fix_function(error, file_content, context)

                if fix_result.success:
                    # Store fix in history
                    self._record_fix(pattern, error, fix_result)

                    # Add to rollback stack if supported
                    if pattern.rollback_supported and fix_result.rollback_data:
                        self.rollback_stack.append({
                            'file_path': error.file_path,
                            'rollback_data': fix_result.rollback_data,
                            'pattern_id': pattern.pattern_id,
                            'timestamp': datetime.now().isoformat()
                        })

                    return fix_result

            except Exception as e:
                # Log error and continue with next pattern
                print(f"Error applying fix pattern {pattern.pattern_id}: {str(e)}")
                continue

        return FixResult(
            success=False,
            file_path=error.file_path,
            original_code=file_content,
            fixed_code=file_content,
            warnings=[f"All applicable fix patterns failed for error: {error.error_type}"]
        )

    def _find_matching_patterns(self, error: ErrorInfo) -> List[FixPattern]:
        """Find fix patterns that match the error"""
        matching_patterns = []

        for pattern in self.fix_patterns.values():
            if self._pattern_matches_error(pattern, error):
                matching_patterns.append(pattern)

        return matching_patterns

    def _pattern_matches_error(self, pattern: FixPattern, error: ErrorInfo) -> bool:
        """Check if a pattern matches an error"""
        # Check error type
        if pattern.error_types and error.error_type not in pattern.error_types:
            return False

        # Check category
        if pattern.categories and error.category not in pattern.categories:
            return False

        return True

    def _check_prerequisites(self, pattern: FixPattern, context: Dict) -> bool:
        """Check if pattern prerequisites are met"""
        for prereq in pattern.prerequisites:
            if prereq not in context or not context[prereq]:
                return False
        return True

    def _record_fix(self, pattern: FixPattern, error: ErrorInfo, result: FixResult):
        """Record applied fix in history"""
        self.fix_history.append({
            'pattern_id': pattern.pattern_id,
            'pattern_name': pattern.name,
            'error_type': error.error_type,
            'file_path': error.file_path,
            'timestamp': datetime.now().isoformat(),
            'success': result.success,
            'changes_made': result.changes_made,
            'warnings': result.warnings
        })

    def rollback_last_fix(self) -> bool:
        """Rollback the last applied fix"""
        if not self.rollback_stack:
            return False

        rollback_info = self.rollback_stack.pop()

        try:
            file_path = rollback_info['file_path']
            rollback_data = rollback_info['rollback_data']

            # Restore original content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(rollback_data)

            print(f"Rolled back fix for {file_path}")
            return True

        except Exception as e:
            print(f"Error during rollback: {str(e)}")
            return False

    def _register_import_fixes(self):
        """Register import-related fix patterns"""

        def fix_unused_import(error: ErrorInfo, file_content: str, context: Dict) -> FixResult:
            """Fix unused imports"""
            import_name = error.error_message.split("'")[1] if "'" in error.error_message else None

            if not import_name:
                return FixResult(
                    success=False,
                    file_path=error.file_path,
                    original_code=file_content,
                    fixed_code=file_content,
                    warnings=["Could not extract import name from error message"]
                )

            # Parse AST to find and remove unused import
            try:
                tree = ast.parse(file_content)
                remover = UnusedImportRemover(import_name)
                new_tree = remover.visit(tree)
                new_tree = ast.fix_missing_locations(new_tree)

                fixed_code = ast.unparse(new_tree)

                return FixResult(
                    success=True,
                    file_path=error.file_path,
                    original_code=file_content,
                    fixed_code=fixed_code,
                    changes_made=[f"Removed unused import: {import_name}"],
                    rollback_data=file_content
                )

            except Exception as e:
                # Fallback to text-based removal
                lines = file_content.split('\n')
                new_lines = []
                for line in lines:
                    if import_name in line and ('import' in line or 'from' in line):
                        # Simple check - might be too aggressive
                        new_lines.append(f"# Removed unused import: {line}")
                    else:
                        new_lines.append(line)

                fixed_code = '\n'.join(new_lines)

                return FixResult(
                    success=True,
                    file_path=error.file_path,
                    original_code=file_content,
                    fixed_code=fixed_code,
                    changes_made=[f"Removed unused import (text-based): {import_name}"],
                    warnings=["Used text-based removal - manual review recommended"],
                    rollback_data=file_content
                )

        def fix_missing_dependency(error: ErrorInfo, file_content: str, context: Dict) -> FixResult:
            """Suggest fixes for missing dependencies"""
            # This is more of a suggestion than an automatic fix
            module_match = re.search(r"No module named '([^']+)'", error.error_message)
            if module_match:
                module_name = module_match.group(1)

                # Add import suggestion as comment
                suggestion = f"# TODO: Install missing dependency: pip install {module_name}"
                fixed_code = f"{suggestion}\n{file_content}"

                return FixResult(
                    success=True,
                    file_path=error.file_path,
                    original_code=file_content,
                    fixed_code=fixed_code,
                    changes_made=[f"Added comment about missing dependency: {module_name}"],
                    verification_needed=True,
                    rollback_data=file_content
                )

            return FixResult(
                success=False,
                file_path=error.file_path,
                original_code=file_content,
                fixed_code=file_content,
                warnings=["Could not determine missing dependency"]
            )

        # Register patterns
        self.fix_patterns['unused_import'] = FixPattern(
            pattern_id='unused_import',
            name='Remove Unused Import',
            description='Remove unused import statements',
            error_types={'UnusedImport'},
            categories={ErrorCategory.DEAD_CODE},
            fix_type=FixType.AST_TRANSFORMATION,
            confidence=0.9,
            priority=3,
            fix_function=fix_unused_import
        )

        self.fix_patterns['missing_dependency'] = FixPattern(
            pattern_id='missing_dependency',
            name='Fix Missing Dependency',
            description='Add comment or suggest fix for missing dependency',
            error_types={'MissingDependency', 'ImportError'},
            categories={ErrorCategory.IMPORT},
            fix_type=FixType.TEXT_REPLACEMENT,
            confidence=0.7,
            priority=2,
            fix_function=fix_missing_dependency,
            verification_needed=True
        )

    def _register_syntax_fixes(self):
        """Register syntax-related fix patterns"""

        def fix_pydantic_regex(error: ErrorInfo, file_content: str, context: Dict) -> FixResult:
            """Fix Pydantic regex -> pattern migration"""
            if 'regex=' in file_content and 'pattern=' not in file_content:
                fixed_code = file_content.replace('regex=', 'pattern=')

                return FixResult(
                    success=True,
                    file_path=error.file_path,
                    original_code=file_content,
                    fixed_code=fixed_code,
                    changes_made=['Changed regex= to pattern= for Pydantic v2 compatibility'],
                    rollback_data=file_content
                )

            return FixResult(
                success=False,
                file_path=error.file_path,
                original_code=file_content,
                fixed_code=file_content,
                warnings=['No regex= patterns found or pattern= already present']
            )

        def fix_pydantic_validator(error: ErrorInfo, file_content: str, context: Dict) -> FixResult:
            """Fix Pydantic validator -> field_validator migration"""
            if '@validator(' in file_content and '@field_validator(' not in file_content:
                fixed_code = file_content.replace('@validator(', '@field_validator(')

                return FixResult(
                    success=True,
                    file_path=error.file_path,
                    original_code=file_content,
                    fixed_code=fixed_code,
                    changes_made=['Changed @validator to @field_validator for Pydantic v2 compatibility'],
                    rollback_data=file_content
                )

            return FixResult(
                success=False,
                file_path=error.file_path,
                original_code=file_content,
                fixed_code=file_content,
                warnings=['No @validator decorators found or @field_validator already present']
            )

        # Register patterns
        self.fix_patterns['pydantic_regex'] = FixPattern(
            pattern_id='pydantic_regex',
            name='Fix Pydantic Regex to Pattern',
            description='Change regex= to pattern= for Pydantic v2 compatibility',
            error_types={},
            categories={ErrorCategory.COMPATIBILITY},
            fix_type=FixType.TEXT_REPLACEMENT,
            confidence=0.95,
            priority=4,
            fix_function=fix_pydantic_regex
        )

        self.fix_patterns['pydantic_validator'] = FixPattern(
            pattern_id='pydantic_validator',
            name='Fix Pydantic Validator to Field Validator',
            description='Change @validator to @field_validator for Pydantic v2 compatibility',
            error_types={},
            categories={ErrorCategory.COMPATIBILITY},
            fix_type=FixType.TEXT_REPLACEMENT,
            confidence=0.95,
            priority=4,
            fix_function=fix_pydantic_validator
        )

    def _register_logic_fixes(self):
        """Register logic-related fix patterns"""

        def fix_always_true_condition(error: ErrorInfo, file_content: str, context: Dict) -> FixResult:
            """Fix always-true conditions"""
            # Replace "if True:" with proper condition placeholder
            lines = file_content.split('\n')
            new_lines = []
            changes_made = []

            for line_num, line in enumerate(lines, 1):
                if 'if True:' in line and line_num == error.line_number:
                    new_line = line.replace('if True:', 'if condition:  # TODO: Replace with actual condition')
                    new_lines.append(new_line)
                    changes_made.append(f"Line {line_num}: Replaced 'if True:' with placeholder condition")
                else:
                    new_lines.append(line)

            fixed_code = '\n'.join(new_lines)

            return FixResult(
                success=True,
                file_path=error.file_path,
                original_code=file_content,
                fixed_code=fixed_code,
                changes_made=changes_made,
                rollback_data=file_content,
                verification_needed=True
            )

        def fix_always_false_condition(error: ErrorInfo, file_content: str, context: Dict) -> FixResult:
            """Fix always-false conditions"""
            # Comment out if False: blocks
            lines = file_content.split('\n')
            new_lines = []
            changes_made = []
            in_false_block = False
            indent_level = 0

            for line_num, line in enumerate(lines, 1):
                stripped = line.strip()

                if 'if False:' in stripped and line_num == error.line_number:
                    new_lines.append(f'# {line}  # Unreachable code - review logic')
                    changes_made.append(f"Line {line_num}: Commented out unreachable if False: block")
                    in_false_block = True
                    indent_level = len(line) - len(line.lstrip())
                elif in_false_block and len(line) - len(line.lstrip()) > indent_level:
                    # Still inside the if False block
                    new_lines.append(f'# {line}')
                else:
                    new_lines.append(line)
                    if in_false_block:
                        in_false_block = False

            fixed_code = '\n'.join(new_lines)

            return FixResult(
                success=True,
                file_path=error.file_path,
                original_code=file_content,
                fixed_code=fixed_code,
                changes_made=changes_made,
                rollback_data=file_content,
                verification_needed=True
            )

        def fix_unused_variable(error: ErrorInfo, file_content: str, context: Dict) -> FixResult:
            """Fix unused variables"""
            if error.line_number:
                lines = file_content.split('\n')
                if 1 <= error.line_number <= len(lines):
                    line = lines[error.line_number - 1].strip()
                    if '=' in line and not line.startswith('return') and not line.startswith('def'):

                        # Check if it's a simple assignment
                        var_match = re.match(r'(\w+)\s*=\s*(.+)', line)
                        if var_match:
                            var_name = var_match.group(1)

                            # Don't modify variables that start with underscore (intentionally unused)
                            if not var_name.startswith('_'):
                                # Comment out the assignment
                                commented_line = f"# Removed unused variable: {line}"
                                lines[error.line_number - 1] = commented_line

                                fixed_code = '\n'.join(lines)

                                return FixResult(
                                    success=True,
                                    file_path=error.file_path,
                                    original_code=file_content,
                                    fixed_code=fixed_code,
                                    changes_made=[f"Line {error.line_number}: Removed unused variable '{var_name}'"],
                                    rollback_data=file_content
                                )

            return FixResult(
                success=False,
                file_path=error.file_path,
                original_code=file_content,
                fixed_code=file_content,
                warnings=["Could not safely remove unused variable"]
            )

        # Register patterns
        self.fix_patterns['always_true_condition'] = FixPattern(
            pattern_id='always_true_condition',
            name='Fix Always True Condition',
            description='Replace if True: with proper condition placeholder',
            error_types={'LogicalAntiPattern'},
            categories={ErrorCategory.LOGICAL},
            fix_type=FixType.TEXT_REPLACEMENT,
            confidence=0.8,
            priority=2,
            fix_function=fix_always_true_condition,
            verification_needed=True
        )

        self.fix_patterns['always_false_condition'] = FixPattern(
            pattern_id='always_false_condition',
            name='Fix Always False Condition',
            description='Comment out unreachable if False: blocks',
            error_types={'LogicalAntiPattern'},
            categories={ErrorCategory.LOGICAL},
            fix_type=FixType.TEXT_REPLACEMENT,
            confidence=0.9,
            priority=3,
            fix_function=fix_always_false_condition,
            verification_needed=True
        )

        self.fix_patterns['unused_variable'] = FixPattern(
            pattern_id='unused_variable',
            name='Remove Unused Variable',
            description='Remove or comment out unused variable assignments',
            error_types={'UnusedVariable'},
            categories={ErrorCategory.DEAD_CODE},
            fix_type=FixType.TEXT_REPLACEMENT,
            confidence=0.7,
            priority=1,
            fix_function=fix_unused_variable
        )

    def _register_resource_fixes(self):
        """Register resource management fix patterns"""

        def fix_file_without_context_manager(error: ErrorInfo, file_content: str, context: Dict) -> FixResult:
            """Wrap file operations in context managers"""
            # Pattern to find: variable = open(filename, mode)
            pattern = r'(\w+)\s*=\s*open\s*\(\s*([^)]+)\s*\)'

            def replace_with_context(match):
                var_name = match.group(1)
                open_args = match.group(2)
                return f"with open({open_args}) as {var_name}:"

            fixed_code = re.sub(pattern, replace_with_context, file_content)

            if fixed_code != file_content:
                return FixResult(
                    success=True,
                    file_path=error.file_path,
                    original_code=file_content,
                    fixed_code=fixed_code,
                    changes_made=['Wrapped file opening in context manager'],
                    rollback_data=file_content,
                    verification_needed=True
                )

            return FixResult(
                success=False,
                file_path=error.file_path,
                original_code=file_content,
                fixed_code=file_content,
                warnings=['No file operations found to wrap in context manager']
            )

        # Register pattern
        self.fix_patterns['file_context_manager'] = FixPattern(
            pattern_id='file_context_manager',
            name='Add File Context Manager',
            description='Wrap file operations in with statements',
            error_types={'PotentialResourceLeak'},
            categories={ErrorCategory.RESOURCE_LEAK},
            fix_type=FixType.PATTERN_BASED,
            confidence=0.6,
            priority=3,
            fix_function=fix_file_without_context_manager,
            verification_needed=True
        )

    def _register_security_fixes(self):
        """Register security-related fix patterns"""

        def fix_bare_except(error: ErrorInfo, file_content: str, context: Dict) -> FixResult:
            """Fix bare except handlers"""
            lines = file_content.split('\n')
            new_lines = []
            changes_made = []

            for line_num, line in enumerate(lines, 1):
                stripped = line.strip()
                if stripped == 'except:' or stripped == 'except :':
                    # Replace with specific exception suggestion
                    indent = line[:len(line) - len(line.lstrip())]
                    new_line = f"{indent}except Exception as e:  # TODO: Catch more specific exceptions"
                    new_lines.append(new_line)
                    changes_made.append(f"Line {line_num}: Replaced bare except with specific exception")
                else:
                    new_lines.append(line)

            fixed_code = '\n'.join(new_lines)

            return FixResult(
                success=True,
                file_path=error.file_path,
                original_code=file_content,
                fixed_code=fixed_code,
                changes_made=changes_made,
                rollback_data=file_content,
                verification_needed=True
            )

        # Register pattern
        self.fix_patterns['bare_except'] = FixPattern(
            pattern_id='bare_except',
            name='Fix Bare Except Handler',
            description='Replace bare except with specific exception handling',
            error_types={'LogicalAntiPattern'},
            categories={ErrorCategory.SECURITY},
            fix_type=FixType.TEXT_REPLACEMENT,
            confidence=0.8,
            priority=3,
            fix_function=fix_bare_except,
            verification_needed=True
        )

    def _register_performance_fixes(self):
        """Register performance-related fix patterns"""

        def fix_string_concatenation(error: ErrorInfo, file_content: str, context: Dict) -> FixResult:
            """Fix inefficient string concatenation"""
            # Pattern to find: str1 + str2 + str3...
            pattern = r'(\w+)\s*\+\s*(\w+)\s*\+\s*'

            def replace_with_fstring(match):
                # This is a simplified fix - in practice, you'd need more sophisticated analysis
                return "f'{str1}{str2}'  # TODO: Optimize string concatenation"

            fixed_code = re.sub(pattern, replace_with_fstring, file_content)

            if fixed_code != file_content:
                return FixResult(
                    success=True,
                    file_path=error.file_path,
                    original_code=file_content,
                    fixed_code=fixed_code,
                    changes_made=['Suggested optimization for string concatenation'],
                    rollback_data=file_content,
                    verification_needed=True
                )

            return FixResult(
                success=False,
                file_path=error.file_path,
                original_code=file_content,
                fixed_code=file_content,
                warnings=['No string concatenation patterns found']
            )

        # Register pattern
        self.fix_patterns['string_concatenation'] = FixPattern(
            pattern_id='string_concatenation',
            name='Optimize String Concatenation',
            description='Suggest optimization for string concatenation',
            error_types={'PerformanceIssue'},
            categories={ErrorCategory.PERFORMANCE},
            fix_type=FixType.PATTERN_BASED,
            confidence=0.5,
            priority=1,
            fix_function=fix_string_concatenation,
            verification_needed=True
        )

    def _register_style_fixes(self):
        """Register style-related fix patterns"""

        def fix_line_length(error: ErrorInfo, file_content: str, context: Dict) -> FixResult:
            """Fix overly long lines"""
            lines = file_content.split('\n')
            new_lines = []
            changes_made = []

            for line_num, line in enumerate(lines, 1):
                if len(line) > 120:  # PEP 8 recommends 79, but we'll use 120 for practicality
                    # Split line at reasonable points
                    split_line = self._split_long_line(line)
                    if split_line != line:
                        new_lines.extend(split_line)
                        changes_made.append(f"Line {line_num}: Split long line ({len(line)} chars)")
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)

            fixed_code = '\n'.join(new_lines)

            return FixResult(
                success=True,
                file_path=error.file_path,
                original_code=file_content,
                fixed_code=fixed_code,
                changes_made=changes_made,
                rollback_data=file_content
            )

        # Register pattern
        self.fix_patterns['line_length'] = FixPattern(
            pattern_id='line_length',
            name='Fix Long Lines',
            description='Split lines that exceed maximum length',
            error_types={'StyleIssue'},
            categories={ErrorCategory.MAINTAINABILITY},
            fix_type=FixType.TEXT_REPLACEMENT,
            confidence=0.7,
            priority=1,
            fix_function=fix_line_length
        )

    def _split_long_line(self, line: str) -> List[str]:
        """Split a long line at appropriate points"""
        # Simple split at common break points
        break_points = [' + ', ', ', ' and ', ' or ', ' in ']

        for break_point in break_points:
            if break_point in line and len(line) > 120:
                parts = line.split(break_point)
                if len(parts) == 2:
                    indent = ' ' * (len(line) - len(line.lstrip())) + '  '
                    return [parts[0] + break_point, indent + parts[1]]

        # If no good break point, just return the original line
        return [line]

    def export_fix_patterns(self, output_path: str = None) -> str:
        """Export fix patterns to JSON"""
        if output_path is None:
            output_path = f"/tmp/fix_patterns_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        patterns_data = {
            'timestamp': datetime.now().isoformat(),
            'total_patterns': len(self.fix_patterns),
            'patterns': []
        }

        for pattern_id, pattern in self.fix_patterns.items():
            pattern_dict = {
                'pattern_id': pattern.pattern_id,
                'name': pattern.name,
                'description': pattern.description,
                'error_types': list(pattern.error_types),
                'categories': [cat.value for cat in pattern.categories],
                'fix_type': pattern.fix_type.value,
                'confidence': pattern.confidence,
                'priority': pattern.priority,
                'dependencies': pattern.dependencies,
                'prerequisites': pattern.prerequisites,
                'rollback_supported': pattern.rollback_supported
            }
            patterns_data['patterns'].append(pattern_dict)

        with open(output_path, 'w') as f:
            json.dump(patterns_data, f, indent=2)

        print(f"📋 Fix patterns exported to: {output_path}")
        return output_path


class UnusedImportRemover(ast.NodeTransformer):
    """AST transformer to remove unused imports"""

    def __init__(self, import_name: str):
        self.import_name = import_name

    def visit_Import(self, node: ast.Import):
        new_aliases = []
        for alias in node.names:
            if alias.name != self.import_name and (alias.asname or alias.name) != self.import_name:
                new_aliases.append(alias)

        if new_aliases:
            node.names = new_aliases
            return node
        else:
            return None  # Remove the entire import statement

    def visit_ImportFrom(self, node: ast.ImportFrom):
        if node.module == self.import_name:
            return None  # Remove the entire from import

        new_names = []
        for alias in node.names:
            if alias.name != self.import_name and (alias.asname or alias.name) != self.import_name:
                new_names.append(alias)

        if new_names:
            node.names = new_names
            return node
        elif node.module:  # Only remove if we have names to remove
            return None  # Remove the entire from import
        else:
            return node


def main():
    """Main function for fix patterns"""
    import argparse

    parser = argparse.ArgumentParser(description="Fix pattern application")
    parser.add_argument("--project-root", default=".", help="Root directory of the project")
    parser.add_argument("--export-patterns", action="store_true", help="Export fix patterns")
    parser.add_argument("--output", help="Output file for results")

    args = parser.parse_args()

    fix_engine = ContextAwareFixEngine(args.project_root)

    if args.export_patterns:
        fix_engine.export_fix_patterns(args.output)
    else:
        print("Use --export-patterns to export available fix patterns")

    return []


if __name__ == "__main__":
    main()