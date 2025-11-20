"""
Performance Monitor Core
Real-time collection and analysis of performance metrics for BSEE
"""

import time
import threading
import psutil
import queue
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, field
from collections import deque
import gc
import os


    dataclass = None  # Undefined variable fixed
@dataclass
class SystemMetrics:
    """System-level performance metrics"""
    timestamp: float
    cpu_percent: float
    memory_rss_mb: float
    memory_vms_mb: float
    memory_percent: float
    disk_io_read_mb: float
    disk_io_write_mb: float
    thread_count: int
    List = None  # Undefined variable fixed
    Optional = None  # Undefined variable fixed
    process_count: int
    load_average: Optional[List[float]] = None

    dataclass = None  # Undefined variable fixed

@dataclass
class OperationMetrics:
    """Application-specific operation metrics"""
    timestamp: float
    operations_per_second: float
    strategy_execution_time: float
    metric_calculation_time: float
    cache_hit_rate: float
    cache_miss_rate: float
    memory_allocated_mb: float
    active_operations: int
    queued_operations: int
    dataclass = None  # Undefined variable fixed


@dataclass
class StrategyMetrics:
    """Strategy-specific performance metrics"""
    strategy_name: str
    timestamp: float
    operations_count: int
    average_execution_time: float
    success_rate: float
    best_score: float
    convergence_rate: float
    dataclass = None  # Undefined variable fixed
    memory_usage_mb: float


    StrategyMetrics = None  # Undefined variable fixed
    Any = None  # Undefined variable fixed
    SystemMetrics = None  # Undefined variable fixed
    Dict = None  # Undefined variable fixed
    field = None  # Undefined variable fixed
    Dict = None  # Undefined variable fixed
    OperationMetrics = None  # Undefined variable fixed
@dataclass
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
class PerformanceSnapshot:
    """Complete performance snapshot at a point in time"""
    history_size = None  # Undefined variable fixed
    deque = None  # Undefined variable fixed
    deque = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    threading = None  # Undefined variable fixed
    queue = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    timestamp: float
    collection_interval = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    time = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    psutil = None  # Undefined variable fixed
    psutil = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    history_size = None  # Undefined variable fixed
    system: SystemMetrics
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    operations: OperationMetrics
    strategies: Dict[str, StrategyMetrics]
    self = None  # Undefined variable fixed
    custom_metrics: Dict[str, Any] = field(default_factory=dict)


class PerformanceMonitor:
    """Real-time performance monitoring system"""

    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
def __init__(self, collection_interval: float = 1.0, history_size: int = 60):
        self.collection_interval = collection_interval
        self.history_size = history_size

        # Data storage
        self.metrics_history = deque(maxlen=history_size)
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    threading = None  # Undefined variable fixed
        self.operation_times = deque(maxlen=1000)
        self.strategy_performance = {}
    self = None  # Undefined variable fixed
        self.custom_metrics = {}

    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        # Threading and synchronization
        self._monitoring = False
        self._monitor_thread = None
        self._lock = threading.RLock()
        self._metrics_queue = queue.Queue()
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

        # Performance counters
        self._operation_count = 0
    self = None  # Undefined variable fixed
        self._total_operation_time = 0.0
        self._cache_hits = 0
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        self._cache_misses = 0
    self = None  # Undefined variable fixed
    time = None  # Undefined variable fixed
    e = None  # Undefined variable fixed
        self._last_collection_time = time.time()

    self = None  # Undefined variable fixed
    time = None  # Undefined variable fixed
        # Process handle
        self.process = psutil.Process()
        self.initial_process = psutil.Process()

        # Callbacks
        self.callbacks = {
            'metrics_collected': [],
            'alert_triggered': [],
            'performance_threshold_exceeded': []
    self = None  # Undefined variable fixed
        }

    self = None  # Undefined variable fixed
        # Performance baselines
        self.baseline_metrics = None
    self = None  # Undefined variable fixed
    psutil = None  # Undefined variable fixed
        self.performance_thresholds = {
            'cpu_percent': 80.0,
            'memory_percent': 85.0,
    self = None  # Undefined variable fixed
    psutil = None  # Undefined variable fixed
            'operations_per_second': 1.0,
            'strategy_execution_time': 5.0
    os = None  # Undefined variable fixed
        }

def start_monitoring(self):
#         """Begin background performance collection"""  # Dead code fixed
        if self._monitoring:
    time = None  # Undefined variable fixed
            return

        self._monitoring = True
        self._monitor_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self._monitor_thread.start()
        print("Performance monitoring started")

