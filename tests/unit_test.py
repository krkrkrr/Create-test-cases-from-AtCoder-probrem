import pytest
from src.create_text_content import create_text_content_of_test
from src.create_text_content import create_text_content_of_source_code


def test_create_text_content_of_test():
    # Assert
    actual_test_cases = [
        ('3 15 5\n', 'Yes\n'),
        ('5 3 2\n', 'No\n'),
        ('3 3 9\n', 'Yes\n'),
    ]
    actual_probrem_name = 'a'
    expect = """from src.a import solve

import io


def test_a_solve_1(capsys, monkeypatch):
    actual = \"\"\"\\
3 15 5
\"\"\"
    monkeypatch.setattr('sys.stdin', io.StringIO(actual))
    solve()
    expected = \"\"\"\\
Yes
\"\"\"
    assert capsys.readouterr().out == expected


def test_a_solve_2(capsys, monkeypatch):
    actual = \"\"\"\\
5 3 2
\"\"\"
    monkeypatch.setattr('sys.stdin', io.StringIO(actual))
    solve()
    expected = \"\"\"\\
No
\"\"\"
    assert capsys.readouterr().out == expected


def test_a_solve_3(capsys, monkeypatch):
    actual = \"\"\"\\
3 3 9
\"\"\"
    monkeypatch.setattr('sys.stdin', io.StringIO(actual))
    solve()
    expected = \"\"\"\\
Yes
\"\"\"
    assert capsys.readouterr().out == expected

"""
    # Act
    result = create_text_content_of_test(actual_probrem_name,
                                         actual_test_cases)

    # Assert
    assert result == expect


def test_create_text_content_of_source_code():
    # Assert
    expect = """from sys import stdin


def solve() -> None:
    # N = int(input())
    # N, M = [int(x) for x in input().split()]
    raise NotImplementedError


if __name__ == '__main__':
    solve()
"""

    # Act
    result = create_text_content_of_source_code()

    # Assert
    assert result == expect


if __name__ == "__main__":
    pytest.main()
