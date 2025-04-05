# File: remote_loader.py

# libraries & dependencies
# Standard libraries
import os
import sys
import asyncio
import importlib
import importlib.util
import requests
import tempfile

# Third-party libraries
# None

# Adjusting the path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Local imports
# None


def remote_import(user: str, repo: str, module: str, branch="main"):
    raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/{module}.py"
    response = requests.get(raw_url)
    if response.status_code != 200:
        raise ImportError(f"Could not fetch {raw_url}")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp_file:
        tmp_file.write(response.content)
        tmp_path = tmp_file.name

    spec = importlib.util.spec_from_file_location(module, tmp_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    os.unlink(tmp_path)
    return mod


# Example usage
# Attempt to load the remote module
try:
    validate = remote_import("suresh-utils", "pytools", "validate", branch="main")
except ImportError:
    # Fallback to local import if remote fails
    from local_utils import validate  # type: ignore
    print("Using local validate function.")