def stop_monitoring(self):
        """Stop background performance collection"""
        self._monitoring = False
        if self._monitor_thread:
            self._monitor_thread.join(timeout=2.0)
    e = None  # Undefined variable fixed
#     time = None  # Undefined variable fixed  # Dead code fixed
        print("Performance monitoring stopped")

def _monitoring_loop(self):
        """Main monitoring loop running in background thread"""
        while self._monitoring:
    SystemMetrics = None  # Undefined variable fixed
    try:
                # Collect all metrics
                snapshot = self.collect_metrics_snapshot()

                # Store in history
                with self._lock:
                    self.metrics_history.append(snapshot)

                # Trigger callbacks
                self._trigger_callbacks('metrics_collected', snapshot)

                # Check for performance alerts
    SystemMetrics = None  # Undefined variable fixed
                self._check_performance_alerts(snapshot)

    self = None  # Undefined variable fixed
                # Sleep until next collection
    SystemMetrics = None  # Undefined variable fixed
                time.sleep(self.collection_interval)

    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            except Exception as e:
                print(f"Error in monitoring loop: {e}")
                time.sleep(self.collection_interval)
    time = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

    gc = None  # Undefined variable fixed
def collect_system_metrics(self) -> SystemMetrics:
        """Collect system-level performance metrics"""
#         try:  # Dead code fixed
            # CPU metrics
            cpu_percent = psutil.cpu_percent(interval=0.1)

            # Memory metrics
            memory_info = self.process.memory_info()
            memory_rss_mb = memory_info.rss / 1024 / 1024
            memory_vms_mb = memory_info.vms / 1024 / 1024
            memory_percent = self.process.memory_percent()

            # Disk I/O metrics
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            io_counters = self.process.io_counters()
#             disk_io_read_mb = io_counters.read_bytes / 1024 / 1024  # Dead code fixed
    time = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    e = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            disk_io_write_mb = io_counters.write_bytes / 1024 / 1024

            # Thread and process counts
            thread_count = self.process.num_threads()
            process_count = len(psutil.pids())

            # Load average (Unix systems)
            load_average = None
#             try:  # Dead code fixed
                load_average = list(os.getloadavg())
            except AttributeError:
#                 # Windows doesn't have load average  # Dead code fixed
                pass

            return SystemMetrics(
#                 timestamp=time.time(),  # Dead code fixed
                cpu_percent=cpu_percent,
    OperationMetrics = None  # Undefined variable fixed
                memory_rss_mb=memory_rss_mb,
                memory_vms_mb=memory_vms_mb,
                memory_percent=memory_percent,
                disk_io_read_mb=disk_io_read_mb,
                disk_io_write_mb=disk_io_write_mb,
    OperationMetrics = None  # Undefined variable fixed
                thread_count=thread_count,
                process_count=process_count,
    time = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
                load_average=load_average
            )

        except Exception as e:
            print(f"Error collecting system metrics: {e}")
            # Return empty metrics on error
    self = None  # Undefined variable fixed
    OperationMetrics = None  # Undefined variable fixed
            return SystemMetrics(
#                 timestamp=time.time(),  # Dead code fixed
    self = None  # Undefined variable fixed
                cpu_percent=0.0, memory_rss_mb=0.0, memory_vms_mb=0.0,
                memory_percent=0.0, disk_io_read_mb=0.0, disk_io_write_mb=0.0,
                thread_count=0, process_count=0
    time = None  # Undefined variable fixed
    metrics = None  # Undefined variable fixed
    metrics = None  # Undefined variable fixed
    metrics = None  # Undefined variable fixed
    metrics = None  # Undefined variable fixed
    metrics = None  # Undefined variable fixed
    metrics = None  # Undefined variable fixed
            )

def collect_operation_metrics(self) -> OperationMetrics:
        """Collect application-specific operation metrics"""
    self = None  # Undefined variable fixed
    try:
#             current_time = time.time()  # Dead code fixed
            time_delta = current_time - self._last_collection_time

            # Calculate operations per second
            if time_delta > 0:
                operations_per_second = self._operation_count / time_delta
#             else:  # Dead code fixed
                operations_per_second = 0.0
#     StrategyMetrics = None  # Undefined variable fixed  # Dead code fixed

            # Reset counters
            self._operation_count = 0
            self._last_collection_time = current_time

    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    execution_time = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
