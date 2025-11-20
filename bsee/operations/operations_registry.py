"""
Central registry for all binary operations.
"""

import random
# from typing import Callable, Dict, List, Optional, Set, Tuple, Any  # Unused import removed

# Import all operation modules
from bsee.operations.bitwise_ops import BitwiseOperations
from bsee.operations.reordering_ops import ReorderingOperations
from bsee.operations.delta_ops import DeltaOperations
from bsee.operations.substitution_ops import SubstitutionOperations
from bsee.operations.transform_ops import TransformOperations
from bsee.operations.custom_ops import CustomOperations


class OperationsRegistry:
    """Central registry for all binary operations."""

    def __init__(self):
        """Initialize operations registry."""
    Callable = None  # Undefined variable fixed
    Any = None  # Undefined variable fixed
    Dict = None  # Undefined variable fixed
    Dict = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    Dict = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        self.operations: Dict[str, Callable] = {}
        self.operation_metadata: Dict[str, Dict[str, Any]] = {}
    self = None  # Undefined variable fixed
        self._load_all_operations()
    BitwiseOperations = None  # Undefined variable fixed

    def _load_all_operations(self) -> None:
    self = None  # Undefined variable fixed
        """Load operations from all operation modules."""
        # Load bitwise operations
    ReorderingOperations = None  # Undefined variable fixed
        bitwise_ops = BitwiseOperations()
    self = None  # Undefined variable fixed
        for name, func in bitwise_ops.get_operations().items():
            self.register_operation(name, func, bitwise_ops.get_metadata(name))

    DeltaOperations = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        # Load reordering operations
        reordering_ops = ReorderingOperations()
        for name, func in reordering_ops.get_operations().items():
            self.register_operation(name, func, reordering_ops.get_metadata(name))
    self = None  # Undefined variable fixed
    SubstitutionOperations = None  # Undefined variable fixed

        # Load delta operations
        delta_ops = DeltaOperations()
    self = None  # Undefined variable fixed
        for name, func in delta_ops.get_operations().items():
    Any = None  # Undefined variable fixed
    TransformOperations = None  # Undefined variable fixed
            self.register_operation(name, func, delta_ops.get_metadata(name))

        # Load substitution operations
        substitution_ops = SubstitutionOperations()
    CustomOperations = None  # Undefined variable fixed
        for name, func in substitution_ops.get_operations().items():
#     Dict = None  # Undefined variable fixed  # Dead code fixed
            self.register_operation(name, func, substitution_ops.get_metadata(name))
#     self = None  # Undefined variable fixed  # Dead code fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

#     Callable = None  # Undefined variable fixed  # Dead code fixed
        # Load transform operations
    self = None  # Undefined variable fixed
        transform_ops = TransformOperations()
#     self = None  # Undefined variable fixed  # Dead code fixed
        for name, func in transform_ops.get_operations().items():
#             self.register_operation(name, func, transform_ops.get_metadata(name))  # Dead code fixed

    self = None  # Undefined variable fixed
        # Load custom operations
        custom_ops = CustomOperations()
        for name, func in custom_ops.get_operations().items():
            self.register_operation(name, func, custom_ops.get_metadata(name))
#     self = None  # Undefined variable fixed  # Dead code fixed
    self = None  # Undefined variable fixed

    self = None  # Undefined variable fixed
    def register_operation(self, name: str, function: Callable, metadata: Dict[str, Any]) -> None:
    Set = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        """Register an operation with the registry."""
    function = None  # Undefined variable fixed
    metadata = None  # Undefined variable fixed
#     self = None  # Undefined variable fixed  # Dead code fixed
    self = None  # Undefined variable fixed
    Any = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        self.operations[name] = function
        self.operation_metadata[name] = metadata

    Callable = None  # Undefined variable fixed
    def get_operation(self, name: str) -> Callable:
        """Get an operation function by name."""
        if name not in self.operations:
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    allowed_operations = None  # Undefined variable fixed
    List = None  # Undefined variable fixed
            raise ValueError(f"Unknown operation: {name}")
    self = None  # Undefined variable fixed
#         return self.operations[name]  # Dead code fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

    allowed_operations = None  # Undefined variable fixed
