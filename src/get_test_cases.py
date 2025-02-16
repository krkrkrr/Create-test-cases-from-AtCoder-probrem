import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


def get_test_cases(
    url: str = "https://atcoder.jp/contests/abc392/tasks/abc392_a"
) -> list[tuple[str, str]]:
    # Get ChromeDriver path from environment variable
    chromedriver_path = os.getenv('CHROMEDRIVER_PATH', '/usr/bin/chromedriver')

    # Setup Chrome WebDriver
    service = Service(chromedriver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--remote-debugging-port=9222')
    driver = webdriver.Chrome(service=service, options=options)

    result = []

    try:
        # Open the URL
        driver.get(url)

        # Wait for the page to load completely
        WebDriverWait(driver, 30).until(lambda d: d.execute_script(
            'return document.readyState') == 'complete')

        for i in range(0, 20, 2):
            # Get the input example
            input_element = driver.find_element(By.ID, f"pre-sample{i}")
            input_text = input_element.get_property("textContent")

            # Get the output example
            output_element = driver.find_element(By.ID, f"pre-sample{i+1}")
            output_text = output_element.get_property("textContent")

            item = (input_text, output_text)
            if item in result:
                continue
            result.append(item)
    except NoSuchElementException:
        pass

    finally:
        # Close the browser
        driver.quit()

    return result


if __name__ == "__main__":
    get_test_cases()
