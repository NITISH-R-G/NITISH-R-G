import unittest
import re
import datetime

# Extract code from README.md
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the python block
match = re.search(r'```python\n(.*?)\n```', content, re.DOTALL)
if not match:
    raise ValueError("Could not find Python code block in README.md")

code = match.group(1)

# Remove the if __name__ == "__main__": block
code_to_exec = re.sub(r'if __name__ == "__main__":.*', '', code, flags=re.DOTALL)

# Execute the code in a new namespace
namespace = {}
exec(code_to_exec, namespace)

Developer = namespace['Developer']

class TestDeveloper(unittest.TestCase):
    def setUp(self):
        self.dev = Developer()

    def test_get_mission(self):
        expected_mission = "Turning complex data into actionable intelligence 🚀"
        self.assertEqual(self.dev.get_mission(), expected_mission)

    def test_get_daily_status(self):
        status = self.dev.get_daily_status()
        today = datetime.date.today().isoformat()
        expected_status = f"[{today}] Status: Building scalable AI solutions... 🚀"
        self.assertEqual(status, expected_status)

    def test_generate_system_joke(self):
        expected_jokes = [
            "Why did the neural network break up with the decision tree? It found someone more fully connected! 💔🕸️",
            "A SQL query goes into a bar, walks up to two tables and asks... 'Can I join you?' 🍻🗄️",
            "I'd tell you a joke about UDP, but you probably wouldn't get it. 📡💨",
            "There are 10 types of people in this world: those who understand binary, and those who don't. 💻🔢",
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛🌑"
        ]
        joke = self.dev.generate_system_joke()
        self.assertIn(joke, expected_jokes)

if __name__ == '__main__':
    unittest.main()
