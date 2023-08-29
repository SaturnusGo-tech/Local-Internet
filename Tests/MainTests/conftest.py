import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import platform


@pytest.fixture(scope="function")
def driver():
    if platform.system() == "Darwin":
        driver = webdriver.Safari()
    else:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


# новая фикстура для очистки localStorage
@pytest.fixture(scope="function")
def clear_local_storage(driver):
    driver.execute_script("window.localStorage.clear();")
