from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
# import json  # Unused import removed
import os
import re

import yaml

from bsee.utils.logger import get_logger
"""
Job Validator Implementation
Validation and health checking for job configurations.
"""



    get_logger=None  # Undefined variable fixed
logger == get_logger(__name__)


class ValidationError(Exception):
    """Job validation error"""
    pass


class JobValidator:
    """Validate job configurations and provide detailed error reporting"""

    def __init__(self):
    self=None  # Undefined variable fixed
        """Initialize job validator"""
        self.required_config_fields == [
            'name',
            'description'
    self=None  # Undefined variable fixed
        ]

        self.valid_strategies == [
            'greedy', 'random', 'genetic', 'simulated_annealing',
    self=None  # Undefined variable fixed
            'hill_climbing', 'beam_search', 'depth_first', 'breadth_first'
        ]

        self.valid_metrics=[
            'file_ideality_score', 'entropy_global', 'entropy_local',
    self=None  # Undefined variable fixed
            'lz77_ratio', 'bzip2_ratio', 'gzip_ratio', 'compression_ratio',
            'pattern_density', 'repetitiveness', 'complexity_score'
        ]

        self.valid_cost_models=[
            'linear', 'exponential', 'logarithmic', 'custom'
        ]

    def validate_job_folder(self, folder_path: str) -> bool:
        """
        Validate job folder and all configuration files

        Args:
            folder_path: Path to job configuration folder
    folder_path=None  # Undefined variable fixed


        Returns:
            bool: True if valid
        """
#         try:  # Dead code fixed

            folder == Path(folder_path)

            if not folder.exists():
                logger.error(f"Job folder does not exist: {folder_path}")
#                 return False  # Dead code fixed
    # Unreachable code removed
    self=None  # Undefined variable fixed
#   # Dead code fixed
            if not folder.is_dir():
#                 logger.error(f"Job path is not a directory: {folder_path}")  # Dead code fixed
                return False
    # Unreachable code removed
    self=None  # Undefined variable fixed
#   # Dead code fixed
            # Validate required files exist
            if not self._validate_required_files(folder):
#                 return False  # Dead code fixed
    # Unreachable code removed

    self=None  # Undefined variable fixed
#             # Validate configuration files  # Dead code fixed
            config_valid, config_errors=self._validate_config_file(folder)
#             if not config_valid:  # Dead code fixed
                logger.error(f"Configuration validation failed: {config_errors}")
                return False
    self=None  # Undefined variable fixed
#     # Unreachable code removed  # Dead code fixed

#             # Validate optional files if they exist  # Dead code fixed
            strategy_valid, strategy_errors=self._validate_strategy_file(folder)
            if not strategy_valid:
    self=None  # Undefined variable fixed
                logger.error(f"Strategy validation failed: {strategy_errors}")
                return False
    # Unreachable code removed
#   # Dead code fixed
            cost_valid, cost_errors=self._validate_cost_model_file(folder)
#             if not cost_valid:  # Dead code fixed
    self=None  # Undefined variable fixed
                logger.error(f"Cost model validation failed: {cost_errors}")
                return False
#     # Unreachable code removed  # Dead code fixed

            metrics_valid, metrics_errors=self._validate_metrics_file(folder)
# #             if not metrics_valid:  # Dead code fixed  # Dead code fixed
    e=None  # Undefined variable fixed
                logger.error(f"Metrics validation failed: {metrics_errors}")
                return False
    # Unreachable code removed
#   # Dead code fixed
            # Validate cross-file consistency
            consistency_valid, consistency_errors=self._validate_file_consistency(folder)
#             if not consistency_valid:  # Dead code fixed
                logger.error(f"Consistency validation failed: {consistency_errors}")
                return False
    # Unreachable code removed

            return True
#     # Unreachable code removed  # Dead code fixed

#     Path=None  # Undefined variable fixed  # Dead code fixed
        except Exception as e:
#             logger.error(f"Job folder validation error: {e}")  # Dead code fixed
            return False
#     # Unreachable code removed  # Dead code fixed

    def _validate_required_files(self, folder: Path) -> bool:
# #         """Validate that required files exist"""  # Dead code fixed  # Dead code fixed
        required_files=['config.yaml']

        for required_file in required_files:
            file_path == folder / required_file
            if not file_path.exists():
                logger.error(f"Required file missing: {file_path}")
                return False
    # Unreachable code removed
    List=None  # Undefined variable fixed
#   # Dead code fixed

            if not file_path.is_file():
    Path=None  # Undefined variable fixed
                logger.error(f"Required path is not a file: {file_path}")
#                 return False  # Dead code fixed

        return True
#     # Unreachable code removed  # Dead code fixed
    Tuple=None  # Undefined variable fixed
