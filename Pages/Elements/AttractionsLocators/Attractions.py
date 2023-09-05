import logging
import time

import pytest
import requests
from selenium.common import TimeoutException, ElementNotInteractableException, ElementClickInterceptedException, \
    NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Local_Internet.Pages.Base.Methods.Methods import BaseMethods
from Local_Internet.Pages.Base.Methods.Base import BaseActions
from Local_Internet.Pages.Base.Methods.CheckBoxesMrthods import CheckBoxesMethods
from Local_Internet.Pages.Base.URLS.Attractions.URL import AttractionsURL

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


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

        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.number_of_windows_to_be(2))
        except TimeoutException:
            raise Exception(f"Ошибка: Не удалось открыть новую вкладку в течение {timeout} секунд")

        # Переключение на новую вкладку
        window_handles = self.driver.window_handles
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


class ThematicRedirect(BaseActions, BaseMethods, CheckBoxesMethods):
    TopicItem = (By.XPATH, '//*[@id="all__topics-btn"]')
    NameItem1 = (By.XPATH, '/html/body/div[5]/div/div[2]/a[1]')
    NameItem2 = (By.XPATH, '/html/body/div[5]/div/div[2]/a[3]')
    NameItem3 = (By.XPATH, '/html/body/div[5]/div/div[2]/a[4]')

    MoveItems = (By.XPATH, '/html/body/div[5]/div/button[2]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def ScrollView(self):
        try:
            self.window_scroll_by(0, 650)
            print("Действие: Элемент списка стран в зоне видимости")
        except Exception:
            print("Ошибка: Скролл страницы заблокирован")

    def PageLoaded(self, expected_url, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(lambda driver: driver.current_url == expected_url)
            assert self.driver.current_url == expected_url, f" Ошибка: Страница не доступна или не загрузилась ошибка 404 Ожидалось:{expected_url}  получено {self.driver.current_url}"
            print("Действие: Страница успешно загружена и готова к тесту")
        except TimeoutException:
            raise Exception(f"Ошибка: Страница не загрузилась в течение {timeout} секунд")

    def TopicItemExist(self, timeout=10):
        if self.is_element_present(ThematicRedirect.NameItem1, timeout):
            print("Элемент Все темы активный и присутствует в блоке тематик")
        else:
            print("Ошибка:элемент Все темы не активный либо не присутствует в блоке тематик ")

    def NameItemsExist(self, item_locator, item_name, timeout=10):
        # Клик по элементу
        try:
            self.click_element(item_locator, timeout)
        except ElementNotInteractableException:
            raise Exception(f"Ошибка: Элемент {item_name} не кликабельный")
        print(f"Действие: Кликнули на элемент {item_name} для открытия новой вкладки")

        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.number_of_windows_to_be(2))
        except TimeoutException:
            raise Exception(f"Ошибка: Не удалось открыть новую вкладку в течение {timeout} секунд")

        # Переключение на новую вкладку
        window_handles = self.driver.window_handles
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

    # Метод отработает в случае small size экрана
    """def MoveItem(self, timeout=10): 
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(ThematicRedirect.MoveItems)
            )
            success = self.click_in_loop4(ThematicRedirect.MoveItems)
            if not success:
                raise Exception("Ошибка: Не удалось прокликать элемент MoveItems 4 раза")
            print("Действие: loop успешно прокликал элемент MoveItems ")
        except TimeoutException:
            print(f"Ошибка: Элемент MoveItems не стал кликабельным в течение {timeout} секунд")
        except ElementNotInteractableException:
            print("Ошибка: Элемент MoveItems недоступен по этому локатору либо перекрыт другим и недоступен")"""


class GettingStatusLinksBlocks(BaseActions, BaseMethods, CheckBoxesMethods):
    ArtItems1 = (By.XPATH, '/html/body/section[2]/div/div/div/div[1]/div[1]/a[1]/img')
    ArtItems2 = (By.XPATH, '/html/body/section[2]/div/div/div/div[2]/div[1]/a[1]/img')
    ArtItems3 = (By.XPATH, '/html/body/section[2]/div/div/div/div[3]/div[1]/a[1]/img')
    ArtItems4 = (By.XPATH, '/html/body/section[2]/div/div/div/div[4]/div[1]/a[1]/img')
    ArtItems5 = (By.XPATH, '/html/body/section[2]/div/div/div/div[5]/div[1]/a[1]/img')
    ArtItems6 = (By.XPATH, '/html/body/section[2]/div/div/div/div[6]/div[1]/a[1]/img')
    ArtItems7 = (By.XPATH, '/html/body/section[2]/div/div/div/div[7]/div[1]/a[1]/img')
    ArtItems8 = (By.XPATH, '/html/body/section[2]/div/div/div/div[8]/div[1]/a[1]/img')
    ArtItems9 = (By.XPATH, '/html/body/section[2]/div/div/div/div[9]/div[1]/a[1]/img')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def ScrollView(self):
        try:
            self.window_scroll_by(0, 750)
            print("Действие: Элемент блоков достопримечательностей в зоне видимости")
        except Exception:
            print("Ошибка: Скролл страницы заблокирован")

    def AttractionsItemsLinksRedirect(self, item_locator, item_name, timeout=10):
        # Клик по элементу
        try:
            self.click_element(item_locator, timeout)
        except ElementNotInteractableException:
            raise Exception(f"Ошибка: Элемент {item_name} не кликабельный")
        print(f"Действие: Кликнули на элемент {item_name} для открытия новой вкладки")

        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.number_of_windows_to_be(2))
        except TimeoutException:
            raise Exception(f"Ошибка: Не удалось открыть новую вкладку в течение {timeout} секунд")

        # Переключение на новую вкладку
        window_handles = self.driver.window_handles
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
        GetAttributeItem = (By.XPATH, '/html/body/div[4]/ul')
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

    def ScrollView_6(self):
        try:
            self.window_scroll_by(0, 1350)
            print("Действие: Элемент блоков достопримечательностей в зоне видимости")
        except Exception:
            print("Ошибка: Скролл страницы заблокирован")


