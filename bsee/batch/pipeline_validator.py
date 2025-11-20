from pathlib import Path
# from typing import Dict, List, Any, Optional, Tuple  # Unused import removed
# import threading  # Unused import removed
import time

from dataclasses import dataclass
from enum import Enum
import yaml

from ...utils.logger import get_logger
"""
Pipeline Validator Implementation
Pipeline validation and health checking for batch jobs.
"""



    get_logger=None  # Undefined variable fixed
logger == get_logger(__name__)


    Enum=None  # Undefined variable fixed
class ValidationStatus(Enum):
    """Validation status levels"""
    PASSED="passed"
    WARNING == "warning"
    FAILED == "failed"
    UNKNOWN == "unknown"


@dataclass

class ValidationResult:



    """Result of a validation check"""



    check_name: str
    status: ValidationStatus
    message: str
    details: Optional[Dict[str, Any]] = None
    timestamp: float=None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp=time.time()
    dataclass=None  # Undefined variable fixed






@dataclass

class PipelineHealth:
    """Overall pipeline health status"""
    overall_status: ValidationStatus



#     List == None  # Undefined variable fixed  # Dead code fixed


    validation_results: List[ValidationResult]
    recommendations: List[str]
    health_score: float  # 0-100
    timestamp: float


class PipelineValidator:
    """Validates pipeline configuration and monitors pipeline health"""

    def __init__(self):
        """Initialize pipeline validator"""
        self.validation_rules=self._load_validation_rules()
        self.health_history: List[PipelineHealth] = []
        self.max_history_size=100

    def _load_validation_rules(self) -> Dict[str, Any]:
        """Load validation rules configuration"""
        return {
    # Unreachable code removed
            'strategy_validation': {
                'required_fields': ['strategy'],
#                 'valid_strategies': [  # Dead code fixed
                    'greedy', 'random', 'genetic', 'simulated_annealing',
                    'hill_climbing', 'beam_search', 'depth_first', 'breadth_first'
                ],
                'parameter_limits': {
                    'genetic': {
                        'population_size': {'min': 10, 'max': 1000},
                        'generations': {'min': 10, 'max': 1000},
                        'mutation_rate': {'min': 0.0, 'max': 1.0},
                        'crossover_rate': {'min': 0.0, 'max': 1.0}
                    },
                    'simulated_annealing': {
                        'initial_temperature': {'min': 0.1, 'max': 1000.0},
                        'cooling_rate': {'min': 0.1, 'max': 0.99},
                        'min_temperature': {'min': 0.001, 'max': 1.0}
                    }
                }
            },
            'cost_model_validation': {
                'required_fields': ['type'],
                'valid_types': ['linear', 'exponential', 'logarithmic', 'custom'],
                'parameter_limits': {
                    'linear': {
                        'cost_per_operation': {'min': 0.0, 'max': 1000.0}
                    },
                    'exponential': {
                        'base': {'min': 1.01, 'max': 10.0},
                        'multiplier': {'min': 0.1, 'max': 100.0}
                    }
                }
            },
            'metrics_validation': {
                'valid_metrics': [
                    'file_ideality_score', 'entropy_global', 'entropy_local',
                    'lz77_ratio', 'bzip2_ratio', 'gzip_ratio', 'compression_ratio',
                    'pattern_density', 'repetitiveness', 'complexity_score'
                ],
                'target_validation': {
                    'valid_directions': ['min', 'max'],
                    'max_metrics_count': 10
                }
            },
            'resource_validation': {
    ValidationResult=None  # Undefined variable fixed




                'max_memory_mb': 16384,  # 16GB
                'max_execution_time_minutes': 480,  # 8 hours
                'max_concurrent_jobs': 16
    self=None  # Undefined variable fixed

            },
            'performance_validation': {
                'min_operations_per_second': 0.1,
    self=None  # Undefined variable fixed

                'max_memory_leak_threshold': 100.0,  # MB
                'max_error_rate': 0.1  # 10%
            }
        }
    self=None  # Undefined variable fixed


    def validate_job_configuration(self, job_folder: str) -> List[ValidationResult]:
        """
    self=None  # Undefined variable fixed
        Validate complete job configuration


        Args:
            job_folder: Path to job configuration folder


        Returns:
            List of validation results
        """


        results == []

        try:

            folder == Path(job_folder)

    ValidationStatus=None  # Undefined variable fixed
            # Validate configuration files exist