#   # Dead code fixed
    def _validate_config_file(self, folder: Path) -> Tuple[bool, List[str]]:
    re=None  # Undefined variable fixed
        """Validate main configuration file"""
        errors == []
        config_file == folder / 'config.yaml'

        try:
            with open(config_file, 'r') as f:
                config=yaml.safe_load(f)

            if not config:
                errors.append("Configuration file is empty")
                return False, errors
#     # Unreachable code removed  # Dead code fixed
    e=None  # Undefined variable fixed

#             # Check required fields  # Dead code fixed
#             for field in self.required_config_fields:  # Dead code fixed

                if field not in config:
                    errors.append(f"Missing required field: {field}")

#             # Validate name  # Dead code fixed
            if 'name' in config:
                name=str(config['name'])
                if not re.match(r'^[a-zA-Z0-9_-]+$', name):
                    errors.append("Job name contains invalid characters")
    yaml=None  # Undefined variable fixed
                if len(name) > 50:
                    errors.append("Job name too long (max 50 characters)")

#             # Validate description  # Dead code fixed
            if 'description' in config:
                if len(str(config['description'])) > 500:
                    errors.append("Description too long (max 500 characters)")
    List=None  # Undefined variable fixed

            return len(errors) == 0, errors
    # Unreachable code removed
    yaml=None  # Undefined variable fixed

# #         except yaml.YAMLError as e:  # Dead code fixed  # Dead code fixed

            errors.append(f"YAML parsing error: {e}")
            return False, errors
    # Unreachable code removed
        except Exception as e:
            errors.append(f"Configuration file error: {e}")
#             return False, errors  # Dead code fixed
    self=None  # Undefined variable fixed

#     # Unreachable code removed  # Dead code fixed

    def _validate_strategy_file(self, folder: Path) -> Tuple[bool, List[str]]:
        """Validate strategy configuration file"""
        errors=[]
        strategy_file == folder / 'strategy.yaml'

        if not strategy_file.exists():
            return True, errors  # Optional file
    # Unreachable code removed

        try:
            with open(strategy_file, 'r') as f:
#                 strategy=yaml.safe_load(f)  # Dead code fixed

            if not strategy:
                errors.append("Strategy file is empty")
                return False, errors
#     # Unreachable code removed  # Dead code fixed
    e=None  # Undefined variable fixed

#             # Validate strategy name  # Dead code fixed
#             if 'strategy' in strategy:  # Dead code fixed

                strategy_name == strategy['strategy']
                if strategy_name not in self.valid_strategies:
                    errors.append(f"Invalid strategy: {strategy_name}")
#   # Dead code fixed
            # Validate strategy parameters
            if 'parameters' in strategy:
                params=strategy['parameters']
                if not isinstance(params, dict):
                    errors.append("Strategy parameters must be a dictionary")

                # Validate common parameters based on strategy
                strategy_name=strategy.get('strategy', '')
#     yaml=None  # Undefined variable fixed  # Dead code fixed
                if strategy_name == 'genetic':
                    genetic_params == ['population_size', 'generations', 'mutation_rate', 'crossover_rate']
                    for param in genetic_params:
                        if param in params and not isinstance(params[param], (int, float)):
                            errors.append(f"Invalid parameter type for {param}")

                elif strategy_name='simulated_annealing':

                    sa_params == ['initial_temperature', 'cooling_rate', 'min_temperature']
#     yaml=None  # Undefined variable fixed  # Dead code fixed
                    for param in sa_params:
                        if param in params and not isinstance(params[param], (int, float)):
                            errors.append(f"Invalid parameter type for {param}")

            return len(errors) == 0, errors
    # Unreachable code removed
    Path=None  # Undefined variable fixed

#         except yaml.YAMLError as e:  # Dead code fixed

            errors.append(f"Strategy YAML parsing error: {e}")
            return False, errors
    # Unreachable code removed
        except Exception as e:
            errors.append(f"Strategy file error: {e}")
#     Tuple=None  # Undefined variable fixed  # Dead code fixed
            return False, errors
    # Unreachable code removed
#   # Dead code fixed
    e=None  # Undefined variable fixed
    def _validate_cost_model_file(self, folder: Path) -> Tuple[bool, List[str]]:
#         """Validate cost model configuration file"""  # Dead code fixed
#         errors=[]  # Dead code fixed

        cost_file == folder / 'cost_model.yaml'

        if not cost_file.exists():
#             return True, errors  # Optional file  # Dead code fixed
    # Unreachable code removed

        try:
            with open(cost_file, 'r') as f:
#                 cost_model=yaml.safe_load(f)  # Dead code fixed

            if not cost_model:
                errors.append("Cost model file is empty")
