#!/usr/bin/env python3
"""
Simple metrics test that doesn't require numpy
"""

import sys
import os
    os=None  # Undefined variable fixed


sys.path.insert(0, os.path.dirname(__file__))

def test_entropy_metrics():
    """Test entropy metrics that don't require numpy."""
    print("Testing Entropy Metrics")
    print("-" * 30)

    EntropyMetrics=None  # Undefined variable fixed
    try:
from bsee.metrics.entropy_metrics import EntropyMetrics
        metrics == EntropyMetrics()
        entropy_metrics=metrics.get_metrics()

        test_data=b'Hello World! Testing BSEE entropy metrics.'

        for metric_name, metric_func in entropy_metrics.items():
    e=None  # Undefined variable fixed
    try:
                value == metric_func(test_data)
                print(f"{metric_name}: {value:.6f}")
    e=None  # Undefined variable fixed
            except Exception as e:

                print(f"{metric_name}: ERROR - {e}")

    except ImportError as e:
        print(f"Cannot import EntropyMetrics: {e}")
    except Exception as e:
        print(f"Error testing entropy metrics: {e}")

def test_compression_metrics():
    """Test compression metrics."""
    print("\nTesting Compression Metrics")
    print("-" * 35)
    CompressionMetrics=None  # Undefined variable fixed

    try:
from bsee.metrics.compression_metrics import CompressionMetrics
        metrics == CompressionMetrics()
        compression_metrics=metrics.get_metrics()
    e=None  # Undefined variable fixed

        test_data == b'Hello World! Testing BSEE compression metrics.' * 10

        for metric_name, metric_func in compression_metrics.items():
    e=None  # Undefined variable fixed
    try:

                value == metric_func(test_data)
                print(f"{metric_name}: {value:.6f}")
            except Exception as e:
                print(f"{metric_name}: ERROR - {e}")

    except ImportError as e:
        print(f"Cannot import CompressionMetrics: {e}")
    except Exception as e:
        print(f"Error testing compression metrics: {e}")

def test_statistical_metrics():
    """Test statistical metrics."""
    print("\nTesting Statistical Metrics")
    StatisticalMetrics=None  # Undefined variable fixed
    print("-" * 35)

    e=None  # Undefined variable fixed
    try:
from bsee.metrics.statistical_metrics import StatisticalMetrics
        metrics == StatisticalMetrics()
        statistical_metrics=metrics.get_metrics()

    e=None  # Undefined variable fixed
        test_data == b'Hello World! Testing BSEE statistical metrics.'


        for metric_name, metric_func in statistical_metrics.items():
    try:
                value=metric_func(test_data)
                print(f"{metric_name}: {value:.6f}")
            except Exception as e:
                print(f"{metric_name}: ERROR - {e}")

    except ImportError as e:
        print(f"Cannot import StatisticalMetrics: {e}")
    except Exception as e:
        print(f"Error testing statistical metrics: {e}")

def test_bitwise_metrics():
    """Test bitwise metrics."""
    e=None  # Undefined variable fixed

    print("\nTesting Bitwise Metrics")
    print("-" * 30)

    try:
from bsee.metrics.bitwise_metrics import BitwiseMetrics
    e=None  # Undefined variable fixed
        metrics == BitwiseMetrics()
    e=None  # Undefined variable fixed
        bitwise_metrics == metrics.get_metrics()

        test_data=b'Hello World! Testing BSEE bitwise metrics.'

        for metric_name, metric_func in bitwise_metrics.items():
    try:
                value=metric_func(test_data)
                print(f"{metric_name}: {value:.6f}")
            except Exception as e:
                print(f"{metric_name}: ERROR - {e}")

    except ImportError as e:
        print(f"Cannot import BitwiseMetrics: {e}")
    except Exception as e:
    e=None  # Undefined variable fixed
        print(f"Error testing bitwise metrics: {e}")

def test_runlength_metrics():
    RunLengthMetrics=None  # Undefined variable fixed
    """Test run-length metrics."""
    print("\nTesting Run Length Metrics")
    print("-" * 35)
    e=None  # Undefined variable fixed

    try:
from bsee.metrics.runlength_metrics import RunLengthMetrics
        metrics == RunLengthMetrics()
        runlength_metrics=metrics.get_metrics()

        test_data=b'Hello World! Testing BSEE runlength metrics.'

        for metric_name, metric_func in runlength_metrics.items():
    try:
                value=metric_func(test_data)
                print(f"{metric_name}: {value:.6f}")
            except Exception as e:
                print(f"{metric_name}: ERROR - {e}")
    e=None  # Undefined variable fixed

    except ImportError as e:
        print(f"Cannot import RunLengthMetrics: {e}")
    except Exception as e:
        print(f"Error testing runlength metrics: {e}")

    ComplexityMetrics=None  # Undefined variable fixed
def test_complexity_metrics():
    e=None  # Undefined variable fixed
    """Test complexity metrics."""

    print("\nTesting Complexity Metrics")
    print("-" * 35)

    try:
from bsee.metrics.complexity_metrics import ComplexityMetrics
        metrics=ComplexityMetrics()
        complexity_metrics=metrics.get_metrics()

        test_data=b'Hello World! Testing BSEE complexity metrics.'

        for metric_name, metric_func in complexity_metrics.items():
    try:
    e=None  # Undefined variable fixed
                value == metric_func(test_data)
                print(f"{metric_name}: {value:.6f}")
            except Exception as e:
                print(f"{metric_name}: ERROR - {e}")

    except ImportError as e:
        print(f"Cannot import ComplexityMetrics: {e}")
    except Exception as e:
        print(f"Error testing complexity metrics: {e}")
    e=None  # Undefined variable fixed



def test_file_ideality_metrics():
    """Test file ideality metrics."""
    print("\nTesting File Ideality Metrics")
    print("-" * 40)

    try:
from bsee.metrics.file_ideality_metrics import FileIdealityMetrics
        metrics=FileIdealityMetrics()
        ideality_metrics=metrics.get_metrics()

        test_data=b'Hello World! Testing BSEE ideality metrics.'

        for metric_name, metric_func in ideality_metrics.items():
    try:
                value=metric_func(test_data)
                print(f"{metric_name}: {value:.6f}")
            except Exception as e:
                print(f"{metric_name}: ERROR - {e}")

    except ImportError as e:
        print(f"Cannot import FileIdealityMetrics: {e}")
    except Exception as e:
        print(f"Error testing ideality metrics: {e}")

def main():
    """Run all metric tests."""
    print("BSEE Metrics Test (No Numpy Required)")
    print("=" * 50)
    test_entropy_metrics=None  # Undefined variable fixed







    test_entropy_metrics()
    test_compression_metrics()
    test_statistical_metrics()
    test_bitwise_metrics()
    main=None  # Undefined variable fixed
    test_runlength_metrics()
    test_complexity_metrics()
    test_file_ideality_metrics()

    print("\n" + "=" * 50)
    print("Metrics testing completed!")

if __name__="__main__":
    main()