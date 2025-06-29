import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import Mock, MagicMock


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def mock_config():
    """Provide a mock configuration object."""
    config = MagicMock()
    config.station_names = {"北京": "BJP", "上海": "SHH", "广州": "GZQ"}
    config.seat_types = ["硬座", "硬卧", "软卧", "二等座", "一等座", "商务座"]
    config.urls = {
        "login": "https://kyfw.12306.cn/otn/login/init",
        "query": "https://kyfw.12306.cn/otn/leftTicket/query",
    }
    return config


@pytest.fixture
def mock_session():
    """Provide a mock requests session."""
    session = Mock()
    response = Mock()
    response.status_code = 200
    response.json.return_value = {"status": True, "data": {}}
    response.text = "Mock response"
    session.get.return_value = response
    session.post.return_value = response
    return session


@pytest.fixture
def sample_ticket_data():
    """Provide sample ticket data for testing."""
    return {
        "train_no": "G123",
        "from_station": "北京",
        "to_station": "上海",
        "departure_time": "08:00",
        "arrival_time": "12:30",
        "seats": {
            "二等座": "有",
            "一等座": "10",
            "商务座": "无"
        }
    }


@pytest.fixture
def mock_logger(mocker):
    """Provide a mock logger."""
    return mocker.patch('config.logger.logger')


@pytest.fixture
def test_data_dir():
    """Provide path to test data directory."""
    return Path(__file__).parent / "test_data"


@pytest.fixture(autouse=True)
def reset_environment():
    """Reset environment variables before each test."""
    original_env = os.environ.copy()
    yield
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def mock_file_operations(mocker):
    """Mock file operations for testing."""
    mock_open = mocker.mock_open(read_data="test data")
    mocker.patch("builtins.open", mock_open)
    return mock_open


@pytest.fixture
def capture_stdout(monkeypatch):
    """Capture stdout for testing print statements."""
    import io
    import sys
    
    captured = io.StringIO()
    monkeypatch.setattr(sys, 'stdout', captured)
    
    def get_output():
        return captured.getvalue()
    
    return get_output