import unittest
from unittest.mock import patch, MagicMock
import datetime
import re

class TestDeveloper(unittest.TestCase):
    def setUp(self):
        # Extract code from README.md
        with open('README.md', 'r', encoding='utf-8') as f:
            readme_content = f.read()

        match = re.search(r'```python\n(.*?)```', readme_content, re.DOTALL)
        if not match:
            self.fail("No Python code block found in README.md")

        code = match.group(1)
        # We execute the code in a new namespace dictionary
        self.namespace = {'__name__': 'test_module'}
        exec(code, self.namespace)
        self.Developer = self.namespace['Developer']

    def test_get_daily_status(self):
        # We need to mock datetime.date.today within the executed code's namespace
        # The module has already imported datetime
        with patch.object(self.namespace['datetime'], 'date') as mock_date:
            # Set up the mock return value for isoformat()
            mock_today = MagicMock()
            mock_today.isoformat.return_value = '2023-10-25'
            mock_date.today.return_value = mock_today

            dev = self.Developer()

            # Mock generate_system_joke to make the test deterministic
            dev.generate_system_joke = MagicMock(return_value="Mocked Joke")

            status = dev.get_daily_status()

            expected_line1 = "[2023-10-25] Status: Architecting intelligent systems... 🧠✨"
            expected_line2 = "System Humor Load: Mocked Joke"
            expected_status = expected_line1 + chr(10) + expected_line2

            self.assertEqual(status, expected_status)

            # Verify the mock was called
            dev.generate_system_joke.assert_called_once()
            mock_date.today.assert_called_once()

if __name__ == '__main__':
    unittest.main()