class NewAttractionsItems(BaseActions, BaseMethods, CheckBoxesMethods):
    NewAttractionsItem1 = (By.XPATH, '/html/body/section[3]/div/div[2]/div/div/div[3]/div[1]/a[1]/img')
    NewAttractionsItem2 = (By.XPATH, '/html/body/section[3]/div/div[2]/div/div/div[3]/div[2]/a[1]')
    NewAttractionsItem3 = (By.XPATH, '/html/body/section[3]/div/div[2]/div/div/div[7]/div[1]/a[1]/img')
    NewAttractionsItem4 = (By.XPATH, '/html/body/section[3]/div/div[2]/div/div/div[8]/div[2]/a[1]')
    OpenAttractionItem = (By.XPATH, '/html/body/section[3]/div/div[2]/div/div/div[3]/div[1]/a[2]')
    GetAttributeItem = (By.XPATH, '/html/body/main/section[1]/div/div/div/div[1]/h1')
    AttractionsTitle = (By.XPATH, '//*[@id="page-header"]/section[2]/div/div[1]/h1')

    def scroll_view(self):
        try:
            self.window_scroll_by(0, 2250)
            print("Действие: Элемент блоков достопримечательностей в зоне видимости")
        except Exception:
            print("Ошибка: Скролл страницы заблокирован")

    def attractions_thematic_links_redirect(self, item_locator, item_name, timeout=10):
        # Добавляем явное ожидание
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(item_locator)
            )
        except TimeoutException:
            raise Exception(f"Ошибка: Элемент {item_name} не стал кликабельным в течение {timeout} секунд")

        # Клик по элементу
        try:
            element.click()
        except ElementNotInteractableException:
            raise Exception(f"Ошибка: Элемент {item_name} не кликабельный")
        print(f"Действие: Кликнули на элемент {item_name} для открытия страницы")

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

        # Подтягивание аттрибута с страницы

        # Возвращение на предыдущую страницу
        self.driver.back()
        print("Действие: Вернулись на предыдущую страницу")


