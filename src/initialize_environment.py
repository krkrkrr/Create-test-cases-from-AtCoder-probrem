import os
import sys
from .create_text_content import create_text_content_of_test, create_text_content_of_source_code


def initialize_environment(contest_home_url: str) -> None:
    """
    Initialize the environment for the contest.
    
    Args:
        contest_home_url (str): The URL of the contest home.
    """
    contest_name = contest_home_url.split('/')[-1]

    # Create pyproject.toml
    pyproject_toml_content = f"""
[project]
name = "Solve_{contest_name}"
version = "0.1.0"
requires-python = ">=3.10"

[project.optional-dependencies]
dev = ["pytest", "pytest-randomly", "pytest-watch"]
"""
    pyproject_toml_file_path = "pyproject.toml"
    with open(pyproject_toml_file_path, 'w') as pyproject_toml_file:
        pyproject_toml_file.write(pyproject_toml_content)

    # Create the src directory and the __init__.py file
    src_init_file_path_list = ["src/__init__.py", "tests/__init__.py"]
    for src_init_file_path in src_init_file_path_list:
        os.makedirs(os.path.dirname(src_init_file_path), exist_ok=True)
        with open(src_init_file_path, 'w') as src_init_file:
            src_init_file.write("")

    probrem_names = ['a', 'b', 'c', 'd', 'e', 'f']
    for probrem_name in probrem_names:
        # Define file paths
        test_file_path = f"tests/test_{probrem_name}.py"
        source_code_file_path = f"src/{probrem_name}.py"

        # Create directories if they don't exist
        os.makedirs(os.path.dirname(test_file_path), exist_ok=True)
        os.makedirs(os.path.dirname(source_code_file_path), exist_ok=True)

        # Create the test file content
        test_content = create_text_content_of_test(probrem_name, [])

        # Write the test file
        with open(test_file_path, 'w') as test_file:
            test_file.write(test_content)

        # Create the source code file content
        source_code_content = create_text_content_of_source_code()

        # Write the source code file
        with open(source_code_file_path, 'w') as source_code_file:
            source_code_file.write(source_code_content)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: init <contest_home_url>", file=sys.stderr)
        sys.exit(1)
    contest_home_url = sys.argv[1]
    initialize_environment(contest_home_url)


if __name__ == "__main__":
    main()
