import unittest
import re
import sys
import ast

class DeveloperMock:
    """A mock class to hold values parsed securely via AST."""
    def __init__(self):
        self.name = None
        self.role = None
        self.education = None
        self.focus = None
        self._mission = None

    def get_mission(self):
        return self._mission

class TestDeveloperClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Extract the python code from README.md
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.search(r'```python\n(.*?)```', content, re.DOTALL)
        if not match:
            raise ValueError("Python code block not found in README.md")

        code = match.group(1)
        tree = ast.parse(code)

        # Safely extract data from the AST instead of executing arbitrary code
        @staticmethod
        def mock_developer_factory():
            dev = DeveloperMock()
            for node in tree.body:
                if isinstance(node, ast.ClassDef) and node.name == 'Developer':
                    for item in node.body:
                        if isinstance(item, ast.AnnAssign):
                            if item.target.id == 'name':
                                dev.name = ast.literal_eval(item.value)
                            elif item.target.id == 'role':
                                dev.role = ast.literal_eval(item.value)
                            elif item.target.id in ('education', 'focus') and isinstance(item.value, ast.Call):
                                for kw in item.value.keywords:
                                    if kw.arg == 'default_factory' and isinstance(kw.value, ast.Lambda):
                                        val = ast.literal_eval(kw.value.body)
                                        if item.target.id == 'education':
                                            dev.education = val
                                        elif item.target.id == 'focus':
                                            dev.focus = val
                        elif isinstance(item, ast.FunctionDef) and item.name == 'get_mission':
                            for stmt in item.body:
                                if isinstance(stmt, ast.Return):
                                    dev._mission = ast.literal_eval(stmt.value)
            return dev

        cls.Developer = mock_developer_factory

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
