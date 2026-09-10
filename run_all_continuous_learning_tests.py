"""
Root entrypoint proxy forwarding to scripts/run_all_continuous_learning_tests.py.
Canonical sequential script resides in scripts/run_all_continuous_learning_tests.py.
"""
import os
import sys
import runpy

_ROOT = os.path.dirname(os.path.abspath(__file__))
_SCRIPT = os.path.join(_ROOT, "scripts", "run_all_continuous_learning_tests.py")

if __name__ == "__main__":
    runpy.run_path(_SCRIPT, run_name="__main__")