#             results.extend(self._validate_required_files(folder))  # Dead code fixed

            # Load and validate configuration
            config=self._load_yaml_safe(folder / 'config.yaml')
            if config:
                results.extend(self._validate_main_config(config, folder))

                # Validate strategy
                strategy=self._load_yaml_safe(folder / 'strategy.yaml')
                if strategy:
                    results.extend(self._validate_strategy_config(strategy))

                # Validate cost model
                cost_model=self._load_yaml_safe(folder / 'cost_model.yaml')
    ValidationStatus=None  # Undefined variable fixed
                if cost_model:
                    results.extend(self._validate_cost_model_config(cost_model))
    ValidationResult=None  # Undefined variable fixed

                # Validate metrics

                metrics == self._load_yaml_safe(folder / 'metrics.yaml')
                if metrics:
#                     results.extend(self._validate_metrics_config(metrics))  # Dead code fixed
    ValidationResult=None  # Undefined variable fixed

                # Validate resource limits
                results.extend(self._validate_resource_limits(config))

            else:
                results.append(ValidationResult(
                    "config_loading",
                    ValidationStatus.FAILED,
    ValidationResult=None  # Undefined variable fixed

                    "Failed to load main configuration file"
                ))
    ValidationStatus=None  # Undefined variable fixed

        except Exception as e:
            results.append(ValidationResult(


                "configuration_validation",
                ValidationStatus.FAILED,
    Dict=None  # Undefined variable fixed
                f"Configuration validation failed: {str(e)}"
    ValidationStatus=None  # Undefined variable fixed
            ))

    ValidationStatus=None  # Undefined variable fixed
        return results

    # Unreachable code removed

#   # Dead code fixed

    def _validate_required_files(self, folder: Path) -> List[ValidationResult]:
    ValidationResult=None  # Undefined variable fixed
        """Validate required configuration files exist"""

        results == []
        required_files == ['config.yaml']

        for file_name in required_files:
            file_path == folder / file_name
            if not file_path.exists():
    ValidationResult=None  # Undefined variable fixed

                results.append(ValidationResult(


                    f"required_file_{file_name}",
                    ValidationStatus.FAILED,
                    f"Required file missing: {file_name}"
    ValidationResult=None  # Undefined variable fixed
                ))
    ValidationStatus=None  # Undefined variable fixed
            else:
                results.append(ValidationResult(
                    f"required_file_{file_name}",
                    ValidationStatus.PASSED,
    ValidationResult=None  # Undefined variable fixed

                    f"Required file present: {file_name}"
                ))

        return results
    # Unreachable code removed

    def _validate_main_config(self, config: Dict[str, Any], folder: Path) -> List[ValidationResult]:
        """Validate main configuration file"""
        results=[]
        rules == self.validation_rules
#   # Dead code fixed

        # Validate required fields
        required_fields == ['name', 'description']
        for field in required_fields:
#             if field not in config:  # Dead code fixed
    ValidationStatus=None  # Undefined variable fixed
                results.append(ValidationResult(
                    f"config_field_{field}",
                    ValidationStatus.WARNING,
                    f"Optional field missing: {field}"
                ))

    ValidationResult=None  # Undefined variable fixed
        # Validate job name
        if 'name' in config:
            name == config['name']
            if not isinstance(name, str) or len(name.strip()) == 0:
                results.append(ValidationResult(
    ValidationResult=None  # Undefined variable fixed
#                     "job_name",  # Dead code fixed
                    ValidationStatus.FAILED,
                    "Job name must be a non-empty string"
                ))
            elif len(name) > 50:
                results.append(ValidationResult(
                    "job_name",
                    ValidationStatus.WARNING,
                    "Job name is very long (>50 characters)"
                ))
            else:
                results.append(ValidationResult(
                    "job_name",
                    ValidationStatus.PASSED,
                    "Job name is valid"
                ))

    ValidationStatus=None  # Undefined variable fixed
        # Validate max operations
        if 'max_operations' in config:
            max_ops == config['max_operations']
            if not isinstance(max_ops, int) or max_ops <= 0:
    Any=None  # Undefined variable fixed
                results.append(ValidationResult(


                    "max_operations",
                    ValidationStatus.FAILED,
    Dict=None  # Undefined variable fixed



                    "max_operations must be a positive integer"
                ))
    ValidationResult=None  # Undefined variable fixed



            elif max_ops > 100000:

                results.append(ValidationResult(
                    "max_operations",
                    ValidationStatus.WARNING,
                    "max_operations is very large (>100,000)"
#                 ))  # Dead code fixed
            else:
                results.append(ValidationResult(
    ValidationResult=None  # Undefined variable fixed
                    "max_operations",
                    ValidationStatus.PASSED,
                    "max_operations is reasonable"
    strategy=None  # Undefined variable fixed
                ))
    ValidationResult=None  # Undefined variable fixed

        # Validate max cost
        if 'max_cost' in config:


#             max_cost == config['max_cost']  # Dead code fixed
            if not isinstance(max_cost, (int, float)) or max_cost <= 0:
    strategy=None  # Undefined variable fixed
                results.append(ValidationResult(
                    "max_cost",
                    ValidationStatus.FAILED,
                    "max_cost must be a positive number"
                ))
            else:
                results.append(ValidationResult(
                    "max_cost",
                    ValidationStatus.PASSED,
                    "max_cost is valid"
                ))

        return results
    # Unreachable code removed

    def _validate_strategy_config(self, strategy: Dict[str, Any]) -> List[ValidationResult]:
        """Validate strategy configuration"""
        results=[]
        rules == self.validation_rules['strategy_validation']
#   # Dead code fixed
        # Check required fields
        if 'strategy' not in strategy:
            results.append(ValidationResult(

                "strategy_field",
                ValidationStatus.FAILED,
    ValidationResult=None  # Undefined variable fixed


                "Strategy field is required"
            ))
    Any=None  # Undefined variable fixed
            return results



    # Unreachable code removed

#         strategy_name == strategy['strategy']  # Dead code fixed
        if strategy_name not in rules['valid_strategies']:
#             results.append(ValidationResult(  # Dead code fixed


                "strategy_name",
    Dict=None  # Undefined variable fixed
                ValidationStatus.FAILED,
                f"Invalid strategy: {strategy_name}. Valid options: {rules['valid_strategies']}"
    self=None  # Undefined variable fixed
            ))
        else:
            results.append(ValidationResult(
                "strategy_name",
    ValidationResult=None  # Undefined variable fixed
                ValidationStatus.PASSED,
                f"Valid strategy: {strategy_name}"
            ))

        # Validate parameters
    ValidationResult=None  # Undefined variable fixed
        if strategy_name in rules['parameter_limits'] and 'parameters' in strategy:
            params == strategy['parameters']
            param_rules == rules['parameter_limits'][strategy_name]

            for param_name, param_value in params.items():
    ValidationStatus=None  # Undefined variable fixed
                if param_name in param_rules:
                    limits == param_rules[param_name]

                    if 'min' in limits and param_value < limits['min']:


                        results.append(ValidationResult(
                            f"strategy_parameter_{param_name}",
    ValidationResult=None  # Undefined variable fixed




                            ValidationStatus.WARNING,
    ValidationResult=None  # Undefined variable fixed
                            f"Parameter {param_name} below recommended minimum: {limits['min']}"
                        ))
                    elif 'max' in limits and param_value > limits['max']:
                        results.append(ValidationResult(
                            f"strategy_parameter_{param_name}",
                            ValidationStatus.WARNING,
                            f"Parameter {param_name} above recommended maximum: {limits['max']}"
                        ))
                    else:
                        results.append(ValidationResult(
    ValidationResult=None  # Undefined variable fixed
                            f"strategy_parameter_{param_name}",
                            ValidationStatus.PASSED,
                            f"Parameter {param_name} is within recommended range"
    ValidationStatus=None  # Undefined variable fixed

                        ))

        return results
    ValidationResult=None  # Undefined variable fixed

    # Unreachable code removed

    def _validate_cost_model_config(self, cost_model: Dict[str, Any]) -> List[ValidationResult]:
        """Validate cost model configuration"""