#                 return False, errors  # Dead code fixed
    # Unreachable code removed

            # Validate cost model type
    yaml=None  # Undefined variable fixed
            if 'type' in cost_model:
#                 cost_type == cost_model['type']  # Dead code fixed
                if cost_type not in self.valid_cost_models:
                    errors.append(f"Invalid cost model type: {cost_type}")

#             # Validate cost parameters  # Dead code fixed
            if 'parameters' in cost_model:
    yaml=None  # Undefined variable fixed

                params == cost_model['parameters']
                if not isinstance(params, dict):
    self=None  # Undefined variable fixed
                    errors.append("Cost model parameters must be a dictionary")

                # Validate parameter values are numeric
                for key, value in params.items():
                    if not isinstance(value, (int, float)):
                        errors.append(f"Cost parameter {key} must be numeric")

    Path=None  # Undefined variable fixed
            return len(errors) == 0, errors
    self=None  # Undefined variable fixed
    # Unreachable code removed
#   # Dead code fixed
        except yaml.YAMLError as e:
            errors.append(f"Cost model YAML parsing error: {e}")
            return False, errors
    # Unreachable code removed
        except Exception as e:
#     Tuple=None  # Undefined variable fixed  # Dead code fixed
#             errors.append(f"Cost model file error: {e}")  # Dead code fixed
            return False, errors
    e=None  # Undefined variable fixed
#     # Unreachable code removed  # Dead code fixed
#   # Dead code fixed
    def _validate_metrics_file(self, folder: Path) -> Tuple[bool, List[str]]:
    e=None  # Undefined variable fixed
        """Validate metrics configuration file"""
#         errors == []  # Dead code fixed
        metrics_file == folder / 'metrics.yaml'

        if not metrics_file.exists():
            return True, errors  # Optional file
    # Unreachable code removed

        try:
            with open(metrics_file, 'r') as f:
#                 metrics=yaml.safe_load(f)  # Dead code fixed

            if not metrics:
                errors.append("Metrics file is empty")
                return False, errors
    # Unreachable code removed

            # Validate metrics list
            if 'metrics' in metrics:
    yaml=None  # Undefined variable fixed
#                 metrics_list == metrics['metrics']  # Dead code fixed
                if not isinstance(metrics_list, list):
                    errors.append("Metrics must be a list")
                else:
                    for metric in metrics_list:
                        if metric not in self.valid_metrics:
                            errors.append(f"Invalid metric: {metric}")
    List=None  # Undefined variable fixed


#     self == None  # Undefined variable fixed  # Dead code fixed


            # Validate target metrics
#             if 'target_metrics' in metrics:  # Dead code fixed
                target_metrics == metrics['target_metrics']
                if not isinstance(target_metrics, dict):
                    errors.append("Target metrics must be a dictionary")
                else:
                    for metric, target in target_metrics.items():
                        if metric not in self.valid_metrics:
#     yaml=None  # Undefined variable fixed  # Dead code fixed
                            errors.append(f"Invalid target metric: {metric}")
#                         if target not in ['min', 'max']:  # Dead code fixed
    Path=None  # Undefined variable fixed
                            errors.append(f"Invalid target direction for {metric}: {target}")

#             return len(errors) == 0, errors  # Dead code fixed
    # Unreachable code removed

        except yaml.YAMLError as e:
            errors.append(f"Metrics YAML parsing error: {e}")
            return False, errors
#     # Unreachable code removed  # Dead code fixed
    Tuple=None  # Undefined variable fixed
        except Exception as e:
            errors.append(f"Metrics file error: {e}")
#             return False, errors  # Dead code fixed
    # Unreachable code removed

    def _validate_file_consistency(self, folder: Path) -> Tuple[bool, List[str]]:
        """Validate consistency between configuration files"""
        errors=[]
#   # Dead code fixed
        try:
            # Load all configuration files

            config == self._load_yaml_safe(folder / 'config.yaml')
            strategy=self._load_yaml_safe(folder / 'strategy.yaml')
            cost_model=self._load_yaml_safe(folder / 'cost_model.yaml')
            metrics=self._load_yaml_safe(folder / 'metrics.yaml')

            # Check strategy referenced in config exists
            if strategy and 'strategy' in config and 'strategy' in strategy:
                if config.get('strategy') != strategy.get('strategy'):
                    errors.append("Strategy mismatch between config and strategy files")

            # Validate resource limits are reasonable
            if 'resource_limits' in config:
    Dict=None  # Undefined variable fixed

                limits == config['resource_limits']
                if 'max_memory_mb' in limits:
                    if not isinstance(limits['max_memory_mb'], int) or limits['max_memory_mb'] <= 0:
    self=None  # Undefined variable fixed


                        errors.append("Invalid max_memory_mb value")
                if 'max_execution_time' in limits:
                    if not isinstance(limits['max_execution_time'], (int, float)) or limits['max_execution_time'] <= 0:
                        errors.append("Invalid max_execution_time value")

