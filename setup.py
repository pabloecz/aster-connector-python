import os
from setuptools import setup, find_packages

# --- CONFIGURATION CONSTANTS (Consider moving these to setup.cfg) ---
# Single source of truth for metadata variables.
PACKAGE_NAME = "aster-connector-python"
PACKAGE_DESCRIPTION = (
    "A lightweight Python library acting as a connector to the Aster Finance public API."
)
PACKAGE_AUTHOR = "Your Name/Organization Name Here" # NOTE: Original was empty, filled with placeholder.
PACKAGE_URL = "https://github.com/asterdex/aster-connector-python"
PACKAGE_VERSION = "1.1.0" 

# --- READ REQUIREMENTS ---
# Use os.path.abspath to ensure the path is resolved correctly 
# relative to this setup.py file, and filter out empty lines/comments.
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
REQUIREMENTS_FILE_PATH = os.path.join(ROOT_DIR, "requirements", "common.txt")

with open(REQUIREMENTS_FILE_PATH, "r") as fh:
    # Filter out empty lines and comments, and strip whitespace.
    requirements = [
        line.strip() 
        for line in fh.readlines() 
        if line.strip() and not line.startswith("#")
    ]

# --- READ README FOR LONG DESCRIPTION ---
with open("README.md", "r") as fh:
    long_description = fh.read()

# --- VERSION HANDLING (Ensure a Single Source of Truth) ---
# If a version is explicitly defined above, use it. Otherwise, attempt to load 
# it dynamically from the package's __version__.py file.
# This pattern simplifies the original conditional block.

version_data = {}
if not PACKAGE_VERSION:
    # Attempt to read the version dynamically from the package itself
    version_file_path = os.path.join(ROOT_DIR, PACKAGE_NAME.replace('-', '_'), "__version__.py")
    if os.path.exists(version_file_path):
        with open(version_file_path) as f:
            exec(f.read(), version_data)
        PACKAGE_VERSION = version_data.get("__version__")
    
# Fallback/Error check
if not PACKAGE_VERSION:
    raise RuntimeError("Version not found in PACKAGE_VERSION constant or __version__.py file.")


setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    license="MIT",
    description=PACKAGE_DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Using lowercase style for setup arguments is preferred (PEP 8 for variables)
    author=PACKAGE_AUTHOR,
    url=PACKAGE_URL,
    keywords=["Aster", "Public API", "Finance", "Connector"],
    # Pass the cleaned list directly
    install_requires=requirements,
    # Exclude tests and any other non-package directories
    packages=find_packages(exclude=["tests", "docs", "examples"]), 
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        # Keep only currently supported Python versions. 3.6 is EOL. 
        # Add newer versions if the library supports them.
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    # Set the minimum required Python version
    python_requires=">=3.7", 
)
