"""Validation tests to ensure the testing infrastructure is properly configured."""

import os
import sys
from pathlib import Path

import pytest


class TestInfrastructureSetup:
    """Test class to validate the testing infrastructure setup."""
    
    @pytest.mark.unit
    def test_project_structure_exists(self):
        """Verify that the project structure is correctly set up."""
        project_root = Path(__file__).parent.parent
        
        # Check main directories exist
        assert project_root.exists()
        assert (project_root / "tests").exists()
        assert (project_root / "tests" / "unit").exists()
        assert (project_root / "tests" / "integration").exists()
        assert (project_root / "coding_algorithms").exists()
        
        # Check __init__.py files exist
        assert (project_root / "tests" / "__init__.py").exists()
        assert (project_root / "tests" / "unit" / "__init__.py").exists()
        assert (project_root / "tests" / "integration" / "__init__.py").exists()
        assert (project_root / "coding_algorithms" / "__init__.py").exists()
    
    @pytest.mark.unit
    def test_pyproject_toml_exists(self):
        """Verify that pyproject.toml exists and contains required sections."""
        project_root = Path(__file__).parent.parent
        pyproject_path = project_root / "pyproject.toml"
        
        assert pyproject_path.exists(), "pyproject.toml should exist"
        
        content = pyproject_path.read_text()
        
        # Check for Poetry sections
        assert "[tool.poetry]" in content
        assert "[tool.poetry.dependencies]" in content
        assert "[tool.poetry.group.dev.dependencies]" in content
        assert "[tool.poetry.scripts]" in content
        
        # Check for pytest configuration
        assert "[tool.pytest.ini_options]" in content
        assert "[tool.coverage.run]" in content
        assert "[tool.coverage.report]" in content
        
        # Check that test dependencies are listed
        assert "pytest" in content
        assert "pytest-cov" in content
        assert "pytest-mock" in content
    
    @pytest.mark.unit
    def test_fixtures_available(self, temp_dir, mock_config, sample_data):
        """Test that common fixtures are available and working."""
        # Test temp_dir fixture
        assert temp_dir.exists()
        assert temp_dir.is_dir()
        
        # Test mock_config fixture
        assert isinstance(mock_config, dict)
        assert "debug" in mock_config
        assert "features" in mock_config
        
        # Test sample_data fixture
        assert isinstance(sample_data, dict)
        assert "integers" in sample_data
        assert "graph_edges" in sample_data
    
    @pytest.mark.unit
    def test_markers_registered(self, pytestconfig):
        """Verify that custom markers are properly registered."""
        # Get the registered markers from config
        markers_list = pytestconfig.getini("markers")
        marker_names = [marker.split(":")[0].strip() for marker in markers_list]
        
        assert "unit" in marker_names
        assert "integration" in marker_names
        assert "slow" in marker_names
    
    @pytest.mark.unit
    def test_python_path_configured(self):
        """Verify that the project root is in the Python path."""
        project_root = Path(__file__).parent.parent
        
        # Check if we can import the main package
        import coding_algorithms
        assert coding_algorithms.__version__ == "0.1.0"
    
    @pytest.mark.unit
    def test_coverage_configuration(self):
        """Test that coverage is properly configured."""
        project_root = Path(__file__).parent.parent
        pyproject_path = project_root / "pyproject.toml"
        
        content = pyproject_path.read_text()
        
        # Check coverage configuration
        assert "--cov=coding_algorithms" in content
        assert "--cov-fail-under=80" in content
        assert "--cov-report=html:htmlcov" in content
        assert "--cov-report=xml:coverage.xml" in content
    
    @pytest.mark.slow
    @pytest.mark.unit
    def test_slow_marker_skip(self):
        """This test should be skipped unless --runslow is provided."""
        # This test validates that slow tests are skipped by default
        import time
        time.sleep(0.1)  # Simulate slow operation
        assert True
    
    @pytest.mark.integration
    def test_integration_marker(self):
        """Test that integration marker works correctly."""
        # This is a placeholder integration test
        assert True
    
    @pytest.mark.unit
    def test_captured_output_fixture(self, captured_output):
        """Test that the captured output fixture works correctly."""
        print("Hello, World!")
        output = captured_output()
        assert "Hello, World!" in output


class TestEnvironmentValidation:
    """Validate the testing environment setup."""
    
    @pytest.mark.unit
    def test_mock_env_vars(self, mock_env_vars):
        """Test that mock environment variables are set correctly."""
        assert os.environ.get("TEST_ENV") == "true"
        assert os.environ.get("DEBUG") == "false"
        assert os.environ.get("API_KEY") == "test_key_12345"
        assert os.environ.get("TIMEOUT") == "60"
        
        # Verify the fixture returns the correct dict
        assert mock_env_vars["TEST_ENV"] == "true"
        assert len(mock_env_vars) == 4
    
    @pytest.mark.unit
    def test_temp_file_fixture(self, temp_file):
        """Test that the temp file fixture creates a file correctly."""
        assert temp_file.exists()
        assert temp_file.is_file()
        assert temp_file.read_text() == "test content"
        
        # File should be in a temp directory
        assert "tmp" in str(temp_file) or "temp" in str(temp_file).lower()


def test_pytest_running():
    """Basic test to ensure pytest is running correctly."""
    assert True


if __name__ == "__main__":
    # Allow running this file directly for quick validation
    pytest.main([__file__, "-v"])