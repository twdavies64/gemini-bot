"""
Monkey-patch dotenv.load_dotenv to resolve 1Password secret references.

Import this module BEFORE any code that calls load_dotenv().
"""

import subprocess
import os
import sys
from dotenv import dotenv_values
import dotenv

_original_load_dotenv = dotenv.load_dotenv


def _load_dotenv_1password(dotenv_path=".env", stream=None, verbose=False, 
                            override=False, interpolate=True, encoding="utf-8", **kwargs):
    """Drop-in replacement for load_dotenv that resolves op:// references via 1Password CLI."""
    
    values = dotenv_values(
        dotenv_path=dotenv_path,
        stream=stream,
        verbose=verbose,
        interpolate=interpolate,
        encoding=encoding
    )
    
    for key, value in values.items():
        if value and value.startswith("op://"):
            result = subprocess.run(
                ["op", "read", value],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                raise RuntimeError(
                    f"Failed to resolve {key} from 1Password: {result.stderr.strip()}"
                )
            resolved_value = result.stdout.strip()
            
            if override or key not in os.environ:
                os.environ[key] = resolved_value
        else:
            if override or key not in os.environ:
                os.environ.setdefault(key, value or "")
    
    return True


# Monkey-patch dotenv module
dotenv.load_dotenv = _load_dotenv_1password
sys.modules['dotenv'].load_dotenv = _load_dotenv_1password # type: ignore