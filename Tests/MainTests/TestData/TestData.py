import random
from selenium.webdriver.common.by import By


class CheckBoxes:
    ATTRACTION = [
        (By.CSS_SELECTOR, '[for="vehicle1"]'),
        (By.CSS_SELECTOR, '[for="vehicle4"]'),
        (By.CSS_SELECTOR, '[for = "vehicle7"]'),
        (By.CSS_SELECTOR, '[for = "vehicle10"]'),
        (By.CSS_SELECTOR, '[for = "vehicle13"]'),
        (By.CSS_SELECTOR, '[for = "vehicle16"]'),
        (By.CSS_SELECTOR, '[for = "vehicle19"]'),
        (By.CSS_SELECTOR, '[for = "vehicle22"]'),
        (By.CSS_SELECTOR, '[for = "vehicle2"]'),
        (By.CSS_SELECTOR, '[for = "vehicle5"]'),
        (By.CSS_SELECTOR, '[for = "vehicle8"]'),
        (By.CSS_SELECTOR, '[for = "vehicle11"]'),
        (By.CSS_SELECTOR, '[for ="vehicle14"]'),
        (By.CSS_SELECTOR, '[for ="vehicle17"]'),
        (By.CSS_SELECTOR, '[for ="vehicle20"]'),
        (By.CSS_SELECTOR, '[for ="vehicle3"]'),
        (By.CSS_SELECTOR, '[for ="vehicle6"]'),
        (By.CSS_SELECTOR, '[for ="vehicle9"]'),
        (By.CSS_SELECTOR, '[for ="vehicle12"]'),
        (By.CSS_SELECTOR, '[for ="vehicle15"]'),
        (By.CSS_SELECTOR, '[for ="vehicle18"]'),
        (By.CSS_SELECTOR, '[for ="vehicle21"]'),
        (By.CSS_SELECTOR, '[for ="vehicle23"] '),

    ]

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @classmethod
    def get_random_locator(cls):
        return random.choice(cls.ATTRACTION)
