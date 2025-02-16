# Create-test-cases-from-AtCoder-probrem
Create an automated test environment from the AtCoder ABC contest page.

## Requirements
### WSL
1. Install chromium
```
$ sudo apt-get install -y chromium-browser chromium-chromedriver
```

1. Check chromedriver parent path
```
$ which chromedriver
```

1. Add chromedriver path to environment
```
$ export PATH=$PATH:<chrome driver parent path>
$ export CHROMEDRIVER_PATH=<chrome driver parent path>/chromedriver
```


## Usage
### Quick Start
1. Install the package
```
$ python -m venv .venv --upgrade-deps
$ source .venv/bin/activate
$ python -m pip install .
```

1. Create required files
```
$ cd path/to/root/for/environment
$ python path/to/src/initialize_environment.py https://atcoder.jp/contests/{contest_name}
```

### In develop
1. Install the package
```
$ python -m venv .venv --upgrade-deps
$ source .venv/bin/activate
$ python -m pip install -e '.[dev]'
```

1. Run the script
```
$ pytest
```