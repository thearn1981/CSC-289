#!/usr/bin/env python3
"""
Environment Validation Script
Run this to confirm your development environment is operational.
"""

import sys
import platform
from datetime import datetime

def validate_environment():
    """Run basic environment checks and report status."""
    
    print("=" * 50)
    print("ALGOCRATIC FUTURES™ ENVIRONMENT VALIDATION")
    print("=" * 50)
    print()
    
    # Collect system info
    checks = {
        "Python Version": sys.version.split()[0],
        "Platform": platform.system(),
        "Machine": platform.machine(),
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Display results
    print("SYSTEM DIAGNOSTICS:")
    for key, value in checks.items():
        print(f"  {key}: {value}")
    print()
    
    # Version check
    major, minor = sys.version_info[:2]
    if major >= 3 and minor >= 8:
        status = "PASSED"
        message = "Environment validated successfully."
    else:
        status = "WARNING"
        message = f"Python {major}.{minor} detected. 3.8+ recommended."
    
    print(f"STATUS: {status}")
    print(f"MESSAGE: {message}")
    print()
    
    # The proof of completion
    print("=" * 50)
    print("Environment validated for: Teresa Hearn")
    print("=" * 50)
    
    return status == "PASSED"

if __name__ == "__main__":
    success = validate_environment()
    sys.exit(0 if success else 1)