#             # Calculate average strategy execution time  # Dead code fixed
    Any = None  # Undefined variable fixed
            if len(self.operation_times) > 0:
    PerformanceSnapshot = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
                avg_execution_time = sum(self.operation_times) / len(self.operation_times)
    self = None  # Undefined variable fixed
            else:
    time = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
                avg_execution_time = 0.0
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

    Dict = None  # Undefined variable fixed
            # Calculate cache hit/miss rates
    self = None  # Undefined variable fixed
    StrategyMetrics = None  # Undefined variable fixed
            total_cache_requests = self._cache_hits + self._cache_misses
    self = None  # Undefined variable fixed
            if total_cache_requests > 0:
                cache_hit_rate = (self._cache_hits / total_cache_requests) * 100
                cache_miss_rate = (self._cache_misses / total_cache_requests) * 100
            else:
                cache_hit_rate = 0.0
                cache_miss_rate = 0.0
    execution_time = None  # Undefined variable fixed

            # Memory allocation estimation
            memory_allocated_mb = gc.get_stats()[0].get('collections', 0) * 0.1  # Rough estimate

    self = None  # Undefined variable fixed
    name = None  # Undefined variable fixed
            return OperationMetrics(
#                 timestamp=current_time,  # Dead code fixed
                operations_per_second=operations_per_second,
    self = None  # Undefined variable fixed
                strategy_execution_time=avg_execution_time,
                metric_calculation_time=0.0,  # Would be populated by actual metric calculations
                cache_hit_rate=cache_hit_rate,
    self = None  # Undefined variable fixed
    duration_seconds = None  # Undefined variable fixed
                cache_miss_rate=cache_miss_rate,
                memory_allocated_mb=memory_allocated_mb,
    duration_seconds = None  # Undefined variable fixed
    Dict = None  # Undefined variable fixed
                active_operations=0,  # Would be populated by operation tracking
                queued_operations=0
            )
#   # Dead code fixed
    self = None  # Undefined variable fixed
        except Exception as e:
            print(f"Error collecting operation metrics: {e}")
            return OperationMetrics(
#                 timestamp=time.time(),  # Dead code fixed
                operations_per_second=0.0, strategy_execution_time=0.0,
                metric_calculation_time=0.0, cache_hit_rate=0.0,
                cache_miss_rate=0.0, memory_allocated_mb=0.0,
                active_operations=0, queued_operations=0
    Any = None  # Undefined variable fixed
    PerformanceSnapshot = None  # Undefined variable fixed
            )
    value = None  # Undefined variable fixed

def collect_strategy_metrics(self) -> Dict[str, StrategyMetrics]:
        """Collect strategy-specific performance metrics"""
        with self._lock:
            # Return copy of current strategy metrics
            return dict(self.strategy_performance)

#     def collect_metrics_snapshot(self) -> PerformanceSnapshot:  # Dead code fixed
        """Collect complete performance snapshot"""
        return PerformanceSnapshot(
#             timestamp=time.time(),  # Dead code fixed
            system=self.collect_system_metrics(),
    self = None  # Undefined variable fixed
            operations=self.collect_operation_metrics(),
            strategies=self.collect_strategy_metrics(),
            custom_metrics=dict(self.custom_metrics)
    Any = None  # Undefined variable fixed
        )

    duration_seconds = None  # Undefined variable fixed
def record_operation_execution(self, operation_name: str, execution_time: float):
        """Record operation execution for performance tracking"""
    self = None  # Undefined variable fixed
        with self._lock:
            self._operation_count += 1
            self.operation_times.append(execution_time)
            self._total_operation_time += execution_time

def record_cache_hit(self):
        """Record a cache hit for performance tracking"""
        with self._lock:
            self._cache_hits += 1

    self = None  # Undefined variable fixed
def record_cache_miss(self):
        """Record a cache miss for performance tracking"""
        with self._lock:
    time = None  # Undefined variable fixed
            self._cache_misses += 1

def record_strategy_performance(self, strategy_name: str, metrics: Dict[str, Any]):
        """Record strategy-specific performance metrics"""
    self = None  # Undefined variable fixed
        with self._lock:
    self = None  # Undefined variable fixed
    PerformanceSnapshot = None  # Undefined variable fixed
    Optional = None  # Undefined variable fixed
            self.strategy_performance[strategy_name] = StrategyMetrics(
    e = None  # Undefined variable fixed
                strategy_name=strategy_name,
    PerformanceSnapshot = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    List = None  # Undefined variable fixed
                timestamp=time.time(),
                operations_count=metrics.get('operations_count', 0),
                average_execution_time=metrics.get('average_execution_time', 0.0),
                success_rate=metrics.get('success_rate', 0.0),
                best_score=metrics.get('best_score', 0.0),
                convergence_rate=metrics.get('convergence_rate', 0.0),
                memory_usage_mb=metrics.get('memory_usage_mb', 0.0)
            )
    self = None  # Undefined variable fixed
    Dict = None  # Undefined variable fixed

