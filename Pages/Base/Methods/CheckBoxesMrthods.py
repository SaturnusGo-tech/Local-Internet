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


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        self.logger.addHandler(self.handler)

    def log_action(self, message):
        self.logger.debug(message)


class CheckBoxesMethods(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def assert_checkbox_selected(self, checkbox_locator):
        checkbox = self.driver.find_element(*checkbox_locator)
        assert checkbox.is_selected(), "Чекбокс не выбран"
        self.log_action("Утверждено, что чекбокс выбран")

    def assert_checkbox_not_selected(self, checkbox_locator):
        checkbox = self.driver.find_element(*checkbox_locator)
        assert not checkbox.is_selected(), "Чекбокс выбран"
        self.log_action("Утверждено, что чекбокс не выбран")

    def assert_checkbox_enabled(self, checkbox_locator):
        checkbox = self.driver.find_element(*checkbox_locator)
        assert checkbox.is_enabled(), "Чекбокс неактивен"
        self.log_action("Утверждено, что чекбокс активен")

    def assert_checkbox_disabled(self, checkbox_locator):
        checkbox = self.driver.find_element(*checkbox_locator)
        assert not checkbox.is_enabled(), "Чекбокс активен"
        self.log_action("Утверждено, что чекбокс неактивен")

    def perform_load_test(self, checkbox_locator, iterations=10):
        successes = 0
        failures = 0

        for i in range(iterations):
            checkbox = self.driver.find_element(*checkbox_locator)
            checkbox.click()
            time.sleep(1)  # Задержка для нагрузочного тестирования
            checkbox.click()

            # Проверяем состояние чекбокса после клика
            if checkbox.is_selected():
                successes += 1
                self.log_action(f"Нагрузочное тестирование чекбокса (итерация {i+1}) - успешно")
            else:
                failures += 1
                self.log_action(f"Нагрузочное тестирование чекбокса (итерация {i+1}) - неудачно")

        self.log_action(f"Успешные итерации: {successes}/{iterations}")
        self.log_action(f"Неудачные итерации: {failures}/{iterations}")
