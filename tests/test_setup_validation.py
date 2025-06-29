import pytest
import sys
from pathlib import Path


class TestSetupValidation:
    """Validation tests to verify the testing infrastructure is properly configured."""
    
    def test_python_version(self):
        """Verify Python version is compatible."""
        assert sys.version_info >= (3, 7), "Python 3.7 or higher is required"
    
    def test_project_structure(self):
        """Verify the basic project structure exists."""
        project_root = Path(__file__).parent.parent
        assert project_root.exists()
        assert (project_root / "pyproject.toml").exists()
        assert (project_root / "tests").exists()
        assert (project_root / "tests" / "conftest.py").exists()
    
    def test_pytest_import(self):
        """Verify pytest can be imported."""
        import pytest
        assert pytest.__version__
    
    def test_coverage_import(self):
        """Verify pytest-cov is available."""
        import pytest_cov
        assert pytest_cov
    
    def test_mock_import(self):
        """Verify pytest-mock is available."""
        import pytest_mock
        assert pytest_mock
    
    @pytest.mark.unit
    def test_unit_marker(self):
        """Verify unit test marker works."""
        assert True
    
    @pytest.mark.integration
    def test_integration_marker(self):
        """Verify integration test marker works."""
        assert True
    
    @pytest.mark.slow
    def test_slow_marker(self):
        """Verify slow test marker works."""
        assert True
    
    def test_fixtures_available(self, temp_dir, mock_config, mock_session):
        """Verify custom fixtures are available."""
        assert temp_dir.exists()
        assert mock_config is not None
        assert mock_session is not None
    
    def test_sample_data_fixture(self, sample_ticket_data):
        """Verify sample data fixture provides expected structure."""
        assert "train_no" in sample_ticket_data
        assert "from_station" in sample_ticket_data
        assert "to_station" in sample_ticket_data
        assert "seats" in sample_ticket_data
    
    def test_logger_mock(self, mock_logger):
        """Verify logger can be mocked."""
        mock_logger.info("Test message")
        mock_logger.info.assert_called_once_with("Test message")
    
    def test_file_operations_mock(self, mock_file_operations):
        """Verify file operations can be mocked."""
        with open("test.txt", "r") as f:
            content = f.read()
        assert content == "test data"
    
    def test_stdout_capture(self, capture_stdout):
        """Verify stdout capture works."""
        print("Hello, testing!")
        output = capture_stdout()
        assert "Hello, testing!" in output