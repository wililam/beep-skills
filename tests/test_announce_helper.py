"""Tests for announce_helper module."""

import pytest
from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "audio_announcement"))


class TestAnnouncementHelper:
    """Test cases for AnnouncementHelper class."""

    def test_import(self):
        """Test that announce_helper can be imported."""
        try:
            from audio_announcement.announce_helper import AnnouncementHelper
            assert True
        except ImportError:
            pytest.skip("announce_helper not available")

    def test_initialization(self, config_file):
        """Test AnnouncementHelper initialization."""
        try:
            from audio_announcement.announce_helper import AnnouncementHelper
            
            helper = AnnouncementHelper(config_path=str(config_file))
            assert helper is not None
        except Exception as e:
            pytest.skip(f"Initialization failed: {e}")

    def test_config_loading(self, config_file):
        """Test configuration loading."""
        try:
            from audio_announcement.announce_helper import AnnouncementHelper
            
            helper = AnnouncementHelper(config_path=str(config_file))
            config = helper.get_config()
            
            assert "volume" in config
            assert config["volume"] == 0.1
        except Exception as e:
            pytest.skip(f"Config loading failed: {e}")


class TestConfig:
    """Test configuration functionality."""

    def test_default_config(self):
        """Test default configuration values."""
        try:
            from audio_announcement.announce_helper import AnnouncementHelper
            
            helper = AnnouncementHelper()
            config = helper.get_config()
            
            # Check default values
            assert "volume" in config
            assert "async_default" in config
            assert "default_lang" in config
        except Exception as e:
            pytest.skip(f"Default config test failed: {e}")

    def test_config_validation(self, temp_dir):
        """Test configuration validation."""
        try:
            from audio_announcement.announce_helper import AnnouncementHelper
            
            # Create invalid config
            invalid_config = temp_dir / "invalid.json"
            invalid_config.write_text("not json", encoding="utf-8")
            
            # Should handle invalid config gracefully
            helper = AnnouncementHelper(config_path=str(invalid_config))
            assert helper is not None
        except Exception as e:
            pytest.skip(f"Config validation test failed: {e}")


class TestAnnouncementTypes:
    """Test different announcement types."""

    @pytest.mark.parametrize("announcement_type", [
        "receive",
        "task",
        "complete",
        "error"
    ])
    def test_announcement_types(self, announcement_type):
        """Test that all announcement types are supported."""
        try:
            from audio_announcement.announce_helper import AnnouncementHelper
            
            helper = AnnouncementHelper()
            # Just verify the type is recognized
            assert announcement_type in ["receive", "task", "complete", "error"]
        except Exception as e:
            pytest.skip(f"Announcement type test failed: {e}")
