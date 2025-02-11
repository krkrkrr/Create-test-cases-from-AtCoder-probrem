import pytest
from get_test_cases import get_test_cases


def test_get_test_cases():
    # Assert
    actual = 'https://atcoder.jp/contests/abc392/tasks/abc392_a'
    expect = set([
        ('3 15 5\n', 'Yes\n'),
        ('5 3 2\n', 'No\n'),
        ('3 3 9\n', 'Yes\n'),
    ])

    # Act
    result = get_test_cases(actual)

    # Assert
    assert result == expect


if __name__ == "__main__":
    pytest.main()
