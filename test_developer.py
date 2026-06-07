import unittest
import re
import io
import sys
from typing import Dict, List, Optional, Union

class TestDeveloperClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Extract the python code from README.md
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.search(r'```python\n(.*?)```', content, re.DOTALL)
        if not match:
            raise ValueError("Python code block not found in README.md")

        # We want to prevent the module from printing to stdout during import/exec
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            code = match.group(1)
            namespace = {"Dict": Dict, "List": List, "Optional": Optional, "Union": Union}
            exec(code, namespace)
            cls.Developer = namespace['Developer']
        finally:
            sys.stdout = original_stdout

    def setUp(self):
        self.dev = self.Developer()

    def test_initialization(self):
        """Test if the Developer instance initializes with correct attributes."""
        self.assertEqual(self.dev.name, "Nitish R.G")
        self.assertEqual(self.dev.role, "Data Science & AI Practitioner")
        self.assertDictEqual(
            self.dev.education,
            {
                "BS": "Data Science @ IIT Madras",
                "BE": "Computer Science Engineering @ SIET"
            }
        )
        self.assertListEqual(
            self.dev.focus,
            ["Advanced LLMs", "Computer Vision", "Full-Stack ML Integration"]
        )

    def test_get_mission(self):
        """Test the get_mission method returns the correct string."""
        self.assertEqual(
            self.dev.get_mission(),
            "Turning complex data into actionable intelligence 🚀"
        )

    def test_get_daily_status(self):
        """Test the get_daily_status method returns the correct string."""
        import datetime
        from unittest.mock import Mock

        # The Developer class is executed dynamically, so we must patch its specific globals
        dev_globals = self.dev.get_daily_status.__globals__
        original_datetime = dev_globals.get('datetime')

        mock_datetime = Mock()
        mock_date = Mock()
        mock_date.today.return_value = datetime.date(2023, 10, 27)
        mock_datetime.date = mock_date

        try:
            dev_globals['datetime'] = mock_datetime
            status = self.dev.get_daily_status()
        finally:
            if original_datetime:
                dev_globals['datetime'] = original_datetime
            else:
                del dev_globals['datetime']

        self.assertTrue(status.startswith("[2023-10-27] Status: Architecting intelligent systems"))

if __name__ == '__main__':
    unittest.main()
