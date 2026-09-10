"""
Global pytest configuration.
Imports compatibility shims from compat.py for legacy runners/fixtures without mutating production code.
Ensures transparent access to sequentially arranged models/ and data/ artifacts.
"""
import os
import sys
import gc
import pytest

_WORKSPACE = os.path.dirname(os.path.abspath(__file__))

# Ensure transparent access to sequentially organized artifacts
for _src, _sub in [
    ("ensemble.joblib", "models"),
    ("pipeline.joblib", "models"),
    ("rsf_only.joblib", "models"),
    ("timeline.joblib", "models"),
    ("indian_infrastructure_projects_dataset.csv", "data"),
    ("district_coordinates.json", "data"),
    ("feature_importance.csv", "data"),
]:
    _sub_path = os.path.join(_WORKSPACE, _sub, _src)
    _root_path = os.path.join(_WORKSPACE, _src)
    if not os.path.exists(_root_path) and os.path.exists(_sub_path):
        try:
            os.link(_sub_path, _root_path)
        except Exception:
            pass

from compat import apply_all_patches

apply_all_patches()

@pytest.fixture(autouse=True, scope="module")
def _cleanup_memory_module():
    yield
    gc.collect()
