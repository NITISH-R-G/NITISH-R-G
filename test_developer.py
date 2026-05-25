import unittest
import re
import io
import sys
from typing import Dict, List

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
            namespace = {"Dict": Dict, "List": List}
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

if __name__ == '__main__':
    unittest.main()