class AllTopicRedirectItem(BaseMethods, BaseActions, CheckBoxesMethods):
    CanyonItem = (By.XPATH, '//*[@id="all__topics"]/div/div/div/ul/li[1]/ul/li[1]/a')
    AquaTopic = (By.XPATH, '//*[@id="all__topics"]/div/div/div/ul/li[1]/ul/li[5]/a')
    Lakes = (By.XPATH, '//*[@id="all__topics"]/div/div/div/ul/li[1]/ul/li[13]/a')

    Gallery = (By.XPATH, '//*[@id="all__topics"]/div/div/div/ul/li[2]/ul/li[1]/a')
    Theatre = (By.XPATH, '//*[@id="all__topics"]/div/div/div/ul/li[2]/ul/li[5]/a')

    GetAttributeItem = (By.XPATH, '/html/body/div[6]/h1')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def ScrollView(self):
        try:
            self.window_scroll_by(0, 2900)
            print("Действие: Элемент блоков достопримечательностей в зоне видимости")
        except Exception:
            print("Ошибка: Скролл страницы заблокирован")

    def TopicItemsLinksRedirect(self, item_locator, item_name, timeout=10):
        # Клик по элементу
        try:
            self.click_element(item_locator, timeout)
        except ElementNotInteractableException:
            raise Exception(f"Ошибка: Элемент {item_name} не кликабельный")
        print(f"Действие: Кликнули на элемент {item_name} для открытия новой вкладки")

        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.number_of_windows_to_be(2))
        except TimeoutException:
            raise Exception(f"Ошибка: Не удалось открыть новую вкладку в течение {timeout} секунд")

        # Переключение на новую вкладку
        window_handles = self.driver.window_handles
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


class AdditionalArticles(BaseMethods, BaseActions, CheckBoxesMethods):
    LinkItem1 = (By.XPATH, '/html/body/section[6]/div/div/div/div[1]/div[1]/div[1]/a')
    LinkItem2 = (By.XPATH, '/html/body/section[6]/div/div/div/div[1]/div[1]/div[2]/a')
    LinkItem3 = (By.XPATH, '/html/body/section[6]/div/div/div/div[1]/div[1]/div[3]/a')

    Routs = (By.XPATH, '/html/body/section[6]/div/div/div/div[2]/div/a[1]')
    Tours = (By.XPATH, '/html/body/section[6]/div/div/div/div[2]/div/a[3]')
    Attractions = (By.XPATH, '/html/body/section[6]/div/div/div/div[2]/div/a[2]')
    Hotel = (By.XPATH, '/html/body/section[6]/div/div/div/div[2]/div/a[4]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def ScrollView(self):
        try:
            self.window_scroll_by(0, 4150)
            print("Действие: Элемент блоков достопримечательностей в зоне видимости")
        except Exception:
            print("Ошибка: Скролл страницы заблокирован")

    def AdditionalArticlesRedirect(self, item_locator, item_name, timeout=10):
        # Клик по элементу
        try:
            self.click_element(item_locator, timeout)
        except ElementNotInteractableException:
            raise Exception(f"Ошибка: Элемент {item_name} не кликабельный")
        print(f"Действие: Кликнули на элемент {item_name} для открытия новой вкладки")

        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.number_of_windows_to_be(2))
        except TimeoutException:
            raise Exception(f"Ошибка: Не удалось открыть новую вкладку в течение {timeout} секунд")

        # Переключение на новую вкладку
        window_handles = self.driver.window_handles
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
        GetAttributeItem = (By.XPATH, '/html/body/main/div[3]/div/section[1]/h1')
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

    def OfferBlock(self, item_locator, item_name, timeout=10):
        # Клик по элементу
        try:
            self.click_element(item_locator, timeout)
        except ElementNotInteractableException:
            raise Exception(f"Ошибка: Элемент {item_name} не кликабельный")
        print(f"Действие: Кликнули на элемент {item_name} для открытия новой вкладки")

        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.number_of_windows_to_be(2))
        except TimeoutException:
            raise Exception(f"Ошибка: Не удалось открыть новую вкладку в течение {timeout} секунд")

        # Переключение на новую вкладку
        window_handles = self.driver.window_handles
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

        # Закрытие текущей вкладки и переключение на предыдущую
        self.driver.close()
        self.driver.switch_to.window(window_handles[0])
        print("Действие: Вернулись на предыдущую вкладку")


