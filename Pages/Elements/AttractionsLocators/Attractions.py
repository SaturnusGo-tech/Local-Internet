import pytest
import requests
from selenium.common import TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Local_Internet.Pages.Base.Methods.Methods import BaseMethods
from Local_Internet.Pages.Base.Methods.Base import BaseActions
from Local_Internet.Pages.Base.Methods.CheckBoxesMrthods import CheckBoxesMethods
from Local_Internet.Pages.Base.URLS.Attractions.URL import AttractionsURL


class AttractionsList(BaseActions, BaseMethods, CheckBoxesMethods):
    CountryItems = (By.XPATH, '//*[@id="attraction-search-form"]/div[1]/input')
    GetItemsCountryList = (By.XPATH, '//*[@id="attraction-search-form"]/div[1]/div')
    CityItems = (By.XPATH, '//*[@id="attraction-search-form"]/div[2]/input')
    GetItemsCityList = (By.XPATH, '//*[@id="attraction-search-form"]/div[2]/div')

    CountryItem = (By.XPATH, '//*[@id="attraction-search-form"]/div[1]/div/ul/li[2]')
    CityItem = (By.XPATH, '//*[@id="attraction-search-form"]/div[2]/div/ul/li[2]')
    Submit = (By.XPATH, '//*[@id="attraction-search-form"]/div[3]/button')

    GetAttributeItem = (By.XPATH, '/html/body/div[6]/h1')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def ScrollView(self):
        try:
            self.window_scroll_by(0, 450)
            print("Действие: Элемент списка стран в зоне видимости")
        except Exception:
            print("Ошибка: Скролл страницы заблокирован")

    def PageLoaded(self, expected_url, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(lambda driver: driver.current_url == expected_url)
            assert self.driver.current_url == expected_url, f"Ошибка: текущий URL не соответствует ожидаемому URL. Ожидалось: {expected_url}, Получено: {self.driver.current_url}"
            print("Страница успешно загрузилась и готова к тесту")
        except TimeoutException:
            raise Exception(f"Ошибка: Страница не загрузилась в течение {timeout} секунд")

    def OpenCountryItems(self, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(AttractionsList.CountryItems)
            )
            element.click()
            print("Действие: Кликнули на элемен CountryItem, успешно")
        except TimeoutException:
            print("Ошибка:Элемент CountryItem не кликабельный")

    def GetCountryListItems(self, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(AttractionsList.GetItemsCountryList)
            )
            print("Действие: Список стран присутствует")
        except TimeoutException:
            print("Ошибка: Список стран отсутствует")

    def SelectCountryItem(self, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(AttractionsList.CountryItem)
            )
            element.click()
            print("Действие: Кликнули на элемент CountryItem, успешно")
        except TimeoutException:
            print("Ошибка: Элемент CountryItem не кликабельный")

    def OpenCityItems(self, timeout=10):
        try:
            self.click_element(AttractionsList.CityItems, timeout)
            print("Действие: Кликнули на элемент CityItems, успешно")
        except ElementNotInteractableException:
            print("Ошибка: Элемент CityItems не кликабельный")

    def GetCityListItems(self, timeout=10):
        if self.is_element_present(AttractionsList.GetItemsCityList, timeout):
            print("Действие: Список городов присутствует")
        else:
            print("Ошибка: Список городов отсутствует")

    def SelectCityItem(self, timeout=10):
        try:
            self.click_element(AttractionsList.CityItem, timeout)
            print("Действие: Кликнули на элемент CityItem, успешно")
        except ElementNotInteractableException:
            print("Ошибка: Элемент CityItem не кликабельный")

    def OpenAndReturnItem(self, item_locator, item_name, timeout=10):
        # Клик по элементу
        try:
            self.click_element(item_locator, timeout)
        except ElementNotInteractableException:
            raise Exception(f"Ошибка: Элемент {item_name} не кликабельный")
        print(f"Действие: Кликнули на элемент {item_name} для открытия новой вкладки")

        # Проверка, что открылась новая вкладка
        window_handles = self.driver.window_handles
        assert len(window_handles) >= 2, f"Проверка: Ожидалось, что будет открыта вторая вкладка для {item_name}"

        # Переключение на новую вкладку
        self.driver.switch_to.window(window_handles[1])
        print("Проверка: Переключились на вторую вкладку")

        # Получение URL текущей страницы
        current_url = self.driver.current_url

        # Отправка GET-запроса на URL текущей страницы и проверка кода ответа
        try:
            response = requests.get(current_url, timeout=10)
        except requests.exceptions.Timeout:
            raise Exception(f"Ошибка: Получение кода статуса для {item_name} заняло слишком много времени")
        status_code = response.status_code
        print(f"Код статуса страницы {item_name}: {status_code}")
        if status_code != 200:
            raise Exception(f"Ошибка элемента {item_name}: Код статуса {status_code}")

        # Подтягивание аттрибута с другой страницы
        GetAttributeItem = (By.XPATH, '/html/body/div[6]/h1')
        try:
            wait = WebDriverWait(self.driver, timeout)
            GetAttributeItem = wait.until(EC.visibility_of_element_located(GetAttributeItem))
        except TimeoutException:
            raise Exception(f"Ошибка: Элемент на странице {item_name} не стал видимым в течение заданного времени")
        GetAttributeItem_text = GetAttributeItem.text
        print(f"Текст элемента data_count: {GetAttributeItem_text}")

        # Закрытие текущей вкладки и переключение на предыдущую
        self.driver.close()
        self.driver.switch_to.window(window_handles[0])
        print("Действие: Вернулись на предыдущую вкладку")
