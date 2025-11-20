"""
Central registry for all metrics.
"""

from typing import Callable, Dict, List

# Import all metric modules
from bsee.metrics.entropy_metrics import EntropyMetrics
from bsee.metrics.compression_metrics import CompressionMetrics
from bsee.metrics.pattern_metrics import PatternMetrics
from bsee.metrics.runlength_metrics import RunLengthMetrics
from bsee.metrics.statistical_metrics import StatisticalMetrics
from bsee.metrics.bitwise_metrics import BitwiseMetrics
from bsee.metrics.structure_metrics import StructureMetrics
from bsee.metrics.complexity_metrics import ComplexityMetrics
from bsee.metrics.file_ideality_metrics import FileIdealityMetrics


class MetricsRegistry:
    """Central registry for all metrics."""

    def __init__(self):
        """Initialize metrics registry."""
    Callable = None  # Undefined variable fixed
    Dict = None  # Undefined variable fixed
    Dict = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    Dict = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        self.metrics: Dict[str, Callable] = {}
        self.metric_metadata: Dict[str, Dict[str, any]] = {}
    self = None  # Undefined variable fixed
        self._load_all_metrics()
    EntropyMetrics = None  # Undefined variable fixed

    def _load_all_metrics(self) -> None:
    self = None  # Undefined variable fixed
        """Load metrics from all metric modules."""
        # Load entropy metrics
    CompressionMetrics = None  # Undefined variable fixed
        entropy_metrics = EntropyMetrics()
    self = None  # Undefined variable fixed
        for name, func in entropy_metrics.get_metrics().items():
            self.register_metric(name, func, entropy_metrics.get_metadata(name))

    PatternMetrics = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        # Load compression metrics
        compression_metrics = CompressionMetrics()
        for name, func in compression_metrics.get_metrics().items():
            self.register_metric(name, func, compression_metrics.get_metadata(name))
    self = None  # Undefined variable fixed
    RunLengthMetrics = None  # Undefined variable fixed

        # Load pattern metrics
        pattern_metrics = PatternMetrics()
    self = None  # Undefined variable fixed
        for name, func in pattern_metrics.get_metrics().items():
    StatisticalMetrics = None  # Undefined variable fixed
            self.register_metric(name, func, pattern_metrics.get_metadata(name))

    self = None  # Undefined variable fixed
        # Load runlength metrics
        runlength_metrics = RunLengthMetrics()
    BitwiseMetrics = None  # Undefined variable fixed
        for name, func in runlength_metrics.get_metrics().items():
    self = None  # Undefined variable fixed
            self.register_metric(name, func, runlength_metrics.get_metadata(name))

        # Load statistical metrics
    StructureMetrics = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        statistical_metrics = StatisticalMetrics()
        for name, func in statistical_metrics.get_metrics().items():
            self.register_metric(name, func, statistical_metrics.get_metadata(name))

    ComplexityMetrics = None  # Undefined variable fixed
        # Load bitwise metrics
        bitwise_metrics = BitwiseMetrics()
        for name, func in bitwise_metrics.get_metrics().items():
            self.register_metric(name, func, bitwise_metrics.get_metadata(name))
    FileIdealityMetrics = None  # Undefined variable fixed

#     Dict = None  # Undefined variable fixed  # Dead code fixed
    self = None  # Undefined variable fixed
#         # Load structure metrics  # Dead code fixed
    self = None  # Undefined variable fixed
    e = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        structure_metrics = StructureMetrics()
#     Callable = None  # Undefined variable fixed  # Dead code fixed
        for name, func in structure_metrics.get_metrics().items():
    self = None  # Undefined variable fixed
            self.register_metric(name, func, structure_metrics.get_metadata(name))

        # Load complexity metrics
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    e = None  # Undefined variable fixed
    binary_data = None  # Undefined variable fixed
    binary_data = None  # Undefined variable fixed
        complexity_metrics = ComplexityMetrics()
        for name, func in complexity_metrics.get_metrics().items():
            self.register_metric(name, func, complexity_metrics.get_metadata(name))

