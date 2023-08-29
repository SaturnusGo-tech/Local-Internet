import random
import time
import logging
from datetime import datetime
from io import BytesIO
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from functools import wraps
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementNotVisibleException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        logging.basicConfig(level=logging.ERROR)

class BaseActions(Base):

    def click_element(self, by_locator, timeout=10, error_message="Failed to click on element"):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(by_locator)
            )
            element.click()
            self.logger.info(f"Clicked on element with locator: {by_locator}")
        except TimeoutException:
            self.logger.error(f"{error_message}: Timeout - Failed to click on element with locator: {by_locator}")
            raise
        except ElementNotInteractableException:
            self.logger.error(
                f"{error_message}: Element not interactable - Failed to click on element with locator: {by_locator}")
            raise
        except Exception as e:
            self.logger.error(
                f"{error_message}: Unknown exception - Failed to click on element with locator: {by_locator}")
            self.logger.exception(e)
            raise

    def switch_to_new_tab(self):
        try:
            # Get the handles of all open tabs/windows
            handles = self.driver.window_handles

            if len(handles) > 1:
                # Switch to the new tab/window (last one)
                new_tab_handle = handles[-1]
                self.driver.switch_to.window(new_tab_handle)
            else:
                raise Exception("New tab/window was not opened.")
        except Exception as e:
            print(f"Failed to switch to new tab: {str(e)}")

    def get_response_code(self, url):
        try:
            response = requests.get(url)
            return response.status_code
        except Exception as e:
            print(f"Error while checking response code: {str(e)}")
            return None

    def select_random_checkboxes(checkbox_elements, num_to_select):
        """
        Selects a random number of checkboxes from a list of checkbox elements.

        :param checkbox_elements: List of WebElement instances representing the checkboxes
        :param num_to_select: Number of checkboxes to select
        """
        # Shuffle the list of checkbox elements
        random.shuffle(checkbox_elements)

        # Select the first 'num_to_select' checkboxes from the shuffled list
        for i in range(num_to_select):
            checkbox = checkbox_elements[i]
            checkbox.click()

    def random_click_on_screen(self):
        action = ActionChains(self.driver)

        # Примерно узнаем размеры окна браузера (это не размеры экрана, а размеры видимой части веб-страницы)
        window_size = self.driver.get_window_size()
        width = window_size["width"]
        height = window_size["height"]

        # Генерируем случайные координаты
        x = random.randint(0, width)
        y = random.randint(0, height)

        # Двигаемся к случайной точке и кликаем
        action.move_by_offset(x, y).click().perform()

        # Возвращаем курсор обратно
        action.move_by_offset(-x, -y).perform()

    def wait_until_element_is_clickable(self, by_locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(by_locator))
            return element
        except TimeoutException:
            return False

    def get_random_locators(self, xpath, number_of_locators):
        elements = self.driver.find_elements(By.CLASS_NAME, xpath)

        if len(elements) < number_of_locators:
            raise Exception(f"Не достаточно элементов для выбора: {len(elements)} < {number_of_locators}")

        random_elements = random.sample(elements, number_of_locators)
        return random_elements

    def click_all_items(self, locators):
        for locator in locators:
            try:
                element = WebDriverWait(self, 10).until(
                    EC.element_to_be_clickable(locator)
                )
                element.click()
            except Exception as e:
                print(f"Error clicking element with locator {locator}: {str(e)}")


