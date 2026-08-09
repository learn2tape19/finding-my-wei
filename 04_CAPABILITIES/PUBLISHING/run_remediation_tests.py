#!/usr/bin/env python3
"""
Test runner for PCP-ENG-002 remediation.
No external dependencies - uses unittest framework.
"""

import sys
import unittest
from pathlib import Path

# Add control_plane to path
sys.path.insert(0, str(Path(__file__).parent))

# Import all test classes
from tests.test_wordpress_v1_adapter import *

if __name__ == "__main__":
    # Run all tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)
