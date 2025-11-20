#!/usr/bin/env python3
"""
Enhanced Complete Error Analysis Pipeline for BSEE Codebase
Integrates advanced error detection, correlation analysis, pattern recognition, and intelligent fixing
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

# Add error_tools to path
sys.path.insert(0, str(Path(__file__).parent / 'error_tools'))

# Import all enhanced error analysis components
try:
    from advanced_error_detector import AdvancedErrorDetector
    from logical_error_detector import LogicalErrorDetector
    from combination_tester import CombinationTester
    from runtime_analyzer import RuntimeAnalyzer
    from pattern_analyzer import PatternAnalyzer
    from fix_patterns import ContextAwareFixEngine
    from csv_logger import CSVLogger
    from windows_simulator import WindowsSimulator
except ImportError as e:
    print(f"Warning: Could not import some error analysis components: {e}")
    print("Falling back to basic analysis only")


class EnhancedErrorAnalysisPipeline:
    """Enhanced complete error analysis pipeline with all new systems"""

    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Output paths
        self.advanced_error_results_path = f"/tmp/bsee_advanced_errors_{self.timestamp}.json"
        self.logical_error_results_path = f"/tmp/bsee_logical_errors_{self.timestamp}.json"
        self.combination_results_path = f"/tmp/bsee_combination_errors_{self.timestamp}.json"
        self.runtime_results_path = f"/tmp/bsee_runtime_errors_{self.timestamp}.json"
        self.pattern_results_path = f"/tmp/bsee_pattern_analysis_{self.timestamp}.json"
        self.windows_results_path = f"/tmp/bsee_windows_{self.timestamp}.json"
        self.enhanced_csv_path = "tests/enhanced_error_report.csv"
        self.error_logs_dir = self.project_root / "tests" / "error_logs"

        # Ensure error logs directory exists
        self.error_logs_dir.mkdir(parents=True, exist_ok=True)

        # Initialize components
        self.components = {}
        self._initialize_components()

    def _initialize_components(self):
        """Initialize all analysis components"""
        try:
            self.components['advanced_detector'] = AdvancedErrorDetector(str(self.project_root))
            print("✅ Advanced Error Detector initialized")
        except Exception as e:
            print(f"⚠️  Could not initialize Advanced Error Detector: {e}")

        try:
            self.components['logical_detector'] = LogicalErrorDetector(str(self.project_root))
            print("✅ Logical Error Detector initialized")
        except Exception as e:
            print(f"⚠️  Could not initialize Logical Error Detector: {e}")

        try:
            self.components['combination_tester'] = CombinationTester(str(self.project_root))
            print("✅ Combination Tester initialized")
        except Exception as e:
            print(f"⚠️  Could not initialize Combination Tester: {e}")

        try:
            self.components['runtime_analyzer'] = RuntimeAnalyzer(str(self.project_root))
            print("✅ Runtime Analyzer initialized")
        except Exception as e:
            print(f"⚠️  Could not initialize Runtime Analyzer: {e}")

        try:
            self.components['pattern_analyzer'] = PatternAnalyzer(str(self.project_root))
            print("✅ Pattern Analyzer initialized")
        except Exception as e:
            print(f"⚠️  Could not initialize Pattern Analyzer: {e}")

        try:
            self.components['fix_engine'] = ContextAwareFixEngine(str(self.project_root))
            print("✅ Context-Aware Fix Engine initialized")
        except Exception as e:
            print(f"⚠️  Could not initialize Fix Engine: {e}")

        try:
            self.components['csv_logger'] = CSVLogger(str(self.project_root), self.enhanced_csv_path)
            print("✅ Enhanced CSV Logger initialized")
        except Exception as e:
            print(f"⚠️  Could not initialize CSV Logger: {e}")

        try:
            self.components['windows_simulator'] = WindowsSimulator(str(self.project_root))
            print("✅ Windows Simulator initialized")
        except Exception as e:
            print(f"⚠️  Could not initialize Windows Simulator: {e}")

    def run_enhanced_error_analysis(self) -> dict:
        """Run enhanced multi-phase error detection"""
        print("=" * 80)
        print("PHASE 1: Enhanced Multi-Phase Error Detection")
        print("=" * 80)

        all_errors = []

        # Advanced error detection
        if 'advanced_detector' in self.components:
            print("🚀 Running Advanced Error Detection...")
            try:
                advanced_errors = self.components['advanced_detector'].detect_all_errors()
                all_errors.extend(advanced_errors)

                # Convert to dictionary format for saving
                advanced_errors_dict = [self._convert_error_to_dict(error) for error in advanced_errors]

                with open(self.advanced_error_results_path, 'w') as f:
                    json.dump(advanced_errors_dict, f, indent=2)

                print(f"✅ Advanced detection found {len(advanced_errors)} errors")

            except Exception as e:
                print(f"❌ Advanced error detection failed: {e}")
                advanced_errors = []
        else:
            print("⚠️  Advanced Error Detector not available")
            advanced_errors = []

        # Logical error detection
        if 'logical_detector' in self.components:
            print("\n🧠 Running Logical Error Detection...")
            try:
                python_files = self._find_python_files()
                logical_errors = []

                for file_path in python_files[:10]:  # Limit to 10 files for performance
                    try:
                        file_logical_errors = self.components['logical_detector'].detect_logical_errors(file_path)
                        logical_errors.extend(file_logical_errors)
                    except Exception as e:
                        print(f"⚠️  Error analyzing {file_path}: {e}")

                all_errors.extend(logical_errors)

                # Convert and save
                logical_errors_dict = [self._convert_error_to_dict(error) for error in logical_errors]

                with open(self.logical_error_results_path, 'w') as f:
                    json.dump(logical_errors_dict, f, indent=2)

                print(f"✅ Logical detection found {len(logical_errors)} errors")

            except Exception as e:
                print(f"❌ Logical error detection failed: {e}")
                logical_errors = []
        else:
            print("⚠️  Logical Error Detector not available")
            logical_errors = []

        return {
            'total_errors_found': len(all_errors),
            'advanced_errors': len(advanced_errors),
            'logical_errors': len(logical_errors),
            'error_details': [self._convert_error_to_dict(error) for error in all_errors]
        }

    def run_combination_testing(self) -> dict:
        """Run cross-file combination testing"""
        print("\n" + "=" * 80)
        print("PHASE 2: Cross-File Combination Testing")
        print("=" * 80)

        if 'combination_tester' not in self.components:
            print("⚠️  Combination Tester not available")
            return {'combination_errors': 0, 'error_details': []}

        try:
            python_files = self._find_python_files()
            combination_errors = self.components['combination_tester'].analyze_combinations(python_files)

            # Convert and save
            combination_errors_dict = [self._convert_error_to_dict(error) for error in combination_errors]

            with open(self.combination_results_path, 'w') as f:
                json.dump(combination_errors_dict, f, indent=2)

            print(f"✅ Combination testing found {len(combination_errors)} errors")

            return {
                'combination_errors': len(combination_errors),
                'error_details': combination_errors_dict
            }

        except Exception as e:
            print(f"❌ Combination testing failed: {e}")
            return {'combination_errors': 0, 'error_details': []}

    def run_runtime_analysis(self) -> dict:
        """Run runtime interaction analysis"""
        print("\n" + "=" * 80)
        print("PHASE 3: Runtime Interaction Analysis")
        print("=" * 80)

        if 'runtime_analyzer' not in self.components:
            print("⚠️  Runtime Analyzer not available")
            return {'runtime_errors': 0, 'error_details': []}

        try:
            python_files = self._find_python_files()
            runtime_errors = self.components['runtime_analyzer'].analyze_runtime_interactions(python_files)

            # Convert and save
            runtime_errors_dict = [self._convert_error_to_dict(error) for error in runtime_errors]

            with open(self.runtime_results_path, 'w') as f:
                json.dump(runtime_errors_dict, f, indent=2)

            print(f"✅ Runtime analysis found {len(runtime_errors)} errors")

            return {
                'runtime_errors': len(runtime_errors),
                'error_details': runtime_errors_dict
            }

        except Exception as e:
            print(f"❌ Runtime analysis failed: {e}")
            return {'runtime_errors': 0, 'error_details': []}

    def run_pattern_analysis(self, all_errors: list) -> dict:
        """Run pattern correlation and clustering analysis"""
        print("\n" + "=" * 80)
        print("PHASE 4: Pattern Recognition and Correlation Analysis")
        print("=" * 80)

        if 'pattern_analyzer' not in self.components:
            print("⚠️  Pattern Analyzer not available")
            return {'patterns_recognized': 0, 'clusters_created': 0}

        try:
            # Convert errors to ErrorInfo objects for pattern analyzer
            error_info_objects = []
            for error_dict in all_errors:
                try:
                    # Convert dict back to ErrorInfo-like object
                    error_info_objects.append(error_dict)  # Simplified for now
                except Exception as e:
                    print(f"⚠️  Could not convert error for pattern analysis: {e}")

            # Run pattern analysis
            if error_info_objects:
                pattern_results = self.components['pattern_analyzer'].analyze_error_patterns(error_info_objects)

                with open(self.pattern_results_path, 'w') as f:
                    json.dump(pattern_results, f, indent=2, default=str)

                print(f"✅ Pattern analysis completed")
                print(f"  🔍 Recognized patterns: {len(pattern_results.get('recognized_patterns', []))}")
                print(f"  📊 Created clusters: {len(pattern_results.get('error_clusters', []))}")

                return {
                    'patterns_recognized': len(pattern_results.get('recognized_patterns', [])),
                    'clusters_created': len(pattern_results.get('error_clusters', [])),
                    'pattern_details': pattern_results
                }
            else:
                print("⚠️  No errors available for pattern analysis")
                return {'patterns_recognized': 0, 'clusters_created': 0}

        except Exception as e:
            print(f"❌ Pattern analysis failed: {e}")
            return {'patterns_recognized': 0, 'clusters_created': 0}

    def run_windows_simulation(self) -> dict:
        """Run Windows environment simulation"""
        print("\n" + "=" * 80)
        print("PHASE 5: Windows Environment Simulation")
        print("=" * 80)

        if 'windows_simulator' not in self.components:
            print("⚠️  Windows Simulator not available")
            return {'windows_issues': 0, 'issue_details': []}

        try:
            windows_errors = self.components['windows_simulator'].run_all_simulations()

            # Convert and save
            windows_errors_dict = [self._convert_error_to_dict(error) for error in windows_errors]

            with open(self.windows_results_path, 'w') as f:
                json.dump(windows_errors_dict, f, indent=2)

            print(f"✅ Windows simulation found {len(windows_errors)} issues")

            return {
                'windows_issues': len(windows_errors),
                'issue_details': windows_errors_dict
            }

        except Exception as e:
            print(f"❌ Windows simulation failed: {e}")
            return {'windows_issues': 0, 'issue_details': []}

    def apply_intelligent_fixes(self, errors: list) -> dict:
        """Apply context-aware intelligent fixes"""
        print("\n" + "=" * 80)
        print("PHASE 6: Intelligent Fix Application")
        print("=" * 80)

        if 'fix_engine' not in self.components:
            print("⚠️  Fix Engine not available")
            return {'fixes_applied': 0, 'fix_details': []}

        try:
            fixes_applied = []
            fix_results = []

            for error_dict in errors[:20]:  # Limit to 20 errors for safety
                try:
                    # Create a simple error object for fixing
                    error_obj = type('ErrorObj', (), error_dict)()
                    file_path = self.project_root / error_obj.file_path

                    if file_path.exists():
                        # Read current file content
                        with open(file_path, 'r', encoding='utf-8') as f:
                            file_content = f.read()

                        # Apply fix
                        fix_result = self.components['fix_engine'].apply_fix(error_obj, file_content)

                        if fix_result.success:
                            # Write fixed content
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(fix_result.fixed_code)

                            fixes_applied.append({
                                'file_path': str(file_path),
                                'error_type': error_obj.error_type,
                                'changes_made': fix_result.changes_made
                            })

                            fix_results.append(fix_result)

                except Exception as e:
                    print(f"⚠️  Could not apply fix to {error_dict.get('file_path', 'unknown')}: {e}")

            print(f"✅ Applied {len(fixes_applied)} intelligent fixes")

            return {
                'fixes_applied': len(fixes_applied),
                'fix_details': fixes_applied
            }

        except Exception as e:
            print(f"❌ Fix application failed: {e}")
            return {'fixes_applied': 0, 'fix_details': []}

    def generate_enhanced_comprehensive_report(self, all_results: dict) -> dict:
        """Generate enhanced comprehensive report with correlation tracking"""
        print("\n" + "=" * 80)
        print("PHASE 7: Generating Enhanced Comprehensive Report")
        print("=" * 80)

        if 'csv_logger' not in self.components:
            print("⚠️  CSV Logger not available")
            return {'csv_path': None, 'total_errors': 0}

        try:
            # Collect all errors from all phases
            all_errors = []

            # Add errors from all phases
            for phase in ['advanced_error_results', 'logical_error_results', 'combination_results', 'runtime_results']:
                phase_path = getattr(self, f"{phase}_path", None)
                if phase_path and Path(phase_path).exists():
                    with open(phase_path, 'r') as f:
                        phase_errors = json.load(f)
                        all_errors.extend(phase_errors)

            # Add correlation data
            enhanced_errors = []
            for error in all_errors:
                enhanced_error = error.copy()
                # Add enhanced fields
                enhanced_error.update({
                    'analysis_phase': self._determine_analysis_phase(error),
                    'correlation_context': self._get_correlation_context(error),
                    'fix_strategy': self._suggest_fix_strategy(error)
                })
                enhanced_errors.append(enhanced_error)

            # Create enhanced CSV report
            csv_path = self.components['csv_logger'].create_error_report(
                enhanced_errors,
                include_correlations=True,
                include_fixes=True
            )

            # Generate correlation analysis
            correlation_path = self.components['csv_logger'].export_correlation_analysis(
                f"/tmp/bsee_correlation_analysis_{self.timestamp}.txt"
            )

            print(f"✅ Enhanced CSV report created: {csv_path}")
            print(f"✅ Correlation analysis exported: {correlation_path}")

            # Generate summary statistics
            stats = self.components['csv_logger'].get_error_statistics()

            return {
                'csv_path': str(csv_path),
                'correlation_path': str(correlation_path),
                'total_errors': len(all_errors),
                'statistics': stats,
                'phase_breakdown': {
                    'advanced_errors': all_results.get('total_errors_found', 0),
                    'combination_errors': all_results.get('combination_errors', 0),
                    'runtime_errors': all_results.get('runtime_errors', 0),
                    'windows_issues': all_results.get('windows_issues', 0)
                }
            }

        except Exception as e:
            print(f"❌ Enhanced report generation failed: {e}")
            return {'csv_path': None, 'total_errors': 0}

    def _find_python_files(self) -> list:
        """Find all Python files in the project"""
        python_files = []
        for root, dirs, files in os.walk(self.project_root):
            # Skip cache and hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in [
                '__pycache__', 'node_modules', '.git', '.pytest_cache'
            ]]

            for file in files:
                if file.endswith('.py'):
                    file_path = Path(root) / file
                    python_files.append(file_path)

        return sorted(python_files)

    def _convert_error_to_dict(self, error) -> dict:
        """Convert ErrorInfo object to dictionary"""
        if hasattr(error, '__dict__'):
            return {
                'file_path': getattr(error, 'file_path', ''),
                'error_type': getattr(error, 'error_type', ''),
                'error_message': getattr(error, 'error_message', ''),
                'severity': getattr(error, 'severity', {}).value if hasattr(getattr(error, 'severity', None), 'value') else str(getattr(error, 'severity', '')),
                'category': getattr(error, 'category', {}).value if hasattr(getattr(error, 'category', None), 'value') else str(getattr(error, 'category', '')),
                'line_number': getattr(error, 'line_number', None),
                'suggested_fix': getattr(error, 'suggested_fix', ''),
                'timestamp': getattr(error, 'timestamp', datetime.now().isoformat()),
                'test_context': getattr(error, 'test_context', '')
            }
        elif isinstance(error, dict):
            return error
        else:
            return {'error_type': 'Unknown', 'error_message': str(error)}

    def _determine_analysis_phase(self, error: dict) -> str:
        """Determine which analysis phase found this error"""
        error_type = error.get('error_type', '')

        if error_type in ['UnusedVariable', 'UnreachableCode', 'DeadCode']:
            return 'LOGICAL_ANALYSIS'
        elif 'Combination' in error_type or 'Dependency' in error_type:
            return 'COMBINATION_TESTING'
        elif 'Resource' in error_type or 'Runtime' in error_type:
            return 'RUNTIME_ANALYSIS'
        elif 'Windows' in error_type:
            return 'WINDOWS_SIMULATION'
        else:
            return 'ADVANCED_DETECTION'

    def _get_correlation_context(self, error: dict) -> str:
        """Get correlation context for an error"""
        file_path = error.get('file_path', '')
        error_type = error.get('error_type', '')

        # Simple correlation context based on file and error type
        return f"{Path(file_path).name}_{error_type}"

    def _suggest_fix_strategy(self, error: dict) -> str:
        """Suggest fix strategy for an error"""
        error_type = error.get('error_type', '')

        strategy_map = {
            'ImportError': 'INSTALL_DEPENDENCY',
            'SyntaxError': 'MANUAL_FIX',
            'UnusedVariable': 'AUTOMATED_REMOVAL',
            'PotentialResourceLeak': 'REFACTOR_PATTERN',
            'LogicalAntiPattern': 'CODE_REVIEW',
            'CircularDependency': 'ARCHITECTURAL_CHANGE'
        }

        return strategy_map.get(error_type, 'MANUAL_REVIEW')

    def run_complete_enhanced_analysis(self) -> dict:
        """Run the complete enhanced error analysis pipeline"""
        print("🚀 Starting Enhanced BSEE Error Analysis Pipeline")
        print(f"📁 Project root: {self.project_root}")
        print(f"⏰ Timestamp: {self.timestamp}")
        print(f"🔧 Available components: {len(self.components)}")
        print()

        # Collect all results
        all_results = {}
        all_errors = []

        # Phase 1: Enhanced Error Detection
        detection_results = self.run_enhanced_error_analysis()
        all_results.update(detection_results)
        all_errors.extend(detection_results.get('error_details', []))

        # Phase 2: Combination Testing
        combination_results = self.run_combination_testing()
        all_results.update(combination_results)
        all_errors.extend(combination_results.get('error_details', []))

        # Phase 3: Runtime Analysis
        runtime_results = self.run_runtime_analysis()
        all_results.update(runtime_results)
        all_errors.extend(runtime_results.get('error_details', []))

        # Phase 4: Pattern Analysis
        pattern_results = self.run_pattern_analysis(all_errors)
        all_results.update(pattern_results)

        # Phase 5: Windows Simulation
        windows_results = self.run_windows_simulation()
        all_results.update(windows_results)
        all_errors.extend(windows_results.get('issue_details', []))

        # Phase 6: Intelligent Fix Application (optional, limited scope)
        fix_results = self.apply_intelligent_fixes(all_errors[:10])  # Limit for safety
        all_results.update(fix_results)

        # Phase 7: Enhanced Comprehensive Report
        report_results = self.generate_enhanced_comprehensive_report(all_results)
        all_results.update(report_results)

        # Final summary
        print("\n" + "=" * 80)
        print("🎉 ENHANCED ANALYSIS COMPLETE")
        print("=" * 80)

        total_errors = (
            detection_results.get('total_errors_found', 0) +
            combination_results.get('combination_errors', 0) +
            runtime_results.get('runtime_errors', 0) +
            windows_results.get('windows_issues', 0)
        )

        print(f"📊 Total Errors Found: {total_errors}")
        print(f"🔍 Advanced Detection: {detection_results.get('total_errors_found', 0)}")
        print(f"🔗 Combination Testing: {combination_results.get('combination_errors', 0)}")
        print(f"⚡ Runtime Analysis: {runtime_results.get('runtime_errors', 0)}")
        print(f"🪟 Pattern Recognition: {pattern_results.get('patterns_recognized', 0)} patterns")
        print(f"🔧 Fixes Applied: {fix_results.get('fixes_applied', 0)}")
        print(f"🪟 Windows Issues: {windows_results.get('windows_issues', 0)}")
        print(f"📋 Enhanced CSV Report: {report_results.get('csv_path', 'N/A')}")
        print(f"🔗 Correlation Analysis: {report_results.get('correlation_path', 'N/A')}")

        return {
            'detection_results': detection_results,
            'combination_results': combination_results,
            'runtime_results': runtime_results,
            'pattern_results': pattern_results,
            'windows_results': windows_results,
            'fix_results': fix_results,
            'report_results': report_results,
            'timestamp': self.timestamp,
            'total_errors': total_errors
        }

    def get_enhanced_fix_recommendations(self) -> list:
        """Get enhanced prioritized fix recommendations"""
        recommendations = []

        # Load latest enhanced results
        if self.enhanced_csv_path and Path(self.enhanced_csv_path).exists():
            try:
                stats = self.components['csv_logger'].get_error_statistics()

                # Analyze statistics for recommendations
                if stats.get('manual_review_count', 0) > 0:
                    recommendations.append({
                        'priority': 'CRITICAL',
                        'issue': 'Manual Review Required',
                        'description': f"{stats['manual_review_count']} errors require manual expert review",
                        'fix': 'Review correlation analysis and apply targeted fixes',
                        'affected_files': stats['manual_review_count']
                    })

                if stats.get('by_correlation'):
                    high_corr_count = len([count for count in stats['by_correlation'].values() if count > 3])
                    if high_corr_count > 0:
                        recommendations.append({
                            'priority': 'HIGH',
                            'issue': 'Correlated Error Patterns',
                            'description': f"{high_corr_count} error correlation groups found indicating systematic issues",
                            'fix': 'Address root causes identified in correlation analysis',
                            'affected_files': sum(stats['by_correlation'].values())
                        })

                # Add category-specific recommendations
                by_category = stats.get('by_category', {})
                if by_category.get('DEAD_CODE', 0) > 5:
                    recommendations.append({
                        'priority': 'MEDIUM',
                        'issue': 'Dead Code Accumulation',
                        'description': f"{by_category['DEAD_CODE']} dead code issues detected",
                        'fix': 'Run automated cleanup and review unused code patterns',
                        'affected_files': by_category['DEAD_CODE']
                    })

                if by_category.get('RESOURCE_LEAK', 0) > 0:
                    recommendations.append({
                        'priority': 'HIGH',
                        'issue': 'Resource Management Issues',
                        'description': f"{by_category['RESOURCE_LEAK']} potential resource leaks found",
                        'fix': 'Implement context managers and proper resource cleanup',
                        'affected_files': by_category['RESOURCE_LEAK']
                    })

            except Exception as e:
                print(f"Could not generate enhanced recommendations: {e}")

        return recommendations


def main():
    """Main function for running the enhanced analysis"""
    import argparse

    parser = argparse.ArgumentParser(description="Enhanced BSEE error analysis pipeline")
    parser.add_argument("--project-root", default=".", help="Root directory of the project")
    parser.add_argument("--recommendations", action="store_true", help="Show enhanced fix recommendations")
    parser.add_argument("--fix-automatically", action="store_true", help="Apply automatic fixes where safe")
    parser.add_argument("--export-patterns", action="store_true", help="Export fix patterns")

    args = parser.parse_args()

    # Run complete enhanced analysis
    pipeline = EnhancedErrorAnalysisPipeline(args.project_root)
    results = pipeline.run_complete_enhanced_analysis()

    # Show recommendations if requested
    if args.recommendations:
        print("\n" + "=" * 80)
        print("🔧 ENHANCED FIX RECOMMENDATIONS")
        print("=" * 80)

        recommendations = pipeline.get_enhanced_fix_recommendations()
        for i, rec in enumerate(recommendations, 1):
            print(f"\n{i}. {rec['priority']} PRIORITY: {rec['issue']}")
            print(f"   📝 Description: {rec['description']}")
            print(f"   🔧 Fix: {rec['fix']}")
            print(f"   📁 Affected files: {rec['affected_files']}")

    # Export fix patterns if requested
    if args.export_patterns and 'fix_engine' in pipeline.components:
        try:
            patterns_path = pipeline.components['fix_engine'].export_fix_patterns()
            print(f"\n📋 Fix patterns exported to: {patterns_path}")
        except Exception as e:
            print(f"Could not export fix patterns: {e}")

    print(f"\n🎯 Enhanced analysis completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return results


if __name__ == "__main__":
    main()