class InnerPageAttractions(BaseMethods, BaseActions, CheckBoxesMethods):
    CountryItems = (By.XPATH, '//*[@id="attraction-search-form"]/div[1]/input')
    GetItemsCountryList = (By.XPATH, '//*[@id="attraction-search-form"]/div[1]/div')
    CityItems = (By.XPATH, '//*[@id="attraction-search-form"]/div[2]/input')
    GetItemsCityList = (By.XPATH, '//*[@id="attraction-search-form"]/div[2]/div')

    CountryItem = (By.XPATH, '//*[@id="attraction-search-form"]/div[1]/div/ul/li[2]')
    CityItem = (By.XPATH, '//*[@id="attraction-search-form"]/div[2]/div/ul/li[2]')
    Submit = (By.XPATH, '//*[@id="attraction-search-form"]/div[3]/button')

    NatureItem = (By.XPATH, '/html/body/div[8]/div/div[2]/a[1]')
    ReligionItem = (By.XPATH, '/html/body/div[8]/div/div[2]/a[2]')
    FloraItem = (By.XPATH, '/html/body/div[8]/div/div[2]/a[3]')
    HistoricalItem = (By.XPATH, '/html/body/div[8]/div/div[2]/a[4]')
    ArchitectureItem = (By.XPATH, '/html/body/div[8]/div/div[2]/a[5]')
    EntertainmentItem = (By.XPATH, '/html/body/div[8]/div/div[2]/a[6]')

    GetAttributeItem = (By.XPATH, '/html/body/div[6]/h1')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logger = logging.getLogger(__name__)

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

    def OpenAndReturnItems(self, item_locator, item_name, timeout=10):
        # Клик по элементу
        try:
            self.click_element(item_locator, timeout)
        except ElementNotInteractableException:
            raise Exception(f"Ошибка: Элемент {item_name} не кликабельный")
        print(f"Действие: Кликнули на элемент {item_name} для открытия новой вкладки")

        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.number_of_windows_to_be(2))
        except TimeoutException:
            raise Exception(f"Ошибка: Не удалось открыть новую вкладку в течение {timeout} секунд")

        # Переключение на новую вкладку
        window_handles = self.driver.window_handles
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

    def Scroll_View(self):
        try:
            self.window_scroll_by(0, 450)
            print("Действие: Элемент блоков достопримечательностей в зоне видимости")
        except Exception:
            print("Ошибка: Скролл страницы заблокирован")

    def ScrollView(self):
        try:
            self.window_scroll_by(0, 1250)
            print("Действие: Элемент блоков достопримечательностей в зоне видимости")
        except Exception:
            print("Ошибка: Скролл страницы заблокирован")

    def AttractionsTopicsRedirect(self, item_locator, item_name, timeout=20):
        """Метод для перенаправления на темы достопримечательностей."""

        # Создание объекта WebDriverWait для повторного использования
        wait = WebDriverWait(self.driver, timeout)

        previous_window_handle = self.driver.current_window_handle

        # Клик по элементу
        # Клик по элементу
        try:
            wait.until(EC.element_to_be_clickable(item_locator))  # Явное ожидание перед кликом
            # Получение списка текущих дескрипторов окон перед кликом
            current_window_handles = self.driver.window_handles
            print(f"Дескрипторы окон перед кликом: {current_window_handles}")
            self.click_element(item_locator, timeout)
        except ElementNotInteractableException:
            raise Exception(f"Ошибка: Элемент {item_name} не кликабельный")

        print(f"Действие: Кликнули на элемент {item_name} для открытия новой вкладки")

        try:
            wait.until(lambda d: len(d.window_handles) > len(current_window_handles))
        except TimeoutException:
            raise Exception(f"Ошибка: Не удалось открыть новую вкладку в течение {timeout} секунд")

        # Переключение на новую вкладку
        new_window_handle = list(set(self.driver.window_handles) - set(current_window_handles))[0]
        self.driver.switch_to.window(new_window_handle)
        print("Проверка: Переключились на новую вкладку")

        # Получение URL текущей страницы
        current_url = self.driver.current_url

        # Отправка GET-запроса на URL текущей страницы и проверка кода ответа
        try:
            response = requests.get(current_url, timeout=10)
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ошибка запроса: {str(e)}")

        status_code = response.status_code
        print(f"Код статуса страницы {item_name}: {status_code}")
        if status_code != 200:
            raise Exception(f"Ошибка элемента {item_name}: Код статуса {status_code}")

        # Подтягивание аттрибута с другой страницы
        ATTRIBUTE_XPATH = '/html/body/div[6]/h1'
        try:
            GetAttributeItem = wait.until(EC.visibility_of_element_located((By.XPATH, ATTRIBUTE_XPATH)))
        except TimeoutException:
            # Добавление скриншота для анализа ошибки
            self.driver.save_screenshot('error_screenshot.png')
            raise Exception(f"Ошибка: Элемент на странице {item_name} не стал видимым в течение заданного времени")

        GetAttributeItem_text = GetAttributeItem.text
        print(f"Текст элемента data_count: {GetAttributeItem_text}")

        # Закрытие текущей вкладки и переключение на предыдущую
        new_window_handle = self.driver.current_window_handle  # Сохранение дескриптора текущего окна
        time.sleep(5)  # Добавьте небольшую задержку перед закрытием вкладки
        self.driver.close()  # Закрытие текущей вкладки
        self.driver.switch_to.window(previous_window_handle)  # Переключение на предыдущую вкладку
        print("Действие: Вернулись на предыдущую вкладку")


