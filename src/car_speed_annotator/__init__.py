#!/usr/bin/env python3

"""Add custom tags to OSM extracts for travel time matrices"""

__version__ = "0.0.2"

from .car_speed_annotator import CarSpeedAnnotator

__all__ = [
    "CarSpeedAnnotator",
    "__version__",
]
