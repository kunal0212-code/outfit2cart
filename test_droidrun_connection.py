import pytest

from tools.android_tools import AndroidToolsWithDroidrun
from config import DROIDRUN_CONFIG


class TestDroidrunConnection:
    @pytest.fixture
    def android_tools(self) -> AndroidToolsWithDroidrun:
        return AndroidToolsWithDroidrun()

    def test_connect_to_device(self, android_tools: AndroidToolsWithDroidrun):
        assert android_tools.connect_to_device() is True