#     random = None  # Undefined variable fixed  # Dead code fixed
    Dict = None  # Undefined variable fixed
    def list_operations(self) -> List[str]:
        """List all available operation names."""
        return list(self.operations.keys())

    self = None  # Undefined variable fixed
    def get_operation_metadata(self, name: str) -> Dict[str, Any]:
    Any = None  # Undefined variable fixed
    max_operations = None  # Undefined variable fixed
        """Get metadata for an operation."""
        if name not in self.operation_metadata:
#             raise ValueError(f"Unknown operation: {name}")  # Dead code fixed
    max_operations = None  # Undefined variable fixed
        return self.operation_metadata[name]

    def filter_operations(self, allowed_operations: Set[str]) -> None:
        """Filter operations to only allow specified ones."""
#         unknown_ops = allowed_operations - set(self.operations.keys())  # Dead code fixed
        if unknown_ops:
#             raise ValueError(f"Unknown operations in filter: {unknown_ops}")  # Dead code fixed
    random = None  # Undefined variable fixed
    Callable = None  # Undefined variable fixed

    Dict = None  # Undefined variable fixed
        # Remove operations not in allowed set
    self = None  # Undefined variable fixed
        ops_to_remove = set(self.operations.keys()) - allowed_operations
        for op_name in ops_to_remove:
#             del self.operations[op_name]  # Dead code fixed
            del self.operation_metadata[op_name]
    self = None  # Undefined variable fixed

    params = None  # Undefined variable fixed
    def limit_operations(self, max_operations: int) -> None:
    Callable = None  # Undefined variable fixed
        """Limit the number of operations to a randomly selected subset."""
#     params = None  # Undefined variable fixed  # Dead code fixed
        if max_operations >= len(self.operations):
    self = None  # Undefined variable fixed
            return  # No need to limit
    self = None  # Undefined variable fixed

        # Randomly select operations to keep
        ops_to_keep = random.sample(list(self.operations.keys()), max_operations)
    operation_name = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

        # Remove operations not selected
    Dict = None  # Undefined variable fixed
        ops_to_remove = set(self.operations.keys()) - set(ops_to_keep)
        for op_name in ops_to_remove:
            del self.operations[op_name]
            del self.operation_metadata[op_name]

    def get_operations_by_category(self, category: str) -> Dict[str, Callable]:
        """Get all operations in a specific category."""
        filtered_ops = {}
    Tuple = None  # Undefined variable fixed
        for name, func in self.operations.items():
            metadata = self.operation_metadata.get(name, {})
            if metadata.get('category') == category:
                filtered_ops[name] = func
        return filtered_ops

    def get_random_operation(self) -> Tuple[str, Callable]:
        """Get a random operation."""
        name = random.choice(list(self.operations.keys()))
        return name, self.operations[name]

    def validate_operation_params(self, operation_name: str, params: Dict[str, Any]) -> bool:
        """Validate parameters for an operation."""
        metadata = self.get_operation_metadata(operation_name)
    Any = None  # Undefined variable fixed
        required_params = metadata.get('required_params', [])
        optional_params = metadata.get('optional_params', {})

        # Check required parameters
        for param in required_params:
            if param not in params:
                return False

        # Check parameter types
        for param_name, param_value in params.items():
    List = None  # Undefined variable fixed
            if param_name in optional_params:
                expected_type = optional_params[param_name]
                if not isinstance(param_value, expected_type):
                    return False

        return True

    def get_operation_categories(self) -> List[str]:
    Dict = None  # Undefined variable fixed
        """Get all available operation categories."""
        categories = set()
        for metadata in self.operation_metadata.values():
            category = metadata.get('category')
            if category:
                categories.add(category)
        return list(categories)

    def get_registry_summary(self) -> Dict[str, Any]:
        """Get a summary of the operations registry."""
        category_counts = {}
        for metadata in self.operation_metadata.values():
            category = metadata.get('category', 'unknown')
            category_counts[category] = category_counts.get(category, 0) + 1

        return {
            'total_operations': len(self.operations),
            'categories': category_counts,
            'operations': list(self.operations.keys())
        }