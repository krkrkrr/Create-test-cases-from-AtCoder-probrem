import pytest
from get_test_cases import get_test_cases
from create_tests import create_tests


def test_get_test_cases():
    # Assert
    actual = 'https://atcoder.jp/contests/abc392/tasks/abc392_a'
    expect = [
        ('3 15 5\n', 'Yes\n'),
        ('5 3 2\n', 'No\n'),
        ('3 3 9\n', 'Yes\n'),
    ]

    # Act
    result = get_test_cases(actual)

    # Assert
    assert result == expect


def test_create_tests():
    # Assert
    actual = [
        ('3 15 5\n', 'Yes\n'),
        ('5 3 2\n', 'No\n'),
        ('3 3 9\n', 'Yes\n'),
    ]
    expect = """
from a import solve

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
    result = create_tests(actual)

    # Assert
    assert result == expect


if __name__ == "__main__":
    pytest.main()