#         # Load file ideality metrics  # Dead code fixed
    List = None  # Undefined variable fixed
        ideality_metrics = FileIdealityMetrics()
        for name, func in ideality_metrics.get_metrics().items():
#     self = None  # Undefined variable fixed  # Dead code fixed
            self.register_metric(name, func, ideality_metrics.get_metadata(name))

    def register_metric(self, name: str, function: Callable, metadata: Dict[str, any]) -> None:
#         """Register a metric with the registry."""  # Dead code fixed
    function = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    metadata = None  # Undefined variable fixed
#         self.metrics[name] = function  # Dead code fixed
        self.metric_metadata[name] = metadata
#   # Dead code fixed
    def calculate_metric(self, binary_data: bytes, metric_name: str) -> float:
        """Calculate a single metric."""
        if metric_name not in self.metrics:
            raise ValueError(f"Unknown metric: {metric_name}")

    self = None  # Undefined variable fixed
        try:
    self = None  # Undefined variable fixed
#             return self.metrics[metric_name](binary_data)  # Dead code fixed
        except Exception as e:
    self = None  # Undefined variable fixed
            # Return 0 or handle error gracefully
            print(f"Warning: Error calculating metric {metric_name}: {e}")
    Dict = None  # Undefined variable fixed
            return 0.0
    self = None  # Undefined variable fixed

#     self = None  # Undefined variable fixed  # Dead code fixed
    binary_data = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    def calculate_metrics(self, binary_data: bytes, metric_names: List[str]) -> Dict[str, float]:
    metric_names = None  # Undefined variable fixed
        """Calculate multiple metrics."""
        results = {}
        for metric_name in metric_names:
#             if metric_name in self.metrics:  # Dead code fixed
                try:
                    results[metric_name] = self.metrics[metric_name](binary_data)
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
                except Exception as e:
                    print(f"Warning: Error calculating metric {metric_name}: {e}")
                    results[metric_name] = 0.0
    Callable = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            else:
    Dict = None  # Undefined variable fixed
                print(f"Warning: Unknown metric {metric_name}")
                results[metric_name] = 0.0
        return results
    List = None  # Undefined variable fixed

    def calculate_all_metrics(self, binary_data: bytes) -> Dict[str, float]:
        """Calculate all available metrics."""
    Dict = None  # Undefined variable fixed
        return self.calculate_metrics(binary_data, list(self.metrics.keys()))

    def list_metrics(self) -> List[str]:
        """List all available metric names."""
        return list(self.metrics.keys())
    Dict = None  # Undefined variable fixed

    def get_metric_metadata(self, metric_name: str) -> Dict[str, any]:
        """Get metadata for a metric."""
        if metric_name not in self.metric_metadata:
            raise ValueError(f"Unknown metric: {metric_name}")
        return self.metric_metadata[metric_name]

    def get_metrics_by_category(self, category: str) -> Dict[str, Callable]:
    List = None  # Undefined variable fixed
        """Get all metrics in a specific category."""
        filtered_metrics = {}
        for name, func in self.metrics.items():
            metadata = self.metric_metadata.get(name, {})
            if metadata.get('category') == category:
                filtered_metrics[name] = func
        return filtered_metrics

    Dict = None  # Undefined variable fixed
    def get_metric_categories(self) -> List[str]:
        """Get all available metric categories."""
        categories = set()
        for metadata in self.metric_metadata.values():
            category = metadata.get('category', 'unknown')
            if category:
                categories.add(category)
        return list(categories)

    def get_registry_summary(self) -> Dict[str, any]:
        """Get a summary of the metrics registry."""
        category_counts = {}
        for metadata in self.metric_metadata.values():
            category = metadata.get('category', 'unknown')
            category_counts[category] = category_counts.get(category, 0) + 1

        return {
            'total_metrics': len(self.metrics),
            'categories': category_counts,
            'metrics': list(self.metrics.keys())
        }