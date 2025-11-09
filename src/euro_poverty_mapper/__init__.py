"""
EuroPovertyMapper - A tool for analyzing European poverty data
"""

__version__ = "0.1.0"
__author__ = "Ghulam Abbas Zafari"
__email__ = "zafariabbas68@gmail.com"

from .data_processor import DataProcessor
from .visualizer import Visualizer
from .analyzer import Analyzer

__all__ = ["DataProcessor", "Visualizer", "Analyzer"]
