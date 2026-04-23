"""Integration tests for beep-skills."""

import pytest
import subprocess
import sys
from pathlib import Path


class TestIntegration:
    """Integration test cases."""

    def test_package_importable(self):
        """Test that the package can be imported."""
        try:
            import audio_announcement
            assert True
        except ImportError:
            pytest.skip("Package not installed")

    def test_scripts_exist(self):
        """Test that required scripts exist."""
        skill_dir = Path(__file__).parent.parent
        
        required_files = [
            "scripts/announce.py",
            "audio_announcement/__init__.py",
            "audio_announcement/cli.py",
        ]
        
        for file_path in required_files:
            full_path = skill_dir / file_path
            assert full_path.exists(), f"Missing required file: {file_path}"

    def test_setup_py_exists(self):
        """Test that setup.py exists."""
        skill_dir = Path(__file__).parent.parent
        setup_py = skill_dir / "setup.py"
        assert setup_py.exists()

    def test_readme_exists(self):
        """Test that README.md exists."""
        skill_dir = Path(__file__).parent.parent
        readme = skill_dir / "README.md"
        assert readme.exists()

    def test_license_exists(self):
        """Test that LICENSE exists."""
        skill_dir = Path(__file__).parent.parent
        license_file = skill_dir / "LICENSE"
        assert license_file.exists()


class TestVersionConsistency:
    """Test version consistency across files."""

    def test_setup_py_version(self):
        """Test that setup.py has a valid version."""
        skill_dir = Path(__file__).parent.parent
        setup_py = skill_dir / "setup.py"
        
        content = setup_py.read_text(encoding="utf-8")
        assert 'version=' in content
        assert "2.1.0" in content

    def test_meta_json_version(self):
        """Test that _meta.json has a valid version."""
        skill_dir = Path(__file__).parent.parent
        meta_json = skill_dir / "_meta.json"
        
        import json
        data = json.loads(meta_json.read_text(encoding="utf-8"))
        assert "version" in data
        assert data["version"] == "2.1.0"

    def test_skill_md_version(self):
        """Test that SKILL.md mentions the version."""
        skill_dir = Path(__file__).parent.parent
        skill_md = skill_dir / "SKILL.md"
        
        content = skill_md.read_text(encoding="utf-8")
        assert "2.1.0" in content
