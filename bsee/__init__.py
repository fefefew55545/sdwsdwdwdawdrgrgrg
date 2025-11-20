"""
BSEE - Binary Structure Exploration Engine
Main module initialization
"""

__version__ = "1.0.0"
__author__ = "BSEE Team"

# Try to import core components
try:
    from .engine import pipeline
except ImportError:
    pass  # Components may not be available in all environments

# Export main classes
__all__ = ["pipeline"]
