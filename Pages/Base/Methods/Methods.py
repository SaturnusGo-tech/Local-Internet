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
        logging.basicConfig(level=logging.ERROR)

class BaseMethods(BasePage):
    # методы для взаимодействия с элементами страницы
    def __init__(self, driver):
        super().__init__(driver)

    def click_element(self, by_locator, timeout=10, error_message="Failed to click on element"):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(by_locator)
            )
            element.click()

        except ElementNotInteractableException:
            self.logger.error(
                f"{error_message}: Element not interactable - Failed to click on element with locator: {by_locator}")
            raise
        except Exception as e:
            self.logger.error(
                f"{error_message}: Unknown exception - Failed to click on element with locator: {by_locator}")
            self.logger.exception(e)
            raise

    def send_keys_to_element(self, by_locator, keys):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator)
            )
            element.clear()
            element.send_keys(keys)
        except Exception as e:
            print("Can't find an element")
            print(e)

    def wait_until_element_clickable(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(by_locator))

    def wait_until_element_visible(self, by_locator, timeout=10, poll_frequency=0.5):
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        wait.until(EC.visibility_of_element_located(by_locator))

    def double_click_element(self, by_locator, double_click=True):
        element = self.driver.find_element(*by_locator)
        if double_click:
            action = ActionChains(self.driver)
            action.double_click(element).perform()
        else:
            element.click()

    def assert_element_to_be_clickable(self, by_locator, timeout=15, screenshot_path=None):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(by_locator)
            )
            assert element.is_displayed()
            assert element.location_once_scrolled_into_view == element.location
            self.logger.info(f"Тест пройден успешно: элемент {by_locator} виден на странице")
        except (NoSuchElementException, AssertionError) as e:
            self.logger.error(f"Ошибка: {str(e)}")
            if screenshot_path:
                self._save_screenshot_with_arrow(by_locator, screenshot_path)
                self.logger.info(f"Скриншот сохранен по пути: {screenshot_path}")

    def is_visible(self, by_locator, expected_text=None, expected_attribute=None, expected_attribute_value=None):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator)
            )
            assert element.is_displayed() and element.is_enabled()

            if expected_text is not None:
                assert element.text == expected_text, f"Expected text: '{expected_text}', Actual text: '{element.text}'"

            if expected_attribute is not None and expected_attribute_value is not None:
                actual_attribute_value = element.get_attribute(expected_attribute)
                assert actual_attribute_value == expected_attribute_value, f"Expected attribute value: '{expected_attribute_value}', Actual attribute value: '{actual_attribute_value}'"

            self.wait_for_page_to_load()
            return True
        except TimeoutException:
            self.logger.error("TimeoutException: Element is not visible")
            return False
        except AssertionError as e:
            self.logger.error(f"AssertionError: {str(e)}")
            return False

    def wait_for_page_to_load(self):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: self.driver.execute_script('return document.readyState') == 'complete'
            )
        except TimeoutException:
            self.logger.error("TimeoutException: Page did not load completely")

    def wait_for_element_visibility(self, by_locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(by_locator)
            )
            return True
        except TimeoutException:
            self.logger.error("TimeoutException: Element is not visible")
            return False
        except NoSuchElementException:
            self.logger.error("NoSuchElementException: Element not found")
            return False

    def scroll_page(self, scroll_by=300):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def assert_elements_exist(self, by_locator):
        elements = self.driver.find_elements(*by_locator)
        assert len(elements) > 0, f"No elements found with locator {by_locator}."


    def click_random_enabled_day_in_calendar(self, calendar_locator):
        # кликнуть на локатор виджета календаря
        self.driver.find_element(*calendar_locator).click()

        # Ожидание, пока календарь станет видимым
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".wg-datepicker__day"))
        )

        # найти все элементы дней календаря
        day_elements = self.driver.find_elements(By.CSS_SELECTOR, ".wg-datepicker__day:not([aria-disabled='true'])")

        # если нет кликабельных чисел, выбросить исключение
        if not day_elements:
            raise NoSuchElementException("No enabled days found in the calendar widget.")

        # выбрать случайное число из списка кликабельных чисел
        random_day = random.choice(day_elements)
        random_day.click()

    def select_random_option_from_dropdown(self, dropdown_element):
        """Selects a random option from a given dropdown menu element"""

        # Get all available options in the dropdown
        options = dropdown_element.find_elements_by_tag_name("option")

        # Select a random option from the dropdown (excluding the first one)
        random_option = random.choice(options[1:])

        # Click on the random option to select it
        random_option.click()

        # Click on the page body to close the dropdown menu
        body = self.driver.find_element_by_tag_name("body")
        body.send_keys(Keys.ESCAPE)

    def random_country_selection(self, dropdown_country):
        driver = self.driver
        action = ActionChains(driver)
        dropdown = driver.find_element(*dropdown_country)  # Ищем элемент по локатору

        while dropdown.is_displayed():
            action.send_keys(Keys.DOWN).perform()
            WebDriverWait(driver, 0.5).until(EC.element_to_be_clickable(dropdown_country))
            if random.randint(1, 10) == 3:
                action.send_keys(Keys.ENTER).perform()
                break

    def do_randint_click(self, by_locator, count=5, scroll=False):
        max_clicks = 6
        for i in range(count):
            try:
                elements = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(by_locator))
                element = random.choice(elements)
                if scroll:
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                element.click()
                WebDriverWait(self.driver, 5).until(EC.staleness_of(element))
                if i + 1 >= max_clicks:
                    raise Exception("Было сделано больше 6 кликов по элементу")
            except (StaleElementReferenceException, TimeoutException):
                pass

    def select_random_widget_item_by_xpath(self, widget, xpath):
        # Находим список элементов виджета
        items = widget.find_elements_by_xpath(xpath)

        # Выбираем случайный элемент из списка
        random_item = random.choice(items)

        # Создаем экземпляр ActionChains
        action = ActionChains(self.driver)

        # Кликаем на случайный элемент
        action.move_to_element(random_item).click().perform()

    def wait_for_element(self, locator, timeout=10):
        """ Явное ожидание элемента на странице """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise Exception(f"Элемент не найден на странице за {timeout} секунд")

    def check_container_block(self, container_locator, block_locator, timeout=10):
        try:
            # Ожидаем появления контейнера
            container = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(container_locator)
            )
            # Получаем список всех блоков в контейнере
            blocks = container.find_elements(*block_locator)
            # Проверяем, что список блоков не пустой
            assert len(blocks) > 0, "Блоки не найдены в контейнере"
        except TimeoutException:
            raise TimeoutException(f"Контейнер не был найден за {timeout} секунд")
        except NoSuchElementException:
            raise NoSuchElementException("Блок не найден")

    def check_container(self, container_locator, timeout=10):
        try:
            # Ожидаем появления контейнера
            container = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(container_locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Контейнер не был найден за {timeout} секунд")
        except NoSuchElementException:
            raise NoSuchElementException("Контейнер не найден")

    def scroll_page_tours(self, scroll_by=650):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_articles(self, scroll_by=1175):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_attractions(self, scroll_by=1750):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_hotels(self, scroll_by=2150):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_train(self, scroll_by=2550):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_news(self, scroll_by=3525):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_scopes(self, scroll_by=3525):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_other_delay(self, scroll_by=3975):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_comment(self, scroll_by=4475):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_articles_form(self, scroll_by=450):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_news_articles(self, scroll_by=900):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def check_container_blocks_with_arrows(self, container_locator, next_arrow_locator, prev_arrow_locator, timeout=10):
        try:
            # Ожидаем появления контейнера
            container = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(container_locator)
            )

            # Получаем количество блоков в контейнере
            num_blocks = len(container.find_elements(By.CSS_SELECTOR, '*'))

            # Кликаем на стрелки для прокрутки контейнера
            while True:
                try:
                    next_arrow = container.find_element(*next_arrow_locator)
                    next_arrow.click()
                except NoSuchElementException:
                    break

            while True:
                try:
                    prev_arrow = container.find_element(*prev_arrow_locator)
                    prev_arrow.click()
                except NoSuchElementException:
                    break

            # Проверяем, что список блоков не пустой
            try:
                container = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(container_locator)
                )
                blocks = container.find_elements(By.CSS_SELECTOR, '*')
                assert len(blocks) == num_blocks, "Неверное количество блоков в контейнере"
            except TimeoutException:
                raise TimeoutException(f"Контейнер не был найден за {timeout} секунд")
            except NoSuchElementException:
                raise NoSuchElementException("Блок не найден")

        except TimeoutException:
            raise TimeoutException(f"Контейнер не был найден за {timeout} секунд")
        except NoSuchElementException:
            raise NoSuchElementException("Элемент не найден")

    def click_through_container_blocks(self, container_selector, next_selector, prev_selector, timeout=10):
        """
        Метод осуществляет клик по стрелкам навигации контейнера для прокрутки блоков
        и проверяет наличие блоков в контейнере

        :param container_selector: селектор контейнера
        :param next_selector: селектор кнопки "следующий"
        :param prev_selector: селектор кнопки "предыдущий"
        :param timeout: время ожидания элемента в секундах
        """
        try:
            # Ожидаем появления контейнера
            container = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(container_selector)
            )
            # Получаем список всех блоков в контейнере
            blocks = container.find_elements_by_xpath("./*")
            # Проверяем, что список блоков не пустой
            assert len(blocks) > 0, "Блоки не найдены в контейнере"

            # Кликаем на кнопку "следующий" до тех пор, пока она не станет неактивной
            next_button = self.driver.find_element_by_css_selector(next_selector)
            while next_button.is_enabled():
                next_button.click()
                # Ожидаем, пока не загрузится следующий блок
                WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, f"{container_selector}/*[position()={len(blocks) + 1}]"))
                )
                blocks = container.find_elements_by_xpath("./*")

            # Кликаем на кнопку "предыдущий" до тех пор, пока она не станет неактивной
            prev_button = self.driver.find_element_by_css_selector(prev_selector)
            while prev_button.is_enabled():
                prev_button.click()
                # Ожидаем, пока не загрузится предыдущий блок
                WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, f"{container_selector}/*[position()={len(blocks)}]"))
                )
                blocks = container.find_elements_by_xpath("./*")

        except TimeoutException:
            raise TimeoutException(f"Контейнер не был найден за {timeout} секунд")
        except NoSuchElementException:
            raise NoSuchElementException("Блок не найден")

    def do_infinite_click(self, by_locator, scroll=False):
        """
        Метод осуществляет бесконечный клик по заданному локатору, пока элемент доступен для клика.
        :param by_locator: локатор элемента, на который необходимо кликнуть
        :param scroll: флаг прокрутки элемента в область видимости перед кликом (True/False)
        """
        while True:
            try:
                elements = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(by_locator))
                for element in elements:
                    try:
                        if scroll:
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                        element.click()
                        # Ожидаем прогрузки элементов после клика
                        WebDriverWait(self.driver, 5).until(EC.staleness_of(element))
                    except StaleElementReferenceException:
                        pass
            except TimeoutException:
                break

    def is_element_present(self, by_locator, timeout=20, screenshot_on_fail=True):
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located(by_locator))
            assert element.is_enabled(), f"Элемент {by_locator} найден, но не активен"
        except TimeoutException:
            error_message = f"Элемент {by_locator} не найден за {timeout} секунд"
            self.logger.error(error_message)
            error_info = self._get_error_info(by_locator)
            if screenshot_on_fail:
                self._save_screenshot(error_info['Скриншот'])
            error_info['Ошибка'] = error_message
            raise AssertionError(error_info)
        except (NoSuchElementException, ElementNotVisibleException) as e:
            error_message = f"Элемент {by_locator} не найден"
            self.logger.error(error_message)
            error_info = self._get_error_info(by_locator)
            if screenshot_on_fail:
                self._save_screenshot(error_info['Скриншот'])
            error_info['Ошибка'] = error_message
            raise AssertionError(error_info)
        except Exception as e:
            error_message = f"Произошла ошибка при поиске элемента {by_locator}: {str(e)}"
            self.logger.error(error_message)
            error_info = self._get_error_info(by_locator)
            if screenshot_on_fail:
                self._save_screenshot(error_info['Скриншот'])
            error_info['Ошибка'] = error_message
            raise AssertionError(error_info)

    def _get_error_info(self, by_locator):
        element = self.driver.find_element(*by_locator) if by_locator else None
        error_info = {
            'Локатор': str(by_locator),
            'URL': self.driver.current_url,
            'HTML-код': element.get_attribute('outerHTML') if element else None,
            'Текст': element.text if element else None,
            'Расположение': element.location if element else None,
            'Размер': element.size if element else None,
        }
        return error_info

    def _save_screenshot(self, screenshot_path):
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        screenshot_name = f"screenshot_{timestamp}.png"
        self.driver.save_screenshot(screenshot_name)
        self.logger.info(f"Скриншот сохранен по пути: {screenshot_name}")
        return screenshot_name

    def click_in_loop4(self, locator):
        for i in range(4):
            element = self.driver.find_element(*locator)
            element.click()

    def sleep(self, seconds=5, randomize=False, min_seconds=None, max_seconds=None):
        if randomize:
            if min_seconds is None:
                min_seconds = 1
            if max_seconds is None:
                max_seconds = seconds * 2
            sleep_time = random.uniform(min_seconds, max_seconds)
        else:
            sleep_time = seconds
        time.sleep(sleep_time)

    def is_dropdown_present(self, by_locator):
        try:
            wait = WebDriverWait(self.driver, 10)
            dropdown = wait.until(EC.visibility_of_element_located(by_locator))
            assert dropdown.is_displayed(), f"Выпадающий список {by_locator} найден, но не отображается"
            return True
        except (NoSuchElementException, TimeoutException):
            assert False, f"Выпадающий список {by_locator} не найден"

    def window_scroll_by(self, x, y):
        """
        Scrolls the window by the given x and y values.
        """
        try:
            # Wait for the page to load completely
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))

            # Scroll the window to the desired position
            self.driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", x, y)
        except Exception as e:
            print("Error while scrolling window:", e)

    def assert_same_locator_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        if len(elements) == 0:
            raise AssertionError(f"No elements found with locator: {locator}")
        if len(elements) > 8:
            raise AssertionError(f"More than 8 elements found with locator: {locator}")
        for element in elements:
            if not element.is_displayed():
                raise AssertionError(f"Element not displayed with locator: {locator}")
            if not element.is_enabled():
                raise AssertionError(f"Element not enabled with locator: {locator}")
            if not element.is_selected():
                raise AssertionError(f"Element not selected with locator: {locator}")

    def check_heading_text(self, expected_text, tags=("h1", "h2", "h3", "h4", "h5", "h6")):
        # Ожидание, пока хотя бы один заголовок станет видимым
        def any_heading_visible(driver):
            visible_headings = []
            for tag in tags:
                visible_headings.extend(
                    [element for element in driver.find_elements(By.TAG_NAME, tag) if element.is_displayed()])
                if visible_headings:
                    return True
            return False

        WebDriverWait(self.driver, 10).until(any_heading_visible)

        # Найти все элементы заголовков с указанными тегами
        heading_elements = []
        for tag in tags:
            heading_elements.extend(self.driver.find_elements(By.TAG_NAME, tag))

        # Если не найдено ни одного элемента заголовка, выбросить исключение
        if not heading_elements:
            raise NoSuchElementException(f"No heading elements with the specified tags found: {tags}")

        # Проверить текст каждого найденного элемента заголовка
        for heading in heading_elements:
            if heading.text == expected_text:
                return True

        # Если ни один из элементов заголовка не содержит ожидаемый текст, выбросить исключение
        raise AssertionError(
            f"Expected text '{expected_text}' not found in any of the heading elements with tags {tags}")

    def move_slider(self, slider, offset_x, offset_y):
        action = ActionChains(self.driver)
        action.click_and_hold(slider).move_by_offset(offset_x, offset_y).release().perform()

    def page_loaded(self, locator, timeout=10):
        """
        Явное ожидание элемента на странице.
        :param locator: кортеж с двумя значениями (By.<метод>, '<селектор>')
        :param timeout: время ожидания в секундах (по умолчанию 10)
        :return: найденный элемент
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except Exception as e:
            print(f"Error while waiting for element {locator}: {e}")
            return None

    def check_buttons_and_links(self):
        try:
            buttons = self.driver.find_elements_by_tag_name("button")
            links = self.driver.find_elements_by_tag_name("a")
            elements = buttons + links

            for element in elements:
                href = element.get_attribute("href") or element.get_attribute("data-href")

                if href:
                    response = requests.head(href, allow_redirects=True)

                    if 400 <= response.status_code <= 599:
                        print(
                            f"Element '{element.text.strip()}' leads to an error page: {response.status_code} - {href}")

        except NoSuchElementException:
            print("No buttons or links found on the page")



