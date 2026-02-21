import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

ATCODER_LOGIN_URL = "https://atcoder.jp/login"
ATCODER_BASE_URL = "https://atcoder.jp"


def _load_dotenv(path: str = ".env") -> None:
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, value = line.partition("=")
                    os.environ.setdefault(key.strip(), value.strip())
    except FileNotFoundError:
        pass


def _build_driver() -> webdriver.Chrome:
    chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
    service = Service(chromedriver_path) if chromedriver_path else None
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--remote-debugging-port=9222')
    if service:
        return webdriver.Chrome(service=service, options=options)
    return webdriver.Chrome(options=options)


def _wait_loaded(driver: webdriver.Chrome, timeout: int = 30) -> None:
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script('return document.readyState') == 'complete')


def _login_with_session_cookie(driver: webdriver.Chrome, session: str) -> None:
    """Inject a pre-obtained REVEL_SESSION cookie (avoids Cloudflare Turnstile)."""
    driver.get(ATCODER_BASE_URL)
    _wait_loaded(driver)
    driver.add_cookie({
        'name': 'REVEL_SESSION',
        'value': session,
        'domain': 'atcoder.jp',
        'path': '/',
    })


def _login_with_credentials(driver: webdriver.Chrome, username: str, password: str) -> None:
    """Login via the AtCoder login form."""
    driver.get(ATCODER_LOGIN_URL)
    _wait_loaded(driver)
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()
    _wait_loaded(driver)


def get_test_cases(
    url: str = "https://atcoder.jp/contests/abc392/tasks/abc392_a"
) -> list[tuple[str, str]]:
    _load_dotenv()
    session_cookie = os.getenv("ATCODER_SESSION")
    username = os.getenv("ATCODER_USER")
    password = os.getenv("ATCODER_PASSWORD")

    driver = _build_driver()
    result = []

    try:
        if session_cookie:
            _login_with_session_cookie(driver, session_cookie)
        elif username and password:
            _login_with_credentials(driver, username, password)

        driver.get(url)
        _wait_loaded(driver)

        for i in range(0, 20, 2):
            input_element = driver.find_element(By.ID, f"pre-sample{i}")
            input_text = input_element.get_property("textContent")

            output_element = driver.find_element(By.ID, f"pre-sample{i+1}")
            output_text = output_element.get_property("textContent")

            item = (input_text, output_text)
            if item in result:
                continue
            result.append(item)
    except NoSuchElementException:
        pass

    finally:
        driver.quit()

    return result


if __name__ == "__main__":
    get_test_cases()