class AttractionsItemsRedirect(BaseMethods, BaseActions, CheckBoxesMethods):
    AttractionsItem1 = (By.XPATH, '/html/body/section[1]/div/div/div/div[1]/div[1]/a/img')
    AttractionsItem2 = (By.XPATH, '/html/body/section[1]/div/div/div/div[2]/div[1]/a[1]/img')
    AttractionsItem3 = (By.XPATH, '/html/body/section[1]/div/div/div/div[3]/div[1]/a/img')
    AttractionsItem4 = (By.XPATH, '/html/body/section[1]/div/div/div/div[4]/div[1]/a/img')
    AttractionsItem5 = (By.XPATH, '/html/body/section[1]/div/div/div/div[5]/div[1]/a[1]/img')
    AttractionsItem6 = (By.XPATH, '/html/body/section[1]/div/div/div/div[6]/div[1]/a[1]/img')
    AttractionsItem7 = (By.XPATH, '/html/body/section[1]/div/div/div/div[7]/div[1]/a[1]/img')
    AttractionsItem8 = (By.XPATH, '/html/body/section[1]/div/div/div/div[8]/div[1]/a/img')
    AttractionsItem9 = (By.XPATH, '/html/body/section[1]/div/div/div/div[10]/div[1]/a/img')
    AttractionsItem10 = (By.XPATH, '/html/body/section[1]/div/div/div/div[6]/div[1]/a[1]/img')
    AttractionsItem11 = (By.XPATH, '/html/body/section[1]/div/div/div/div[11]/div[1]/a/img')
    AttractionsItem12 = (By.XPATH, '/html/body/section[1]/div/div/div/div[12]/div[1]/a[1]/img')
    AttractionsItem13 = (By.XPATH, '/html/body/section[1]/div/div/div/div[13]/div[1]/a[1]/img')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def Scroll_View(self):
        try:
            self.window_scroll_by(0, 750)
            print("Действие: Элемент блоков достопримечательностей в зоне видимости")
        except Exception:
            print("Ошибка: Скролл страницы заблокирован")

    def Scroll_View6(self):
        try:
            self.window_scroll_by(0, 950)
            self.sleep(3)
            print("Действие: Элемент блоков достопримечательностей в зоне видимости")
        except Exception:
            print("Ошибка: Скролл страницы заблокирован")

    def Scroll_View9(self):
        try:
            self.window_scroll_by(0, 1250)
            print("Действие: Элемент блоков достопримечательностей в зоне видимости")
        except Exception:
            print("Ошибка: Скролл страницы заблокирован")

    def Scroll_View13(self):
        try:
            self.window_scroll_by(0, 1650)
            print("Действие: Элемент блоков достопримечательностей в зоне видимости")
        except Exception:
            print("Ошибка: Скролл страницы заблокирован")

    def OpenAndReturnItem(self, item_locator, item_name, timeout=10):
        # Клик по элементу
        try:
            self.click_element(item_locator, timeout)
        except (ElementNotInteractableException, ElementClickInterceptedException) as e:
            raise Exception(f"Ошибка: Элемент {item_name} не кликабельный ({str(e)})")
        print(f"Действие: Кликнули на элемент {item_name} для открытия новой вкладки")

        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.number_of_windows_to_be(2))
        except TimeoutException:
            raise Exception(f"Ошибка: Не удалось открыть новую вкладку в течение {timeout} секунд")

        # Переключение на новую вкладку
        window_handles = self.driver.window_handles
        new_window_handle = [handle for handle in window_handles if handle != self.driver.current_window_handle][0]
        self.driver.switch_to.window(new_window_handle)
        print("Проверка: Переключились на новую вкладку")

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
        GetAttributeItem = (By.XPATH, '/html/body/main/section[1]/div/div/div/div[1]/h1')
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