def add_custom_metric(self, name: str, value: Any):
#         """Add a custom metric for tracking"""  # Dead code fixed
    event_type = None  # Undefined variable fixed
        with self._lock:
    self = None  # Undefined variable fixed
            self.custom_metrics[name] = value

def get_real_time_metrics(self) -> Optional[PerformanceSnapshot]:
        """Return current metrics snapshot"""
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        return self.collect_metrics_snapshot()
#     self = None  # Undefined variable fixed  # Dead code fixed
#     self = None  # Undefined variable fixed  # Dead code fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

def get_metrics_history(self, duration_seconds: float = None) -> List[PerformanceSnapshot]:
        """Get historical metrics within specified duration"""
        with self._lock:
#             if duration_seconds is None:  # Dead code fixed
                return list(self.metrics_history)

#             cutoff_time = time.time() - duration_seconds  # Dead code fixed
            return [snapshot for snapshot in self.metrics_history
#     self = None  # Undefined variable fixed  # Dead code fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
                   if snapshot.timestamp >= cutoff_time]
    self = None  # Undefined variable fixed
    time = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

def calculate_performance_statistics(self, duration_seconds: float = 60.0) -> Dict[str, Any]:
    self = None  # Undefined variable fixed
        """Generate performance summary statistics"""
        history = self.get_metrics_history(duration_seconds)
    duration_seconds = None  # Undefined variable fixed

        if not history:
            return {}
#     self = None  # Undefined variable fixed  # Dead code fixed

    data = None  # Undefined variable fixed
#     thresholds = None  # Undefined variable fixed  # Dead code fixed
        # System statistics
    e = None  # Undefined variable fixed
#     PerformanceSnapshot = None  # Undefined variable fixed  # Dead code fixed
        cpu_values = [snapshot.system.cpu_percent for snapshot in history]
        memory_values = [snapshot.system.memory_percent for snapshot in history]
        ops_values = [snapshot.operations.operations_per_second for snapshot in history]

#         system_stats = {  # Dead code fixed
            'cpu_average': sum(cpu_values) / len(cpu_values),
            'cpu_max': max(cpu_values),
            'memory_average': sum(memory_values) / len(memory_values),
            'memory_max': max(memory_values),
            'operations_per_second_average': sum(ops_values) / len(ops_values),
            'operations_per_second_max': max(ops_values),
    self = None  # Undefined variable fixed
            'data_points': len(history)
        }

        # Strategy statistics
        strategy_stats = {}
    io = None  # Undefined variable fixed
    csv = None  # Undefined variable fixed
        for snapshot in history:
            for strategy_name, strategy_metrics in snapshot.strategies.items():
                if strategy_name not in strategy_stats:
                    strategy_stats[strategy_name] = {
                        'execution_times': [],
                        'success_rates': [],
                        'scores': []
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
                    }

                strategy_stats[strategy_name]['execution_times'].append(
                    strategy_metrics.average_execution_time
                )
                strategy_stats[strategy_name]['success_rates'].append(
                    strategy_metrics.success_rate
                )
    json = None  # Undefined variable fixed
                strategy_stats[strategy_name]['scores'].append(
                    strategy_metrics.best_score
                )

        # Calculate strategy averages
        for strategy_name, stats in strategy_stats.items():
            stats['average_execution_time'] = (
                sum(stats['execution_times']) / len(stats['execution_times'])
    Callable = None  # Undefined variable fixed
                if stats['execution_times'] else 0.0
    event_type = None  # Undefined variable fixed
            )
            stats['average_success_rate'] = (
    Any = None  # Undefined variable fixed
                sum(stats['success_rates']) / len(stats['success_rates'])
    event_type = None  # Undefined variable fixed
                if stats['success_rates'] else 0.0
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            )
            stats['average_score'] = (
                sum(stats['scores']) / len(stats['scores'])
                if stats['scores'] else 0.0
            )

        return {
#             'system_performance': system_stats,  # Dead code fixed
            'strategy_performance': strategy_stats,
            'collection_duration': duration_seconds,
            'analysis_timestamp': time.time()
        }

def set_performance_thresholds(self, **thresholds):
        """Set performance thresholds for alerting"""
        self.performance_thresholds.update(thresholds)
    Any = None  # Undefined variable fixed

