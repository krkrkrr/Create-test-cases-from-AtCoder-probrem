from string import Template


def create_text_content_of_test(probrem_name: str,
                                test_cases: set[tuple[str, str]]) -> str:
    """
    Create test cases for the function solve.
    
    Args:
        probrem_name (str): The name of the probrem.
        test_cases (set[tuple[str, str]]): A set of test cases.
    
    Returns:
        str: The test cases for the function solve.
    """
    test_template = Template("""

def test_${probrem_name}_solve_${index}(capsys, monkeypatch):
    actual = \"\"\"\\
${input}

\"\"\"
    monkeypatch.setattr('sys.stdin', io.StringIO(actual))
    solve()
    expected = \"\"\"\\
${output}

\"\"\"
    assert capsys.readouterr().out == expected
""")

    tests = []
    for index, (input_str, output_str) in enumerate(test_cases, start=1):
        tests.append(
            test_template.substitute(probrem_name=probrem_name,
                                     index=index,
                                     input=input_str.strip(),
                                     output=output_str.strip()))

    return f"""
from a import solve

import io
{''.join(tests)}
"""


def create_text_content_of_source_code() -> str:
    """
    Create the source code template for the function solve.
    
    Returns:
        str: The source code template for the function solve.
    """
    return """
from sys import stdin


def solve() -> None:
    # N = int(input())
    # N, M = [int(x) for x in stdin.readline().rstrip().split()]
    raise NotImplementedError


if __name__ == '__main__':
    solve()
"""