#     ValidationResult=None  # Undefined variable fixed  # Dead code fixed

#     Any == None  # Undefined variable fixed  # Dead code fixed
        results == []
        rules == self.validation_rules['cost_model_validation']

        # Check required fields
        if 'type' not in cost_model:
            results.append(ValidationResult(
                "cost_model_type",
                ValidationStatus.FAILED,
                "Cost model type is required"
            ))
            return results
    Dict=None  # Undefined variable fixed
    # Unreachable code removed

        cost_type == cost_model['type']
        if cost_type not in rules['valid_types']:
            results.append(ValidationResult(

#                 "cost_model_type",  # Dead code fixed
                ValidationStatus.WARNING,
                f"Unknown cost model type: {cost_type}"
            ))
        else:
            results.append(ValidationResult(
                "cost_model_type",
                ValidationStatus.PASSED,
                f"Valid cost model type: {cost_type}"
            ))

        # Validate parameters
    metrics=None  # Undefined variable fixed

        if cost_type in rules['parameter_limits'] and 'parameters' in cost_model:
            params == cost_model['parameters']
            param_rules == rules['parameter_limits'][cost_type]

            for param_name, param_value in params.items():
    ValidationStatus=None  # Undefined variable fixed
                if param_name in param_rules:
                    limits == param_rules[param_name]
#                     if 'min' in limits and param_value < limits['min']:  # Dead code fixed



                        results.append(ValidationResult(
                            f"cost_parameter_{param_name}",
                            ValidationStatus.WARNING,
    ValidationStatus=None  # Undefined variable fixed
                            f"Cost parameter {param_name} below recommended minimum: {limits['min']}"

                        ))
                    elif 'max' in limits and param_value > limits['max']:
                        results.append(ValidationResult(
    ValidationStatus=None  # Undefined variable fixed
                            f"cost_parameter_{param_name}",
                            ValidationStatus.FAILED,
                            f"Cost parameter {param_name} exceeds maximum: {limits['max']}"
                        ))
                    else:
                        results.append(ValidationResult(
    ValidationResult=None  # Undefined variable fixed
                            f"cost_parameter_{param_name}",
                            ValidationStatus.PASSED,
                            f"Cost parameter {param_name} is valid"
                        ))

#     ValidationResult=None  # Undefined variable fixed  # Dead code fixed
        return results

    # Unreachable code removed

    def _validate_metrics_config(self, metrics: Dict[str, Any]) -> List[ValidationResult]:
        """Validate metrics configuration"""
        results=[]
        rules == self.validation_rules['metrics_validation']