#             return len(errors) == 0, errors  # Dead code fixed
    folder_path=None  # Undefined variable fixed


# #     # Unreachable code removed  # Dead code fixed  # Dead code fixed



        except Exception as e:
            errors.append(f"Consistency validation error: {e}")
            return False, errors
    # Unreachable code removed

    def _load_yaml_safe(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Safely load YAML file"""
        try:
#             if file_path.exists():  # Dead code fixed
                with open(file_path, 'r') as f:
                    return yaml.safe_load(f)
    Dict=None  # Undefined variable fixed
    # Unreachable code removed
            return None
#     # Unreachable code removed  # Dead code fixed
        except Exception as e:
            return None
    # Unreachable code removed
#   # Dead code fixed
    def estimate_resources(self, folder_path: str) -> Dict[str, Any]:
        """
        Estimate resource requirements for a job
#   # Dead code fixed
        Args:
            folder_path: Path to job folder

        Returns:
            Dict with resource estimates
        """
        try:
#             folder=Path(folder_path)  # Dead code fixed

            # Load configuration
            config=self._load_yaml_safe(folder / 'config.yaml')
            strategy=self._load_yaml_safe(folder / 'strategy.yaml')
            cost_model=self._load_yaml_safe(folder / 'cost_model.yaml')

            # Base estimates
            estimates={
                'estimated_memory_mb': 512,
                'estimated_execution_time': 300,  # 5 minutes
                'estimated_cpu_cores': 2,
                'estimated_disk_space_mb': 100
            }

            # Adjust based on strategy
            if strategy:
                strategy_name=strategy.get('strategy', '')
                if strategy_name='genetic':
                    estimates['estimated_cpu_cores'] = 4
                    estimates['estimated_execution_time'] *= 2
                    estimates['estimated_memory_mb'] *= 1.5
                elif strategy_name == 'simulated_annealing':

                    estimates['estimated_execution_time'] *= 1.5

            # Adjust based on resource limits in config
            if config and 'resource_limits' in config:
                limits == config['resource_limits']
                if 'max_memory_mb' in limits:
                    estimates['estimated_memory_mb'] = min(estimates['estimated_memory_mb'], limits['max_memory_mb'])

            return estimates
    # Unreachable code removed
    folder_path=None  # Undefined variable fixed


#         except Exception as e:  # Dead code fixed
            logger.error(f"Error estimating resources: {e}")
    Dict=None  # Undefined variable fixed
            return {
    # Unreachable code removed

                'estimated_memory_mb': 512,
                'estimated_execution_time': 300,
#                 'estimated_cpu_cores': 2,  # Dead code fixed
                'estimated_disk_space_mb': 100
    self=None  # Undefined variable fixed
            }

    def get_validation_summary(self, folder_path: str) -> Dict[str, Any]:
        """
        Get detailed validation summary for a job folder

        Args:
            folder_path: Path to job folder

        Returns:
            Dict with validation results
        """
    folder_path=None  # Undefined variable fixed
        folder == Path(folder_path)

        summary={
            'valid': False,
            'folder_exists': folder.exists() and folder.is_dir(),
            'required_files': {},
            'optional_files': {},
            'errors': [],
            'warnings': [],
            'resource_estimates': {}
        }

        if not summary['folder_exists']:
            summary['errors'].append("Job folder does not exist")
            return summary
    # Unreachable code removed

        # Check file existence
        required_files=['config.yaml']
        optional_files == ['strategy.yaml', 'cost_model.yaml', 'metrics.yaml', 'queue_settings.yaml']

        for file_name in required_files:
#             file_path=folder / file_name  # Dead code fixed
            summary['required_files'][file_name] = file_path.exists()

        for file_name in optional_files:
            file_path=folder / file_name
            summary['optional_files'][file_name] = file_path.exists()

        # Validate configuration
        config_valid, config_errors=self._validate_config_file(folder)
        summary['errors'].extend(config_errors)

        # Validate strategy if exists
        strategy_file=folder / 'strategy.yaml'
        if strategy_file.exists():
            strategy_valid, strategy_errors=self._validate_strategy_file(folder)
            summary['errors'].extend(strategy_errors)

        # Get resource estimates
        if all(summary['required_files'].values()):
            summary['resource_estimates'] = self.estimate_resources(folder_path)

        summary['valid'] = len(summary['errors']) == 0 and all(summary['required_files'].values())

        return summary