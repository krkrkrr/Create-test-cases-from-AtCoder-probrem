import os
import sys
from .create_text_content import create_text_content_of_test, create_text_content_of_source_code


def initialize_environment() -> None:
    """Initialize the environment for the contest."""

    # Create pyproject.toml
    pyproject_toml_content = """
[project]
name = "Solve_contest"
version = "0.1.0"
requires-python = ">=3.10"

[project.optional-dependencies]
dev = ["pytest", "pytest-randomly", "pytest-watch"]
"""
    with open("pyproject.toml", 'w') as f:
        f.write(pyproject_toml_content)

    # Create __init__.py files
    for init_path in ["src/__init__.py", "tests/__init__.py"]:
        os.makedirs(os.path.dirname(init_path), exist_ok=True)
        with open(init_path, 'w') as f:
            f.write("")

    for probrem_name in ['a', 'b', 'c', 'd', 'e', 'f']:
        test_file_path = f"tests/test_{probrem_name}.py"
        source_code_file_path = f"src/{probrem_name}.py"

        os.makedirs(os.path.dirname(test_file_path), exist_ok=True)
        os.makedirs(os.path.dirname(source_code_file_path), exist_ok=True)

        with open(test_file_path, 'w') as f:
            f.write(create_text_content_of_test(probrem_name, []))

        with open(source_code_file_path, 'w') as f:
            f.write(create_text_content_of_source_code())


def main() -> None:
    initialize_environment()


if __name__ == "__main__":
    main()
