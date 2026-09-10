"""
Root entrypoint proxy forwarding to backend.05_orchestration.algorithm.
Maintains backward compatibility with legacy test suites and external callers.
Canonical sequential implementation resides in backend/05_orchestration/algorithm.py.
"""
import os
import sys
import importlib

_ROOT = os.path.dirname(os.path.abspath(__file__))
_BACKEND = os.path.join(_ROOT, "backend")
_ORCH = os.path.join(_BACKEND, "05_orchestration")

for _p in [_ROOT, _BACKEND, _ORCH]:
    if os.path.exists(_p) and _p not in sys.path:
        sys.path.insert(0, _p)

_mod = importlib.import_module("backend.05_orchestration.algorithm")

for _attr in dir(_mod):
    if not _attr.startswith("__"):
        globals()[_attr] = getattr(_mod, _attr)

if hasattr(_mod, "__all__"):
    __all__ = _mod.__all__
