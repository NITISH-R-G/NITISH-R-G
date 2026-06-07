import unittest
import re
import ast

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
        cls.Developer = cls._get_developer_class_from_ast(code)

    @staticmethod
    def _get_developer_class_from_ast(code):
        tree = ast.parse(code)
        class_attrs = {}
        mission_return = None

        for node in tree.body:
            if isinstance(node, ast.ClassDef) and node.name == 'Developer':
                for stmt in node.body:
                    if isinstance(stmt, ast.AnnAssign):
                        target = getattr(stmt.target, 'id', None)
                        if not target: continue
                        if isinstance(stmt.value, ast.Constant):
                            class_attrs[target] = getattr(stmt.value, 'value', None)
                        elif isinstance(stmt.value, ast.Call) and getattr(stmt.value.func, 'id', '') == 'field':
                            for kw in stmt.value.keywords:
                                if kw.arg == 'default_factory' and isinstance(kw.value, ast.Lambda):
                                    try:
                                        val = ast.literal_eval(kw.value.body)
                                        class_attrs[target] = val
                                    except Exception:
                                        pass
                    elif isinstance(stmt, ast.FunctionDef) and stmt.name == 'get_mission':
                        for func_stmt in stmt.body:
                            if isinstance(func_stmt, ast.Return) and getattr(func_stmt, 'value', None):
                                if isinstance(func_stmt.value, ast.Constant):
                                    mission_return = func_stmt.value.value
                                break

        class DummyDeveloper:
            def __init__(self):
                for k, v in class_attrs.items():
                    setattr(self, k, v)
            def get_mission(self):
                return mission_return

        return DummyDeveloper

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