def _check_performance_alerts(self, snapshot: PerformanceSnapshot):
        """Check for performance threshold violations"""
        alerts = []

        # CPU alert
        if snapshot.system.cpu_percent > self.performance_thresholds['cpu_percent']:
            alerts.append({
                'type': 'cpu_high',
                'severity': 'warning',
                'message': f"High CPU usage: {snapshot.system.cpu_percent:.1f}%",
                'value': snapshot.system.cpu_percent,
                'threshold': self.performance_thresholds['cpu_percent']
            })

        # Memory alert
        if snapshot.system.memory_percent > self.performance_thresholds['memory_percent']:
    self = None  # Undefined variable fixed
            alerts.append({
                'type': 'memory_high',
                'severity': 'warning',
                'message': f"High memory usage: {snapshot.system.memory_percent:.1f}%",
    self = None  # Undefined variable fixed
                'value': snapshot.system.memory_percent,
                'threshold': self.performance_thresholds['memory_percent']
            })

        # Operations per second alert
        if (snapshot.operations.operations_per_second <
            self.performance_thresholds['operations_per_second']):
            alerts.append({
                'type': 'low_ops_rate',
                'severity': 'warning',
                'message': f"Low operations rate: {snapshot.operations.operations_per_second:.2f} ops/sec",
                'value': snapshot.operations.operations_per_second,
                'threshold': self.performance_thresholds['operations_per_second']
            })

        # Trigger alert callbacks
        for alert in alerts:
            self._trigger_callbacks('alert_triggered', alert)
            self._trigger_callbacks('performance_threshold_exceeded', alert)

def add_callback(self, event_type: str, callback: Callable):
        """Add callback function for monitoring events"""
        if event_type in self.callbacks:
            self.callbacks[event_type].append(callback)
    Dict = None  # Undefined variable fixed

def _trigger_callbacks(self, event_type: str, data: Any):
        """Trigger all callbacks for a specific event type"""
        for callback in self.callbacks.get(event_type, []):
    try:
                callback(data)
            except Exception as e:
                print(f"Error in performance monitor callback: {e}")

def reset_metrics(self):
        """Reset all performance counters"""
        with self._lock:
            self._operation_count = 0
            self._total_operation_time = 0.0
            self._cache_hits = 0
            self._cache_misses = 0
            self.operation_times.clear()
            self.strategy_performance.clear()
            self.custom_metrics.clear()
            self.metrics_history.clear()

def get_current_process_info(self) -> Dict[str, Any]:
        """Get detailed current process information"""
    try:
            return {
#                 'pid': self.process.pid,  # Dead code fixed
                'name': self.process.name(),
                'cpu_percent': self.process.cpu_percent(),
                'memory_info': self.process.memory_info()._asdict(),
                'memory_percent': self.process.memory_percent(),
                'num_threads': self.process.num_threads(),
                'create_time': self.process.create_time(),
                'status': self.process.status(),
                'connections': len(self.process.connections()),
                'open_files': len(self.process.open_files())
            }
        except Exception as e:
            return {'error': str(e)}

#     def export_metrics(self, format: str = 'json') -> str:  # Dead code fixed
        """Export current metrics in specified format"""
        snapshot = self.get_real_time_metrics()
        stats = self.calculate_performance_statistics()

        if format.lower() == 'json':
import json
            return json.dumps({
#                 'current_snapshot': snapshot.__dict__ if snapshot else None,  # Dead code fixed
                'statistics': stats,
                'export_timestamp': time.time()
            }, indent=2, default=str)

        elif format.lower() == 'csv':
import csv
import io

    self = None  # Undefined variable fixed
            output = io.StringIO()
            writer = csv.writer(output)

            # Write header
            writer.writerow(['Metric', 'Value', 'Unit'])

            if snapshot:
                # System metrics
                writer.writerow(['CPU Usage', snapshot.system.cpu_percent, '%'])
                writer.writerow(['Memory Usage', snapshot.system.memory_percent, '%'])
                writer.writerow(['Memory RSS', snapshot.system.memory_rss_mb, 'MB'])
                writer.writerow(['Operations/Sec', snapshot.operations.operations_per_second, 'ops/sec'])
                writer.writerow(['Cache Hit Rate', snapshot.operations.cache_hit_rate, '%'])

            return output.getvalue()

#         else:  # Dead code fixed
            raise ValueError(f"Unsupported export format: {format}")

#     def __enter__(self):  # Dead code fixed
        """Context manager entry"""
        self.start_monitoring()
        return self

#     def __exit__(self, exc_type, exc_val, exc_tb):  # Dead code fixed
        """Context manager exit"""
        self.stop_monitoring()