"""Shared pytest fixtures and configuration for all tests."""

import os
import sys
import tempfile
from pathlib import Path
from typing import Generator

import pytest

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for test files.
    
    Yields:
        Path: Path to the temporary directory.
    """
    with tempfile.TemporaryDirectory() as temp_dir_str:
        yield Path(temp_dir_str)


@pytest.fixture
def temp_file(temp_dir: Path) -> Generator[Path, None, None]:
    """Create a temporary file for testing.
    
    Args:
        temp_dir: Temporary directory fixture.
        
    Yields:
        Path: Path to the temporary file.
    """
    temp_file = temp_dir / "test_file.txt"
    temp_file.write_text("test content")
    yield temp_file


@pytest.fixture
def mock_config() -> dict:
    """Provide a mock configuration dictionary.
    
    Returns:
        dict: Mock configuration for testing.
    """
    return {
        "debug": True,
        "verbose": False,
        "timeout": 30,
        "max_retries": 3,
        "features": {
            "experimental": False,
            "cache_enabled": True,
        }
    }


@pytest.fixture
def sample_data() -> dict:
    """Provide sample data for testing algorithms.
    
    Returns:
        dict: Sample data sets for different algorithm types.
    """
    return {
        "integers": [64, 34, 25, 12, 22, 11, 90],
        "sorted_integers": [11, 12, 22, 25, 34, 64, 90],
        "strings": ["apple", "banana", "cherry", "date", "elderberry"],
        "graph_edges": [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4)],
        "matrix": [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
    }


@pytest.fixture
def captured_output(monkeypatch):
    """Capture stdout and stderr for testing print statements.
    
    Usage:
        def test_print(captured_output):
            print("Hello")
            assert captured_output() == "Hello\\n"
    """
    import io
    
    captured = {"stdout": "", "stderr": ""}
    
    def capture():
        return captured["stdout"]
    
    def mock_stdout_write(s):
        captured["stdout"] += s
    
    def mock_stderr_write(s):
        captured["stderr"] += s
    
    monkeypatch.setattr(sys.stdout, 'write', mock_stdout_write)
    monkeypatch.setattr(sys.stderr, 'write', mock_stderr_write)
    
    return capture


@pytest.fixture(autouse=True)
def reset_sys_modules():
    """Reset sys.modules to ensure clean imports between tests."""
    modules_before = set(sys.modules.keys())
    yield
    modules_after = set(sys.modules.keys())
    for module in modules_after - modules_before:
        if module.startswith('coding_algorithms'):
            del sys.modules[module]


@pytest.fixture
def mock_env_vars(monkeypatch) -> dict:
    """Set mock environment variables for testing.
    
    Returns:
        dict: Dictionary of environment variables set for testing.
    """
    env_vars = {
        "TEST_ENV": "true",
        "DEBUG": "false",
        "API_KEY": "test_key_12345",
        "TIMEOUT": "60",
    }
    
    for key, value in env_vars.items():
        monkeypatch.setenv(key, value)
    
    return env_vars


def pytest_configure(config):
    """Configure pytest with custom settings."""
    # Add custom markers documentation
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test (fast, isolated)"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test (may have dependencies)"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running (use --runslow to include)"
    )


def pytest_addoption(parser):
    """Add custom command line options."""
    parser.addoption(
        "--runslow",
        action="store_true",
        default=False,
        help="run slow tests"
    )


def pytest_collection_modifyitems(config, items):
    """Modify test collection to handle custom markers."""
    if not config.getoption("--runslow"):
        skip_slow = pytest.mark.skip(reason="need --runslow option to run")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip_slow)