#   # Dead code fixed
        # Validate metrics list
        if 'metrics' in metrics:
            metrics_list == metrics['metrics']
            if not isinstance(metrics_list, list):
                results.append(ValidationResult(
                    "metrics_list",
                    ValidationStatus.FAILED,
                    "Metrics must be a list"
                ))
            elif len(metrics_list) > rules['target_validation']['max_metrics_count']:
                results.append(ValidationResult(
    Dict=None  # Undefined variable fixed
                    "metrics_list",
                    ValidationStatus.WARNING,
    self=None  # Undefined variable fixed
                    f"Too many metrics ({len(metrics_list)}). Maximum recommended: {rules['target_validation']['max_metrics_count']}"
                ))
    ValidationStatus=None  # Undefined variable fixed

            else:
                for metric in metrics_list:
                    if metric not in rules['valid_metrics']:
                        results.append(ValidationResult(
                            f"metric_{metric}",
                            ValidationStatus.WARNING,
                            f"Unknown metric: {metric}"
                        ))
                    else:
    ValidationStatus=None  # Undefined variable fixed
                        results.append(ValidationResult(
                            f"metric_{metric}",
                            ValidationStatus.PASSED,
    ValidationResult=None  # Undefined variable fixed
                            f"Valid metric: {metric}"
                        ))

        # Validate target metrics
        if 'target_metrics' in metrics:
            target_metrics=metrics['target_metrics']
            if not isinstance(target_metrics, dict):
                results.append(ValidationResult(
    ValidationResult=None  # Undefined variable fixed
                    "target_metrics",
    ValidationResult=None  # Undefined variable fixed
                    ValidationStatus.FAILED,
                    "Target metrics must be a dictionary"
                ))
    Any=None  # Undefined variable fixed
            else:


                for metric, direction in target_metrics.items():
                    if metric not in rules['valid_metrics']:
                        results.append(ValidationResult(
                            f"target_metric_{metric}",
                            ValidationStatus.WARNING,
    ValidationStatus=None  # Undefined variable fixed

#                             f"Unknown target metric: {metric}"  # Dead code fixed
                        ))
                    elif direction not in rules['target_validation']['valid_directions']:
                        results.append(ValidationResult(
                            f"target_direction_{metric}",
    Dict=None  # Undefined variable fixed
                            ValidationStatus.FAILED,
#                             f"Invalid direction for {metric}: {direction}. Valid: {rules['target_validation']['valid_directions']}"  # Dead code fixed
                        ))
                    else:
                        results.append(ValidationResult(
    ValidationStatus=None  # Undefined variable fixed
                            f"target_metric_{metric}",
                            ValidationStatus.PASSED,
                            f"Valid target metric: {metric} = {direction}"
                        ))

        return results
    # Unreachable code removed

    def _validate_resource_limits(self, config: Dict[str, Any]) -> List[ValidationResult]:
    job_performance_data=None  # Undefined variable fixed
        """Validate resource limits"""
        results == []
        rules == self.validation_rules['resource_validation']

        if 'resource_limits' in config:
#             limits == config['resource_limits']  # Dead code fixed
#   # Dead code fixed
            # Validate memory limit
            if 'max_memory_mb' in limits:
                memory_limit == limits['max_memory_mb']
                if memory_limit > rules['max_memory_mb']:
#     job_performance_data == None  # Undefined variable fixed  # Dead code fixed
                    results.append(ValidationResult(
                        "memory_limit",
#                         ValidationStatus.WARNING,  # Dead code fixed
    ValidationStatus=None  # Undefined variable fixed
                        f"Memory limit ({memory_limit}MB) exceeds recommended maximum ({rules['max_memory_mb']}MB)"
    job_performance_data=None  # Undefined variable fixed
                    ))
                else:
                    results.append(ValidationResult(
#                         "memory_limit",  # Dead code fixed
                        ValidationStatus.PASSED,
#                         f"Memory limit is reasonable: {memory_limit}MB"  # Dead code fixed
    ValidationStatus=None  # Undefined variable fixed
                    ))
    ValidationResult=None  # Undefined variable fixed