class Map(BaseMethods, BaseActions, CheckBoxesMethods):
    Map = (By.XPATH, '//*[@id="map"]')
    ActiveElement = (By.XPATH, '//*[@id="map"]/div[1]/div[4]/img[13]')
    ZoomIn = (By.XPATH, '//*[@id="map"]/div[2]/div[1]/div/a[1]')
    ZoomOut = (By.XPATH, '//*[@id="map"]/div[2]/div[1]/div/a[2]')
    Marker = (By.XPATH, '//*[@id="map"]/div[1]/div[4]/img[11]')
    MarkerContent = (By.XPATH, '//*[@id="map"]/div[1]/div[6]/div/div[1]')
    GetAttributeItem = (By.XPATH, '/html/body/main/section[1]/div/div/div/div[1]/h1')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def Scroll_View(self):
        try:
            self.window_scroll_by(0, 2850)
            self.logger.info("Действие: Элемент блоков достопримечательностей в зоне видимости")
        except Exception:
            self.logger.error("Ошибка: Скролл страницы заблокирован")

    def map_functionality(self):
        print("Начало теста функциональности карты")

        # 1. Проверка наличия карты на странице
        print("Шаг 1: Проверка наличия карты на странице")
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(self.Map)
            )
            print("Шаг 1: Успешно - Карта присутствует на странице")
        except TimeoutException:
            print("Шаг 1: Ошибка - Карта отсутствует на странице")
            self.driver.quit()
            return

        # Даем время карте для полной загрузки
        time.sleep(5)

        # 2. Проверка активности карты
        print("Шаг 2: Проверка активности карты")
        try:
            active_element = self.driver.find_element(*self.ActiveElement)
            assert active_element.is_enabled(), "Элемент на карте неактивен"
            print("Шаг 2: Успешно - Карта активна")
        except (NoSuchElementException, AssertionError):
            print("Шаг 2: Ошибка - Карта неактивна")
            self.driver.quit()
            return

        # 3. Проверка функций зума
        print("Шаг 3: Проверка функций зума")
        try:
            zoom_in_button = self.driver.find_element(*self.ZoomIn)
            zoom_out_button = self.driver.find_element(*self.ZoomOut)

            zoom_in_button.click()
            time.sleep(5)
            print("Шаг 3.1: Зуммирование вперёд успешно")

            zoom_out_button.click()
            time.sleep(5)
            print("Шаг 3.2: Зуммирование назад успешно")
        except (NoSuchElementException, Exception) as e:
            print(f"Шаг 3: Ошибка - Проблемы с функцией зума ({str(e)})")
            self.driver.quit()
            return

        # 4. Клик на маркер
        print("Шаг 4: Клик на маркер")
        try:
            marker = self.driver.find_element(*self.Marker)
            marker.click()
            time.sleep(3)
            print("Шаг 4: Успешно - Клик на маркер выполнен")
        except (NoSuchElementException, Exception) as e:
            print(f"Шаг 4: Ошибка - Не удалось кликнуть на маркер ({str(e)})")
            self.driver.quit()
            return

        # 5. Клик на контент маркера и переход на новую страницу
        print("Шаг 5: Клик на контент маркера и переход на новую страницу")
        try:
            marker_content = self.driver.find_element(*self.MarkerContent)
            marker_content.click()
            time.sleep(3)
            print("Шаг 5: Успешно - Переход на новую страницу выполнен")
        except (NoSuchElementException, Exception) as e:
            print(f"Шаг 5: Ошибка - Не удалось перейти на новую страницу ({str(e)})")
            self.driver.quit()
            return

        # 6. Получение и вывод атрибута GetAttributeItem
        print("Шаг 6: Получение и вывод атрибута GetAttributeItem")
        try:
            attribute_item = self.driver.find_element(*self.GetAttributeItem).text
            print(f"Атрибут GetAttributeItem: {attribute_item}")
            print(f"Шаг 6: Успешно - Атрибут GetAttributeItem получен: {attribute_item}")
        except (NoSuchElementException, Exception) as e:
            print(f"Шаг 6: Ошибка - Не удалось получить атрибут GetAttributeItem ({str(e)})")
            self.driver.quit()
            return

        print("Тест успешно выполнен")
        self.driver.quit()
