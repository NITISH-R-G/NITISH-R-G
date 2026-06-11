import re

def test_developer_class():
    with open('README.md', 'r') as f:
        content = f.read()

    # extract python code
    match = re.search(r'```python(.*?)```', content, re.DOTALL)
    if not match:
        raise Exception("Could not find python code in README.md")

    code = match.group(1).strip()

    # execute code in local namespace
    local_ns = {}
    exec(code, {}, local_ns)

    Developer = local_ns.get('Developer')
    if not Developer:
        raise Exception("Developer class not found in code")

    dev = Developer()

    assert dev.name == "Nitish R.G"
    assert "Data Science" in dev.role or "AI" in dev.role
    assert isinstance(dev.education, dict)
    assert isinstance(dev.focus, list)
    assert 'Advanced LLMs' in dev.focus
    assert 'Computer Vision' in dev.focus
    assert 'Full-Stack ML Integration' in dev.focus

    assert dev.get_mission() == 'Turning complex data into actionable intelligence 🚀'

    print("All tests passed!")

test_developer_class()