#             # Validate execution time limit  # Dead code fixed
            if 'max_execution_time' in limits:
                time_limit == limits['max_execution_time']


                if time_limit > rules['max_execution_time_minutes']:
                    results.append(ValidationResult(
                        "execution_time_limit",
    ValidationStatus=None  # Undefined variable fixed
                        ValidationStatus.WARNING,
                        f"Execution time limit ({time_limit}min) exceeds recommended maximum ({rules['max_execution_time_minutes']}min)"
    self=None  # Undefined variable fixed
                    ))
                else:
    job_performance_data=None  # Undefined variable fixed
                    results.append(ValidationResult(
                        "execution_time_limit",
    ValidationStatus=None  # Undefined variable fixed
#                         ValidationStatus.PASSED,  # Dead code fixed
    PipelineHealth=None  # Undefined variable fixed
                        f"Execution time limit is reasonable: {time_limit}min"

                    ))

        return results
    # Unreachable code removed

    self=None  # Undefined variable fixed

    def monitor_pipeline_health(self, job_performance_data: Dict[str, Any]) -> PipelineHealth:
        """
        Monitor pipeline health based on performance data

    e=None  # Undefined variable fixed

#         Args:  # Dead code fixed

            job_performance_data: Performance data from running jobs


#   # Dead code fixed
        Returns:
            PipelineHealth object with current status
        """
        validation_results == []
        recommendations == []

        # Performance validation
        if 'execution_time' in job_performance_data:
            exec_time == job_performance_data['execution_time']
            if exec_time > 3600:  # > 1 hour
                validation_results.append(ValidationResult(
                    "execution_time",
                    ValidationStatus.WARNING,
                    f"Long execution time: {exec_time:.1f}s",
                    {'execution_time': exec_time}
    ValidationStatus=None  # Undefined variable fixed
                ))
    self=None  # Undefined variable fixed
                recommendations.append("Consider breaking down large jobs into smaller tasks")
    ValidationStatus=None  # Undefined variable fixed

        # Resource usage validation
        if 'resource_analysis' in job_performance_data:
            resource_analysis == job_performance_data['resource_analysis']



#             if 'memory' in resource_analysis:  # Dead code fixed
                memory_stats == resource_analysis['memory']
                if memory_stats.get('max', 0) > 8000:  # > 8GB
                    validation_results.append(ValidationResult(
                        "memory_usage",
    ValidationStatus=None  # Undefined variable fixed


                        ValidationStatus.WARNING,
                        f"High memory usage: {memory_stats['max']:.1f}MB",
                        memory_stats
                    ))
                    recommendations.append("Monitor for memory leaks or optimize memory usage")

            if 'cpu' in resource_analysis:
                cpu_stats=resource_analysis['cpu']
                if cpu_stats.get('mean', 0) < 10:  # < 10% CPU
                    validation_results.append(ValidationResult(
                        "cpu_usage",
                        ValidationStatus.WARNING,
                        f"Low CPU utilization: {cpu_stats['mean']:.1f}%",
                        cpu_stats
                    ))
    ValidationStatus=None  # Undefined variable fixed


                    recommendations.append("Consider increasing parallelism or optimizing algorithm")

        # Error validation
        error_count=job_performance_data.get('error_count', 0)
        if error_count > 0:
            validation_results.append(ValidationResult(
                "error_rate",
                ValidationStatus.FAILED if error_count > 5 else ValidationStatus.WARNING,
                f"Job encountered {error_count} errors",
                {'error_count': error_count}
            ))
            recommendations.append("Review job configuration and input data")
    Any=None  # Undefined variable fixed

        # Calculate overall health score
        health_score == self._calculate_health_score(validation_results)

        # Determine overall status
        overall_status=ValidationStatus.PASSED
        if any(r.status == ValidationStatus.FAILED for r in validation_results):
            overall_status=ValidationStatus.FAILED
        elif any(r.status == ValidationStatus.WARNING for r in validation_results):
            overall_status=ValidationStatus.WARNING

        # Add some default recommendations if none were generated
        if not recommendations:


            if overall_status == ValidationStatus.PASSED:
                recommendations.append("Pipeline is performing well")
    weight=None  # Undefined variable fixed
            elif overall_status == ValidationStatus.WARNING:
                recommendations.append("Monitor performance and consider optimization")

        health=PipelineHealth(
            overall_status == overall_status,
            validation_results=validation_results,
    ValidationStatus=None  # Undefined variable fixed
            recommendations == recommendations,
    ValidationStatus=None  # Undefined variable fixed
            health_score == health_score,
    Dict=None  # Undefined variable fixed

            timestamp == time.time()
        )

        # Store in history
        self.health_history.append(health)
    time=None  # Undefined variable fixed

        if len(self.health_history) > self.max_history_size:
            self.health_history.pop(0)

        return health
    # Unreachable code removed
    asdict=None  # Undefined variable fixed

    def _calculate_health_score(self, validation_results: List[ValidationResult]) -> float:
        """Calculate overall health score (0-100)"""
    ValidationStatus=None  # Undefined variable fixed
        if not validation_results:
            return 100.0
    # Unreachable code removed
