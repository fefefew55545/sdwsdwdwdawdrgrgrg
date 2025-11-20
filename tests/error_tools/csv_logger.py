#!/usr/bin/env python3
"""
Enhanced CSV Error Reporting Tool for BSEE Codebase
Generates CSV reports with file errors, correlation tracking, and fix status tracking
"""

import csv
import os
import re
import hashlib
import statistics
from pathlib import Path
from typing import List, Dict, Any, Optional, Set, Tuple
from datetime import datetime
from collections import defaultdict


class CSVLogger:
    """Enhanced CSV logger for error reporting, fix tracking, and correlation analysis"""

    def __init__(self, project_root: str = ".", csv_path: str = "tests/error_report.csv"):
        self.project_root = Path(project_root).resolve()
        self.csv_path = Path(csv_path)
        self.fieldnames = [
            'file_path',
            'error_type',
            'error_message',
            'error_status',
            'fix_description',
            'timestamp',
            'fix_timestamp',
            'verified_by',
            'priority',
            'correlation_id',      # New: Group related errors
            'root_cause',          # New: Underlying cause analysis
            'fix_success_prediction', # New: ML-based success probability
            'manual_review_required',  # New: Complex fix flag
            'combination_context', # New: Which files were tested together
            'load_order',          # New: Module loading sequence
            'performance_impact',  # New: Performance metrics
            'error_category',      # New: Error category classification
            'severity_level',      # New: Severity level
            'test_context',        # New: Testing context
            'dependencies',        # New: Related dependencies
            'cluster_id',          # New: Error cluster identifier
            'pattern_match',       # New: Matched error pattern
            'confidence_score'     # New: Confidence in detection
        ]

    def create_error_report(self, errors: List[Dict[str, Any]],
                          include_correlations: bool = True,
                          include_fixes: bool = True) -> Path:
        """Create a comprehensive CSV error report with enhanced tracking"""

        # Ensure directory exists
        self.csv_path.parent.mkdir(parents=True, exist_ok=True)

        # Process errors and add correlation data
        processed_errors = self._process_errors_with_correlations(errors, include_correlations)

        # Prepare CSV rows
        csv_rows = []
        for error in processed_errors:
            # Basic error information
            row = {
                'file_path': error.get('file_path', ''),
                'error_type': error.get('error_type', ''),
                'error_message': error.get('error_message', ''),
                'error_status': error.get('error_status', 'DETECTED'),
                'fix_description': error.get('fix_description', ''),
                'timestamp': error.get('timestamp', datetime.now().isoformat()),
                'fix_timestamp': error.get('fix_timestamp', ''),
                'verified_by': error.get('verified_by', ''),
                'priority': self._determine_priority(error.get('error_type', '')),
                'error_category': error.get('category', 'UNKNOWN'),
                'severity_level': error.get('severity', 'MEDIUM'),
                'test_context': error.get('test_context', ''),
                'dependencies': ';'.join(error.get('dependencies', [])),
                # Enhanced fields
                'correlation_id': error.get('correlation_id', self._generate_correlation_id(error)),
                'root_cause': error.get('root_cause', ''),
                'fix_success_prediction': error.get('fix_success_prediction', 0.0),
                'manual_review_required': error.get('manual_review_required', 'False'),
                'combination_context': error.get('combination_context', ''),
                'load_order': error.get('load_order', ''),
                'performance_impact': error.get('performance_impact', 'unknown'),
                'cluster_id': error.get('cluster_id', ''),
                'pattern_match': error.get('pattern_match', ''),
                'confidence_score': error.get('confidence_score', 0.0)
            }

            # Add fix suggestions
            if include_fixes:
                fix_suggestion = self._suggest_fix(error)
                if not row['fix_description']:
                    row['fix_description'] = fix_suggestion

                # Predict fix success
                row['fix_success_prediction'] = self._predict_fix_success(error)

            csv_rows.append(row)

        # Write CSV file
        with open(self.csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(csv_rows)

        print(f"Enhanced CSV error report created: {self.csv_path}")
        print(f"Report contains {len(csv_rows)} errors with correlation tracking")

        return self.csv_path

    def _process_errors_with_correlations(self, errors: List[Dict[str, Any]],
                                       include_correlations: bool) -> List[Dict[str, Any]]:
        """Process errors and add correlation analysis"""
        processed_errors = []

        if include_correlations:
            # Find error correlations
            correlations = self._analyze_error_correlations(errors)
            clusters = self._cluster_errors(errors)
            patterns = self._match_error_patterns(errors)

            for error in errors:
                error_data = error.copy()

                # Add correlation data
                error_id = self._generate_error_id(error)
                error_data['correlation_id'] = correlations.get(error_id, self._generate_correlation_id(error))
                error_data['cluster_id'] = clusters.get(error_id, '')
                error_data['pattern_match'] = patterns.get(error_id, '')

                # Determine if manual review is needed
                error_data['manual_review_required'] = self._requires_manual_review(error)
                error_data['root_cause'] = self._determine_root_cause(error)
                error_data['confidence_score'] = self._calculate_confidence_score(error)

                processed_errors.append(error_data)
        else:
            processed_errors = errors

        return processed_errors

    def _analyze_error_correlations(self, errors: List[Dict[str, Any]]) -> Dict[str, str]:
        """Analyze correlations between errors"""
        correlations = {}

        # Group errors by similarity
        error_groups = defaultdict(list)
        for error in errors:
            error_id = self._generate_error_id(error)
            signature = self._create_error_signature(error)
            error_groups[signature].append(error_id)

        # Assign correlation IDs
        for signature, error_ids in error_groups.items():
            if len(error_ids) > 1:  # Only correlate if multiple similar errors
                correlation_id = f"corr_{hashlib.md5(signature.encode()).hexdigest()[:8]}"
                for error_id in error_ids:
                    correlations[error_id] = correlation_id

        return correlations

    def _cluster_errors(self, errors: List[Dict[str, Any]]) -> Dict[str, str]:
        """Cluster related errors"""
        clusters = {}

        # Simple clustering by file and error type
        file_type_groups = defaultdict(list)
        for error in errors:
            error_id = self._generate_error_id(error)
            key = f"{error.get('file_path', '')}_{error.get('error_type', '')}"
            file_type_groups[key].append(error_id)

        # Assign cluster IDs
        for group_key, error_ids in file_type_groups.items():
            if len(error_ids) >= 3:  # Only create clusters for groups of 3+ errors
                cluster_id = f"cluster_{hashlib.md5(group_key.encode()).hexdigest()[:8]}"
                for error_id in error_ids:
                    clusters[error_id] = cluster_id

        return clusters

    def _match_error_patterns(self, errors: List[Dict[str, Any]]) -> Dict[str, str]:
        """Match errors against known patterns"""
        patterns = {}

        for error in errors:
            error_id = self._generate_error_id(error)
            pattern_match = self._find_matching_pattern(error)
            if pattern_match:
                patterns[error_id] = pattern_match

        return patterns

    def _find_matching_pattern(self, error: Dict[str, Any]) -> str:
        """Find matching pattern for an error"""
        error_message = error.get('error_message', '').lower()
        error_type = error.get('error_type', '')

        # Common patterns
        patterns = {
            'import_pattern': ['import', 'module', 'no module named'],
            'syntax_pattern': ['syntax', 'indentation', 'invalid syntax'],
            'resource_pattern': ['file', 'open', 'close', 'resource'],
            'null_pattern': ['none', 'null', 'attribute'],
            'type_pattern': ['type', 'typeerror'],
            'logic_pattern': ['logic', 'condition', 'if true', 'if false']
        }

        for pattern_name, keywords in patterns.items():
            if any(keyword in error_message for keyword in keywords):
                return pattern_name

        return ''

    def _generate_error_id(self, error: Dict[str, Any]) -> str:
        """Generate unique ID for an error"""
        error_str = f"{error.get('file_path', '')}_{error.get('error_type', '')}_{error.get('error_message', '')}"
        return hashlib.md5(error_str.encode()).hexdigest()[:12]

    def _generate_correlation_id(self, error: Dict[str, Any]) -> str:
        """Generate correlation ID for similar errors"""
        signature = self._create_error_signature(error)
        return f"corr_{hashlib.md5(signature.encode()).hexdigest()[:8]}"

    def _create_error_signature(self, error: Dict[str, Any]) -> str:
        """Create a signature for error correlation"""
        # Normalize error message for correlation
        message = error.get('error_message', '').lower()
        message = re.sub(r'\d+', 'N', message)  # Replace numbers
        message = re.sub(r'[\'"][^\'\"]*[\'"]', 'STR', message)  # Replace strings
        message = re.sub(r'\b\w+\.py\b', 'FILE.py', message)  # Replace file names

        return f"{error.get('error_type', '')}_{message}_{error.get('category', '')}"

    def _requires_manual_review(self, error: Dict[str, Any]) -> str:
        """Determine if error requires manual review"""
        error_type = error.get('error_type', '')
        category = error.get('category', '')

        # High-risk categories that require manual review
        manual_review_types = [
            'RuntimeError', 'ImportError', 'CircularDependency',
            'PotentialResourceLeak', 'PotentialRaceCondition'
        ]

        if error_type in manual_review_types:
            return 'True'

        # Complex patterns
        if 'combination_context' in error and error['combination_context']:
            return 'True'

        if 'confidence_score' in error and error['confidence_score'] < 0.7:
            return 'True'

        return 'False'

    def _determine_root_cause(self, error: Dict[str, Any]) -> str:
        """Determine the likely root cause of an error"""
        error_type = error.get('error_type', '')
        error_message = error.get('error_message', '')

        root_cause_map = {
            'ImportError': 'Missing dependencies or incorrect import paths',
            'SyntaxError': 'Code syntax issues or language version incompatibility',
            'RuntimeError': 'Logic errors or runtime environment issues',
            'PotentialResourceLeak': 'Improper resource management',
            'UnusedVariable': 'Code accumulation without cleanup',
            'CircularDependency': 'Dependency cycle in module imports'
        }

        return root_cause_map.get(error_type, 'Requires investigation')

    def _calculate_confidence_score(self, error: Dict[str, Any]) -> float:
        """Calculate confidence score for error detection"""
        score = 0.5  # Base score

        # Increase confidence based on clarity
        error_message = error.get('error_message', '')
        if len(error_message) > 20:
            score += 0.1

        # Increase confidence for known error types
        known_types = ['ImportError', 'SyntaxError', 'TypeError', 'AttributeError']
        if error.get('error_type') in known_types:
            score += 0.2

        # Increase confidence if correlation found
        if error.get('correlation_id'):
            score += 0.1

        # Increase confidence if pattern matched
        if error.get('pattern_match'):
            score += 0.1

        return min(1.0, score)

    def _predict_fix_success(self, error: Dict[str, Any]) -> float:
        """Predict the probability of successful fix"""
        error_type = error.get('error_type', '')
        category = error.get('category', '')

        # Success rates based on historical data
        success_rates = {
            'ImportError': 0.9,
            'SyntaxError': 0.8,
            'UnusedVariable': 0.95,
            'PotentialResourceLeak': 0.7,
            'LogicalAntiPattern': 0.6,
            'RuntimeError': 0.5
        }

        base_rate = success_rates.get(error_type, 0.7)

        # Adjust based on complexity
        if error.get('manual_review_required') == 'True':
            base_rate -= 0.2

        if error.get('combination_context'):
            base_rate -= 0.1

        if error.get('cluster_id'):
            base_rate += 0.1  # Clustered errors often have better fix strategies

        return max(0.1, min(1.0, base_rate))

    def _determine_priority(self, error_type: str) -> str:
        """Determine priority level based on error type"""
        high_priority = ['SyntaxError', 'ImportError', 'ModuleNotFoundError', 'CircularDependency']
        medium_priority = ['AttributeError', 'TypeError', 'RuntimeError', 'PotentialResourceLeak']
        low_priority = ['Warning', 'DeprecationWarning', 'UnusedVariable', 'StyleIssue']

        if error_type in high_priority:
            return 'HIGH'
        elif error_type in medium_priority:
            return 'MEDIUM'
        elif error_type in low_priority:
            return 'LOW'
        else:
            return 'MEDIUM'

    def _suggest_fix(self, error: Dict[str, Any]) -> str:
        """Suggest fixes for common error types"""
        error_type = error.get('error_type', '')
        error_message = error.get('error_message', '')
        file_path = error.get('file_path', '')

        # Enhanced fix suggestions
        fix_suggestions = {
            'ImportError': 'Check if required module is installed and accessible in Python path',
            'ModuleNotFoundError': 'Install missing module: pip install <module_name>',
            'SyntaxError': 'Fix syntax error in the code (check brackets, indentation, etc.)',
            'AttributeError': 'Check if attribute/method exists on the object',
            'TypeError': 'Verify data types match expected types',
            'RuntimeError': 'Debug runtime logic and check input data',
            'PotentialResourceLeak': 'Use context managers (with statements) or ensure proper cleanup',
            'UnusedVariable': 'Remove unused variable or prefix with underscore if intentional',
            'LogicalAntiPattern': 'Review logic for correctness and fix anti-patterns',
            'CircularDependency': 'Refactor module structure to break circular imports'
        }

        base_suggestion = fix_suggestions.get(error_type, 'Review error details and debug the issue')

        # Specific suggestions based on error message content
        if 'No module named' in error_message:
            module_name = self._extract_module_name(error_message)
            if module_name:
                return f"Install missing module: pip install {module_name}"

        elif 'bsee' in error_message.lower() and 'import' in error_message.lower():
            return "Add bsee module to Python path or check project structure"

        return base_suggestion

    def _extract_module_name(self, error_message: str) -> Optional[str]:
        """Extract module name from error message"""
        import re

        # Pattern to match "No module named 'module_name'"
        match = re.search(r"No module named ['\"]([^'\"]+)['\"]", error_message)
        if match:
            return match.group(1)

        return None

    def update_error_status(self, file_path: str, error_type: str,
                          new_status: str, fix_description: str = '',
                          verified_by: str = '',
                          correlation_data: Optional[Dict] = None) -> bool:
        """Update the status of an existing error in the CSV with enhanced tracking"""
        if not self.csv_path.exists():
            print(f"CSV file not found: {self.csv_path}")
            return False

        # Read existing rows
        rows = []
        updated = False

        with open(self.csv_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames
            for row in reader:
                if (row['file_path'] == file_path and
                    row['error_type'] == error_type and
                    row['error_status'] != 'FIXED'):

                    row['error_status'] = new_status
                    row['fix_timestamp'] = datetime.now().isoformat()
                    if fix_description:
                        row['fix_description'] = fix_description
                    if verified_by:
                        row['verified_by'] = verified_by

                    # Update correlation data if provided
                    if correlation_data:
                        for key, value in correlation_data.items():
                            if key in row:
                                row[key] = str(value)

                    updated = True

                rows.append(row)

        if updated:
            # Write back to CSV
            with open(self.csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

            print(f"Updated error status for {file_path}: {error_type} -> {new_status}")
            return True
        else:
            print(f"No matching error found for {file_path}: {error_type}")
            return False

    def get_error_statistics(self) -> Dict[str, Any]:
        """Get enhanced statistics from the CSV report"""
        if not self.csv_path.exists():
            return {"error": "CSV file not found"}

        stats = {
            'total_errors': 0,
            'by_status': {},
            'by_type': {},
            'by_priority': {},
            'by_file': {},
            'by_category': {},
            'by_correlation': {},
            'avg_confidence': 0.0,
            'manual_review_count': 0,
            'fix_success_predictions': {}
        }

        confidence_scores = []

        with open(self.csv_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                stats['total_errors'] += 1

                # Count by status
                status = row.get('error_status', 'UNKNOWN')
                stats['by_status'][status] = stats['by_status'].get(status, 0) + 1

                # Count by type
                error_type = row.get('error_type', 'UNKNOWN')
                stats['by_type'][error_type] = stats['by_type'].get(error_type, 0) + 1

                # Count by priority
                priority = row.get('priority', 'MEDIUM')
                stats['by_priority'][priority] = stats['by_priority'].get(priority, 0) + 1

                # Count by file
                file_path = row.get('file_path', 'UNKNOWN')
                if file_path not in stats['by_file']:
                    stats['by_file'][file_path] = 0
                stats['by_file'][file_path] += 1

                # Count by category
                category = row.get('error_category', 'UNKNOWN')
                stats['by_category'][category] = stats['by_category'].get(category, 0) + 1

                # Count by correlation
                correlation_id = row.get('correlation_id', '')
                if correlation_id:
                    stats['by_correlation'][correlation_id] = stats['by_correlation'].get(correlation_id, 0) + 1

                # Count manual reviews
                if row.get('manual_review_required') == 'True':
                    stats['manual_review_count'] += 1

                # Collect confidence scores
                try:
                    confidence = float(row.get('confidence_score', 0))
                    confidence_scores.append(confidence)
                except ValueError:
                    pass

                # Fix success predictions
                try:
                    success_pred = float(row.get('fix_success_prediction', 0))
                    pred_range = f"{success_pred:.1f}"
                    stats['fix_success_predictions'][pred_range] = stats['fix_success_predictions'].get(pred_range, 0) + 1
                except ValueError:
                    pass

        # Calculate average confidence
        if confidence_scores:
            stats['avg_confidence'] = statistics.mean(confidence_scores)

        return stats

    def generate_correlation_report(self) -> str:
        """Generate a correlation analysis report"""
        stats = self.get_error_statistics()

        if 'error' in stats:
            return f"Error generating correlation report: {stats['error']}"

        report = []
        report.append("=" * 70)
        report.append("ENHANCED ERROR CORRELATION ANALYSIS REPORT")
        report.append("=" * 70)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Total Errors: {stats['total_errors']}")
        report.append(f"Average Confidence: {stats['avg_confidence']:.2f}")
        report.append(f"Manual Reviews Required: {stats['manual_review_count']}")
        report.append("")

        # Correlation analysis
        if stats['by_correlation']:
            report.append("Error Correlations:")
            sorted_correlations = sorted(stats['by_correlation'].items(), key=lambda x: x[1], reverse=True)[:10]
            for corr_id, count in sorted_correlations:
                report.append(f"  {corr_id:20} : {count:4} errors")
            report.append("")

        # Category analysis
        if stats['by_category']:
            report.append("Error Categories:")
            for category, count in sorted(stats['by_category'].items(), key=lambda x: x[1], reverse=True):
                percentage = (count / stats['total_errors']) * 100
                report.append(f"  {category:20} : {count:4} ({percentage:5.1f}%)")
            report.append("")

        # Fix success predictions
        if stats['fix_success_predictions']:
            report.append("Fix Success Predictions:")
            for pred_range, count in sorted(stats['fix_success_predictions'].items()):
                percentage = (count / stats['total_errors']) * 100
                report.append(f"  Success Rate {pred_range:15} : {count:4} ({percentage:5.1f}%)")
            report.append("")

        return "\n".join(report)

    def export_correlation_analysis(self, output_path: str) -> Path:
        """Export detailed correlation analysis"""
        stats = self.get_error_statistics()
        correlation_report = self.generate_correlation_report()

        # Create comprehensive analysis file
        output_path_obj = Path(output_path)
        output_path_obj.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path_obj, 'w', encoding='utf-8') as f:
            f.write(correlation_report)
            f.write("\n\n")

            # Add detailed statistics
            f.write("DETAILED STATISTICS:\n")
            f.write("=" * 50 + "\n")
            f.write(f"Total Errors: {stats['total_errors']}\n")
            f.write(f"Average Confidence Score: {stats['avg_confidence']:.3f}\n")
            f.write(f"Errors Requiring Manual Review: {stats['manual_review_count']}\n")
            f.write(f"Number of Correlation Groups: {len(stats['by_correlation'])}\n")

        print(f"Correlation analysis exported to: {output_path_obj}")
        return output_path_obj


def main():
    """Main function for standalone testing"""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Generate enhanced CSV error reports")
    parser.add_argument("--project-root", default=".", help="Root directory of the project")
    parser.add_argument("--csv-path", default="tests/error_report.csv", help="Path for CSV output")
    parser.add_argument("--input-json", help="Input JSON file with errors")
    parser.add_argument("--statistics", action="store_true", help="Show error statistics")
    parser.add_argument("--correlation-report", action="store_true", help="Generate correlation analysis")
    parser.add_argument("--summary", action="store_true", help="Generate text summary")
    parser.add_argument("--filter-status", help="Filter by status (DETECTED, FIXED, etc.)")
    parser.add_argument("--filter-type", help="Filter by error type")
    parser.add_argument("--filter-priority", help="Filter by priority")
    parser.add_argument("--export-correlation", help="Export correlation analysis to this path")

    args = parser.parse_args()

    logger = CSVLogger(args.project_root, args.csv_path)

    # Load errors from JSON if provided
    errors = []
    if args.input_json:
        with open(args.input_json, 'r') as f:
            errors = json.load(f)

    if errors:
        logger.create_error_report(errors, include_correlations=True)

    # Show statistics if requested
    if args.statistics:
        stats = logger.get_error_statistics()
        print("Enhanced Error Statistics:")
        print(json.dumps(stats, indent=2))

    # Generate correlation report if requested
    if args.correlation_report:
        correlation_report = logger.generate_correlation_report()
        print(correlation_report)

    # Generate summary if requested
    if args.summary:
        summary = logger.generate_summary_report()
        print(summary)

    # Export correlation analysis if requested
    if args.export_correlation:
        logger.export_correlation_analysis(args.export_correlation)


if __name__ == "__main__":
    main()