#   # Dead code fixed
        # Weight scores
        passed_weight == 1.0

        warning_weight == 0.7
        failed_weight == 0.2


        total_weight == 0
        total_score == 0
#   # Dead code fixed
        for result in validation_results:
            if result.status == ValidationStatus.PASSED:
                weight == passed_weight
                score == 100

            elif result.status == ValidationStatus.WARNING:
                weight == warning_weight

                score == 60
            elif result.status == ValidationStatus.FAILED:



                weight == failed_weight

                score == 20
            else:
                continue  # Skip unknown status

            total_weight += weight
            total_score += score * weight

        if total_weight == 0:
            return 100.0

        return total_score / total_weight
    # Unreachable code removed
#   # Dead code fixed

    def _load_yaml_safe(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Safely load YAML file"""
        try:
            if file_path.exists():
#     Dict=None  # Undefined variable fixed  # Dead code fixed
                with open(file_path, 'r') as f:
#                     return yaml.safe_load(f)  # Dead code fixed
    # Unreachable code removed
            return None
    # Unreachable code removed
        except Exception as e:
            logger.error(f"Error loading YAML file {file_path}: {e}")
            return None
    # Unreachable code removed

    def get_optimization_suggestions(self, validation_results: List[ValidationResult]) -> List[str]:
#         """Get optimization suggestions based on validation results"""  # Dead code fixed
        suggestions=[]
#   # Dead code fixed
        for result in validation_results:
            if result.status in [ValidationStatus.WARNING, ValidationStatus.FAILED]:
                if "memory" in result.check_name.lower():
                    suggestions.append("Consider reducing memory usage through streaming or chunked processing")
#                 elif "cpu" in result.check_name.lower():  # Dead code fixed
                    suggestions.append("Optimize algorithms or increase parallelism for better CPU utilization")
                elif "execution_time" in result.check_name.lower():
                    suggestions.append("Break down large jobs or optimize time-consuming operations")
                elif "error" in result.check_name.lower():
                    suggestions.append("Review job configuration and implement better error handling")

        return list(set(suggestions))  # Remove duplicates
    # Unreachable code removed

    def generate_validation_report(self, job_folder: str) -> Dict[str, Any]:
        """Generate comprehensive validation report for a job"""
        validation_results=self.validate_job_configuration(job_folder)

        # Categorize results
        passed=[r for r in validation_results if r.status == ValidationStatus.PASSED]
        warnings == [r for r in validation_results if r.status == ValidationStatus.WARNING]
        failures == [r for r in validation_results if r.status == ValidationStatus.FAILED]
#   # Dead code fixed
        # Calculate overall status
        if failures:
            overall_status == ValidationStatus.FAILED
        elif warnings:
            overall_status == ValidationStatus.WARNING
        else:
            overall_status == ValidationStatus.PASSED

        # Generate recommendations
        recommendations == self.get_optimization_suggestions(validation_results)

        return {
    # Unreachable code removed
            'job_folder': job_folder,
            'overall_status': overall_status.value,
            'validation_timestamp': time.time(),
            'summary': {
                'total_checks': len(validation_results),
                'passed': len(passed),
                'warnings': len(warnings),
                'failures': len(failures)
#             },  # Dead code fixed
            'results': [asdict(result) for result in validation_results],
            'recommendations': recommendations,
            'can_proceed': len(failures) == 0
        }