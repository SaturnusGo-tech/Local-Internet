import pytest
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException, \
    ElementNotInteractableException
from Local_Internet.Pages.Base.Utils.Hotels.HotelData import TestData
from Local_Internet.Pages.Base.Methods.CheckBoxesMrthods import CheckBoxesMethods
from Local_Internet.Pages.Base.URLS.Main.URL import MainURL
from Local_Internet.Pages.Base.Methods.Methods import BaseMethods
from Local_Internet.Pages.Base.Methods.Base import BaseActions
from Local_Internet.Tests.MainTests.TestData.TestData import CheckBoxes
from Local_Internet.Tests.MainTests.TestData.Validation_data.Validation_data_items import Valid_Data
from Local_Internet.Tests.MainTests.TestData.Cities.CityData import CityDetails


class MainLocators(BaseMethods, CheckBoxesMethods, BaseActions):
    Country_input = (By.ID, 's-query')
    Trip_checkBoxes = (By.XPATH, '/html/body/section[2]/div/div[1]/form[2]/div[2]/input[1]')
    Unblock_Screen = (By.ID, 'travel-in-toursRussia')
    Submit = (By.CSS_SELECTOR, '[class="btn-orange hotels-search__mob100p"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def LoadPage(self, s=10):
        self.page_loaded(MainURL.Current_url)
        self.sleep(s)

    def city_Input(self, s=10):
        self.send_keys_to_element(MainLocators.Country_input, TestData.POSITIVE)
        self.sleep(s)

    def open_trip_menu(self, s=10):
        self.click_element(MainLocators.Trip_checkBoxes)
        self.sleep(s)

    def scroll_into_View(self, s=10):
        self.window_scroll_by(0, 250)
        self.sleep(s)

    def random_CheckBox_Selection(self, s=10):
        try:
            random_locator = CheckBoxes.get_random_locator()
            element = WebDriverWait(self.driver, s).until(
                EC.visibility_of_element_located(random_locator)
            )
            element.click()
            self.sleep(s)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except TimeoutException as e:
            print(f"Timeout: {e}")

    def click_to_unblock(self, s=10):
        self.double_click_element(MainLocators.Country_input)
        self.sleep(s)

    def openPage(self, s=10):
        try:
            self.click_element(MainLocators.Submit)
            WebDriverWait(self.driver, s).until(EC.number_of_windows_to_be(2))
            self.switch_to_new_tab()

            new_page_url = self.driver.current_url

            response_code = self.get_response_code(new_page_url)
            print(f"Network response code: {response_code}")
            assert response_code == 200, f"Network response code was {response_code}, expected 200"
            self.sleep(s)
            return response_code
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except TimeoutException as e:
            print(f"Timeout: {e}")
        except WebDriverException as e:
            print(f"WebDriver exception: {e}")

    def validation_check_up_pos(self):
        input_value = Valid_Data.TourInputSecretTokenHex4
        self.send_keys_to_element(MainLocators.Country_input, input_value)
        actual_input_value = self.driver.find_element(*MainLocators.Country_input).get_attribute("value")
        assert len(actual_input_value) == len(
            input_value), f"Input field contains {len(actual_input_value)} characters, expected {len(input_value)} characters"
        assert len(input_value) == 8, f"Ожидаемое занчение было: 8, но получили {len(input_value)}"
        print("Тест пройден успешно, поле обрабатывает 8 символов")

    def validation_check_up_pos25(self):
        input_value = Valid_Data.TourInputSecretTokenHex12
        self.send_keys_to_element(MainLocators.Country_input, input_value)
        actual_input_value = self.driver.find_element(*MainLocators.Country_input).get_attribute("value")
        assert len(actual_input_value) == len(
            input_value), f"Input field contains {len(actual_input_value)} characters, expected {len(input_value)} characters"
        assert len(input_value) == 24, f"Ожидаемое занчение было: 24, но получили {len(input_value)}"
        print("Тест пройден успешно, поле обрабатывает 24 символов")

    def validation_check_up_neg16(self):
        input_value = Valid_Data.TourInputSecretTokenHex16
        self.send_keys_to_element(MainLocators.Country_input, input_value)
        actual_input_value = self.driver.find_element(*MainLocators.Country_input).get_attribute("value")
        assert len(actual_input_value) == len(
            input_value), f"Input field contains {len(actual_input_value)} characters, expected {len(input_value)} characters"
        assert len(input_value) == 32, f"Ожидаемое занчение было: 25, но получили{len(input_value)}"
        print("Тест пройден успешно, поле не обрабатывает 32 символов")

    def validation_check_up_neg32(self):
        input_value = Valid_Data.TourInputSecretTokenHex32
        self.send_keys_to_element(MainLocators.Country_input, input_value)
        actual_input_value = self.driver.find_element(*MainLocators.Country_input).get_attribute("value")
        assert len(actual_input_value) == len(
            input_value), f"Input field contains {len(actual_input_value)} characters, expected {len(input_value)} characters"
        assert len(input_value) == 64, f"Ожидаемое занчение было: 25, но получили {len(input_value)}"
        print("Тест пройден успешно, поле не обрабатывает 64 символов")


class MainWorldTour(CheckBoxes, BaseActions, BaseMethods):
    WorldTourSwitcher = (By.XPATH, '/html/body/section[2]/div/div[1]/div/div/div[1]/button[1]')
    DirectionFrom = (By.ID, 'toursearchapi-destinations')
    ApplyCityFrom = (By.XPATH, '//*[@id="tours-search-form"]/div[1]/div[2]/ul/li[1]')
    DirectionTo = (By.ID, 'toursearchapi-departurecityname')
    ApplyCityTo = (By.XPATH, '//*[@id="search-results-tours-d"]/ul/li')
    Quantity = (By.XPATH, '//*[@id="tours-search-form"]/div[4]/div/div[1]')
    AddNights = (By.XPATH, '//*[@id="tours-search-form"]/div[4]/div/div[2]/div/div/div[1]/div/span[3]')
    ShowMenu = (By.XPATH, '//*[@id="tours-search-form"]/div[5]/div[1]')
    OpenMenu = (By.XPATH, '//*[@id="tours-search-form"]/div[5]/div[2]/div[2]/div[1]')
    AddChild = (By.XPATH, '//*[@id="tours-search-form"]/div[5]/div[2]/div[2]/div[2]/div/span[2]')
    Submit = (By.CSS_SELECTOR, '.search__btn.search__mob100p')

    Validation_popup = (By.ID, 'toursearchapi-destinations')
    Error_msg = (By.XPATH, '//*[@id="page-search-tours"]/div[2]/h3')
    Items = [
        (By.XPATH, '//*[@id="tours-search-form"]/div[5]/div[2]/div[2]/div[2]/div/span[3]'),
        (By.XPATH, '//*[@id="tours-search-form"]/div[5]/div[2]/div[2]/div[2]/div/span[7]'),
        (By.XPATH, '//*[@id="tours-search-form"]/div[5]/div[2]/div[2]/div[2]/div/span[3]'),
        (By.XPATH, '//*[@id="tours-search-form"]/div[5]/div[2]/div[2]/div[2]/div/span[4]')
    ]
    Add_item = (By.XPATH, '//*[@id="tours-search-form"]/div[5]/div[2]/div[1]/div/span[2]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def LoadPage(self, s=10):
        self.page_loaded(MainURL.Current_url)
        self.sleep(s)

    def SwitchToWorldTourToggle(self, timeout=10):
        self.click_element(MainWorldTour.WorldTourSwitcher, timeout)

    def FieldInput(self):
        self.send_keys_to_element(MainWorldTour.DirectionFrom, TestData.POSITIVE_INT)

    def CheckValidation(self, timeout=10):
        required_attribute = self.is_visible(MainWorldTour.Validation_popup, timeout).get_attribute('required')
        assert required_attribute == 'true', "Поле не имеет атрибута 'required'"

    def CityAcceptFrom(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(MainWorldTour.ApplyCityFrom)
        )
        element.click()

    def ClearFieldInput(self, timeout=10):
        self.click_element(MainWorldTour.DirectionTo, timeout)
        self.send_keys_to_element(MainWorldTour.DirectionTo, TestData.POSITIVE_INT)

    def CityAcceptTo(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(MainWorldTour.ApplyCityTo)
        )
        element.click()

    def QuantityMenu(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(MainWorldTour.Quantity)
        )
        element.click()

    def addQuantity(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(MainWorldTour.AddNights)
        )
        for _ in range(4):
            element.click()

    def ShowMenuList(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(MainWorldTour.ShowMenu)
        )
        element.click()

    def OpenMenuList(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(MainWorldTour.OpenMenu)
        )
        element.click()

    def addChildToLocal(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(MainWorldTour.AddChild)
        )
        element.click()

    def OpenPageTour(self, timeout=10):
        self.double_click_element(MainWorldTour.Submit, timeout)
        try:
            WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
            self.switch_to_new_tab()

            while True:
                new_page_url = self.driver.current_url
                response_code = self.get_response_code(new_page_url)

                try:
                    error_element = WebDriverWait(self.driver, timeout).until(
                        EC.visibility_of_element_located(MainWorldTour.Error_msg)
                    )
                    if "Упс" in error_element.text:
                        print("Текст 'Упс' найден:", error_element.text)
                        return "Успешно"
                except TimeoutException:
                    pass  # Просто игнорируем TimeoutException и продолжаем цикл

                self.sleep(1)  # Подождать немного перед следующей попыткой
        except (NoSuchElementException, TimeoutException, WebDriverException) as e:
            print(f"Exception: {e}")

    def Error_msg_attribute(self, timeout=10):
        self.is_visible(MainWorldTour.Error_msg, timeout)

    def ScrollView(self):
        self.window_scroll_by(0, 250)

    def Click_All_Locators(self, timeout=10):
        self.page_loaded(MainURL.Current_url)  # Ожидание загрузки страницы
        for locator in self.Items:
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator)
                )
                element.click()
            except Exception as e:
                print(f"Error clicking element with locator {locator}: {str(e)}")

        for locator in self.Items:
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator)
                )
                element.click()
            except Exception as e:
                print(f"Error clicking element with locator {locator}: {str(e)}")

    def ClickLoop(self, timeout=10):
        self.click_in_loop4(MainWorldTour.Add_item)

    def validation_check_up_pos4(self, s=3):
        input_value = Valid_Data.TourInputSecretTokenHex4
        self.send_keys_to_element(MainWorldTour.DirectionFrom, input_value)
        self.sleep(s)
        self.send_keys_to_element(MainWorldTour.DirectionTo, input_value)
        actual_input_value = self.driver.find_element(*MainWorldTour.DirectionFrom).get_attribute("value")
        actual_input_value2 = self.driver.find_element(*MainWorldTour.DirectionTo).get_attribute("value")

        assert len(actual_input_value) == len(
            input_value), f"Input field contains {len(actual_input_value)} characters, expected {len(input_value)} characters"
        assert len(actual_input_value) == 8, f"Expected input field length: 25, but got {len(actual_input_value)}"
        assert len(actual_input_value2) == len(
            input_value), f"Input field contains {len(actual_input_value2)} characters, expected {len(input_value)} characters"
        assert len(actual_input_value2) == 8, f"Expected input field length: 25, but got {len(actual_input_value2)}"

        print("Тест пройден успешно, оба поля обрабатывают 25 символов")

    def validation_check_up_pos12(self, s=3):
        input_value = Valid_Data.TourInputSecretTokenHex12
        self.send_keys_to_element(MainWorldTour.DirectionFrom, input_value)
        self.sleep(s)
        self.send_keys_to_element(MainWorldTour.DirectionTo, input_value)
        actual_input_value = self.driver.find_element(*MainWorldTour.DirectionFrom).get_attribute("value")
        actual_input_value2 = self.driver.find_element(*MainWorldTour.DirectionTo).get_attribute("value")

        assert len(actual_input_value) == len(
            input_value), f"Input field contains {len(actual_input_value)} characters, expected {len(input_value)} characters"
        assert len(actual_input_value) == 8, f"Expected input field length: 25, but got {len(actual_input_value)}"
        assert len(actual_input_value2) == len(
            input_value), f"Input field contains {len(actual_input_value2)} characters, expected {len(input_value)} characters"
        assert len(actual_input_value2) == 8, f"Expected input field length: 25, but got {len(actual_input_value2)}"

    def validation_check_up_neg16(self, s=3):
        input_value = Valid_Data.TourInputSecretTokenHex16
        self.send_keys_to_element(MainWorldTour.DirectionFrom, input_value)
        self.sleep(s)
        self.send_keys_to_element(MainWorldTour.DirectionTo, input_value)
        actual_input_value = self.driver.find_element(*MainWorldTour.DirectionFrom).get_attribute("value")

        assert len(actual_input_value) == len(
            input_value), f"Input field contains {len(actual_input_value)} characters, expected {len(input_value)} characters"
        assert len(actual_input_value) != 32, f"Expected input field length to not be 24, but it is"

        print("Тест пройден успешно, поле не обрабатывает 24 символа")

    def validation_check_up_neg32(self, s=3):
        input_value = Valid_Data.TourInputSecretTokenHex16
        self.send_keys_to_element(MainWorldTour.DirectionFrom, input_value)
        self.sleep(s)
        self.send_keys_to_element(MainWorldTour.DirectionTo, input_value)
        actual_input_value = self.driver.find_element(*MainWorldTour.DirectionFrom).get_attribute("value")

        assert len(actual_input_value) == len(
            input_value), f"Input field contains {len(actual_input_value)} characters, expected {len(input_value)} characters"
        assert len(actual_input_value) != 25, f"Expected input field length to not be 64, but it is"

        print("Тест пройден успешно, поле не обрабатывает 24 символа")


class Hotel(BaseMethods, BaseActions, CheckBoxesMethods):
    Switch_to_hotel = (By.XPATH, '/html/body/div[2]/div/div[2]')
    Input = (By.XPATH, '//*[@id="search-hotels"]/input')
    SelectItem = (By.XPATH, '//*[@id="search-results"]/ul/li[1]')
    OpenMenu = (By.XPATH, '//*[@id="reservation-form"]/div[4]/div[1]')
    AddItem = (By.XPATH, '//*[@id="reservation-form"]/div[4]/div[2]/div[1]/div/span[2]')
    OpenChildMenu = (By.XPATH, '//*[@id="reservation-form"]/div[4]/div[2]/div[2]')
    GetItem = (By.XPATH, '//*[@id="reservation-form"]/div[4]/div[2]/div[2]/div[2]/div/span[2]')
    Submit = (By.XPATH, '//*[@id="reservation-form"]/input[4]')
    Error_Validation = (By.XPATH, '/html/body/pre')

    ExistingDropdown = (By.ID, 'search-results')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def HotelToggleButton(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(Hotel.Switch_to_hotel)
        )
        element.click()

    def SendKeys(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(Hotel.Input)
        )
        element.send_keys(TestData.POSITIVE_INT)

    def DropdownMenuExist(self, timeout=5):
        self.is_element_present(Hotel.ExistingDropdown, timeout)
        assert self.is_visible(Hotel.ExistingDropdown), "Выпадающий список городов/отелей не был найден"
        print("Выпадающий список городов/отелей был найден")

    def Select(self, timeout=10):
        self.click_element(Hotel.SelectItem, timeout)

    def OpenItem(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(Hotel.OpenMenu)
        )
        element.click()

    def AddLoopItem(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(Hotel.AddItem)
        )
        for _ in range(4):
            element.click()

    def OpenChildMenuDown(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(Hotel.OpenChildMenu)
        )
        element.click()

    def GetItems(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(Hotel.GetItem)
        )
        element.click()

    def OpenPage(self, timeout=10):
        print("Начинаем клик на кнопку Submit...")
        self.click_element(Hotel.Submit, timeout)

        try:
            print("Ожидание появления новой вкладки...")
            WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))

            print("Переключение на новую вкладку...")
            self.switch_to_new_tab()

            while True:
                new_page_url = self.driver.current_url
                print(f"Текущий URL: {new_page_url}")

                response_code = self.get_response_code(new_page_url)
                print(f"Код ответа: {response_code}")

                try:
                    print("Проверка наличия элемента с ошибкой...")
                    error_validation_element = WebDriverWait(self.driver, timeout).until(
                        EC.presence_of_element_located(Hotel.Error_Validation)
                    )
                    print("Ошибка редиректа - Нет видимости контента страницы Отели")
                    break
                except TimeoutException:
                    print("Элемент с ошибкой не найден, продолжаем...")
                    pass

                self.sleep(1)
        except (TimeoutException, WebDriverException) as e:
            print(f"Exception: {e}")

    def validation_check_up_pos(self):
        input_value = Valid_Data.TourInputSecretTokenHex4
        self.send_keys_to_element(Hotel.Input, input_value)
        actual_input_value = self.driver.find_element(*Hotel.Input).get_attribute("value")
        assert len(actual_input_value) == len(
            input_value), f"Input field contains {len(actual_input_value)} characters, expected {len(input_value)} characters"
        assert len(input_value) == 8, f"Ожидаемое занчение было: 8, но получили {len(input_value)}"
        print("Тест пройден успешно, поле обрабатывает 8 символов")

    def validation_check_up_pos25(self):
        input_value = Valid_Data.TourInputSecretTokenHex12
        self.send_keys_to_element(Hotel.Input, input_value)
        actual_input_value = self.driver.find_element(*Hotel.Input).get_attribute("value")
        assert len(actual_input_value) == len(
            input_value), f"Input field contains {len(actual_input_value)} characters, expected {len(input_value)} characters"
        assert len(input_value) == 24, f"Ожидаемое занчение было: 24, но получили {len(input_value)}"
        print("Тест пройден успешно, поле обрабатывает 24 символов")

    def validation_check_up_neg16(self):
        input_value = Valid_Data.TourInputSecretTokenHex16
        self.send_keys_to_element(Hotel.Input, input_value)
        actual_input_value = self.driver.find_element(*Hotel.Input).get_attribute("value")
        assert len(actual_input_value) == len(
            input_value), f"Input field contains {len(actual_input_value)} characters, expected {len(input_value)} characters"
        assert len(input_value) == 32, f"Ожидаемое занчение было: 25, но получили{len(input_value)}"
        print("Тест пройден успешно, поле не обрабатывает 32 символов")

    def validation_check_up_neg32(self):
        input_value = Valid_Data.TourInputSecretTokenHex32
        self.send_keys_to_element(Hotel.Input, input_value)
        actual_input_value = self.driver.find_element(*Hotel.Input).get_attribute("value")
        assert len(actual_input_value) == len(
            input_value), f"Input field contains {len(actual_input_value)} characters, expected {len(input_value)} characters"
        assert len(input_value) == 64, f"Ожидаемое занчение было: 25, но получили {len(input_value)}"
        print("Тест пройден успешно, поле не обрабатывает 64 символов")


class Train(BaseMethods, BaseActions, CheckBoxesMethods):
    TrainSwitcher = (By.XPATH, '/html/body/div[2]/div/div[3]')
    InputIn = (By.XPATH, '//*[@id="search-form_tickets"]/div[1]/input')
    DropDownMenuExist = (By.XPATH, '//*[@id="search-form_tickets"]/div[1]/div/ul')
    SelectItemIn = (By.XPATH, '//*[@id="search-form_tickets"]/div[1]/div/ul/li[1]')
    InputOut = (By.XPATH, '//*[@id="search-form_tickets"]/div[2]/input')
    DropDownMenu_Exist = (By.XPATH, '//*[@id="search-form_tickets"]/div[2]/div/ul')
    SelectItemOut = (By.XPATH, '//*[@id="search-form_tickets"]/div[2]/div/ul/li[2]')
    Submit = (By.XPATH, '//*[@id="search-form_tickets"]/button')

    DirectionBlockSuccess = (By.XPATH, '//*[@id="ufs-railway-app"]/div/div/div[2]')
    Error_Notification = (By.XPATH, '//*[@id="ufs-railway-app"]/div/div/div[2]/div[2]/div[2]/div/div[3]/div')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def Page_Loaded(self, timeout=10):
        self.page_loaded(MainURL.Current_url, timeout)

    def TrainSwitch(self, timeout=10):
        self.click_element(Train.TrainSwitcher, timeout)

    def GetInputIn(self):
        self.send_keys_to_element(Train.InputIn, CityDetails.Moscow)

    def DropdownMenuExistIn(self, timeout=5):
        self.is_element_present(Train.DropDownMenuExist, timeout)
        assert self.is_visible(Train.DropDownMenuExist), "Выпадающий список городов не был найден"
        print("Выпадающий список городов был найден")

    def SelectCityItemIn(self, timeout=10):
        self.click_element(Train.SelectItemIn, timeout)

    def GitInputOut(self):
        self.send_keys_to_element(Train.InputOut, CityDetails.Voronezh)

    def DropdownMenuExistOut(self, timeout=5):
        self.is_element_present(Train.DropDownMenu_Exist, timeout)
        assert self.is_visible(Train.DropDownMenu_Exist), "Выпадающий список городов не был найден"
        print("Выпадающий список городов был найден")

    def SelectCityItemOut(self, timeout=10):
        self.click_element(Train.SelectItemOut, timeout)

    def OpenPage(self, timeout=10):
        try:
            print("Начинаем клик на кнопку Submit...")
            self.click_element(Train.Submit, timeout)

            print("Ожидание появления новой вкладки...")
            WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))

            # Получение списка всех открытых вкладок
            windows = self.driver.window_handles

            # Переключение на вторую вкладку
            self.driver.switch_to.window(windows[1])
            print("Переключение на новую вкладку выполнено")

            # Ожидание полной загрузки страницы
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            print("Страница полностью загружена")

            # Дополнительное ожидание, чтобы убедиться, что страница MainURL.Train_url загрузилась на 100%
            WebDriverWait(self.driver, timeout).until(
                EC.url_to_be(MainURL.Train_url)
            )
            print("Страница MainURL.Train_url загрузилась на 100%")

            # Ожидание загрузки ключевого элемента на странице
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located(Train.DirectionBlockSuccess)
                )
                print("Ключевой элемент на второй странице загружен и виден")
                print("Успех: страница MainURL.Train_url загружена на 100% и найден элемент DirectionBlockSuccess")

                # Дополнительная проверка наличия контента на странице
                if self.is_visible(Train.DirectionBlockSuccess):
                    print("На странице обнаружен контент - редирект true")
                else:
                    print("На странице нет контента")

            except TimeoutException as ex:
                print("Произошла ошибка в блоке ожидания видимости элемента:")
                print(ex)
                raise AssertionError("Ключевой элемент на второй странице не загрузился или не виден")

            while True:
                new_page_url = self.driver.current_url
                print(f"Текущий URL: {new_page_url}")

                response_code = self.get_response_code(new_page_url)
                print(f"Код ответа: {response_code}")

                try:
                    print("Проверка наличия элемента с ошибкой...")
                    error_validation_element = WebDriverWait(self.driver, timeout).until(
                        EC.visibility_of_element_located(Train.DirectionBlockSuccess)
                    )
                    print("Ошибка редиректа - Нет видимости контента страницы ЖД")
                    break
                except TimeoutException:
                    print("Элемент с ошибкой не найден, продолжаем...")
                    pass

                self.sleep(1)

            # Проверка наличия элемента Error_Notification
            try:
                error_notification_element = self.driver.find_element(*Train.Error_Notification)
                if error_notification_element.is_displayed():
                    raise AssertionError("Страница не дала результат HTML")
            except NoSuchElementException:
                pass

        except (TimeoutException, WebDriverException) as e:
            print(f"Exception: {e}")

    def Train_validation_check_up_pos4(self, s=3):
        input_value = Valid_Data.TourInputSecretTokenHex4
        self.send_keys_to_element(Train.InputIn, input_value)
        self.sleep(s)
        self.send_keys_to_element(Train.InputOut, input_value)
        actual_input_value = self.driver.find_element(*Train.InputIn).get_attribute("value")
        actual_input_value2 = self.driver.find_element(*Train.InputOut).get_attribute("value")

        assert len(actual_input_value) == len(
            input_value), f"Input field contains {len(actual_input_value)} characters, expected {len(input_value)} characters"
        assert len(actual_input_value) == 8, f"Expected input field length: 25, but got {len(actual_input_value)}"
        assert len(actual_input_value2) == len(
            input_value), f"Input field contains {len(actual_input_value2)} characters, expected {len(input_value)} characters"
        assert len(actual_input_value2) == 8, f"Expected input field length: 25, but got {len(actual_input_value2)}"

        # Проверяем, что введено 8 символов, и завершаем тест с успехом
        if len(actual_input_value) == 8 and len(actual_input_value2) == 8:
            print("Успех: введено 8 символов в оба поля ввода")
            return True

    def Train_validation_check_up_pos12(self, s=3):
        input_value = Valid_Data.TourInputSecretTokenHex12
        self.send_keys_to_element(Train.InputIn, input_value)
        self.sleep(s)
        self.send_keys_to_element(Train.InputOut, input_value)
        actual_input_value = self.driver.find_element(*Train.InputIn).get_attribute("value")
        actual_input_value2 = self.driver.find_element(*Train.InputOut).get_attribute("value")

        assert len(actual_input_value) == len(
            input_value), f"Поле ввода содержит {len(actual_input_value)} символов, ожидается {len(input_value)} символов"
        assert len(
            actual_input_value) == 24, f"Ожидаемая длина поля ввода: 24, текущая длина: {len(actual_input_value)}"
        assert len(actual_input_value2) == len(
            input_value), f"Поле ввода содержит {len(actual_input_value2)} символов, ожидается {len(input_value)} символов"
        assert len(
            actual_input_value2) == 24, f"Ожидаемая длина поля ввода: 24, текущая длина: {len(actual_input_value2)}"

        # Проверяем, что введено 8 символов, и завершаем тест с успехом
        if len(actual_input_value) == 24 and len(actual_input_value2) == 24:
            print("Успех: введено 24 символов в оба поля ввода")
            return True

    def Train_validation_check_up_neg16(self, s=3):
        input_value = Valid_Data.TourInputSecretTokenHex16
        self.send_keys_to_element(Train.InputIn, input_value)
        self.sleep(s)
        self.send_keys_to_element(Train.InputOut, input_value)
        actual_input_value = self.driver.find_element(*Train.InputIn).get_attribute("value")
        actual_input_value2 = self.driver.find_element(*Train.InputOut).get_attribute("value")

        assert len(actual_input_value) == len(
            input_value), f"Поле ввода содержит {len(actual_input_value)} символов, ожидается {len(input_value)} символов"
        assert len(
            actual_input_value) <= 25, f"Ожидается, что длина поля ввода не будет больше 25 символов, текущая длина: {len(actual_input_value)}"
        assert len(actual_input_value2) == len(
            input_value), f"Поле ввода содержит {len(actual_input_value2)} символов, ожидается {len(input_value)} символов"
        assert len(
            actual_input_value2) <= 25, f"Ожидается, что длина поля ввода не будет больше 25 символов, текущая длина: {len(actual_input_value2)}"

        print("Тест пройден успешно, поле не обрабатывает больше 25 символов")

    def Train_validation_check_up_neg32(self, s=3):
        input_value = Valid_Data.TourInputSecretTokenHex32
        self.send_keys_to_element(Train.InputIn, input_value)
        self.sleep(s)
        self.send_keys_to_element(Train.InputOut, input_value)
        actual_input_value = self.driver.find_element(*Train.InputIn).get_attribute("value")
        actual_input_value2 = self.driver.find_element(*Train.InputOut).get_attribute("value")

        assert len(actual_input_value) == len(
            input_value), f"Поле ввода содержит {len(actual_input_value)} символов, ожидается {len(input_value)} символов"
        assert len(
            actual_input_value) <= 25, f"Ожидается, что длина поля ввода не будет больше 25 символов, текущая длина: {len(actual_input_value)}"
        assert len(actual_input_value2) == len(
            input_value), f"Поле ввода содержит {len(actual_input_value2)} символов, ожидается {len(input_value)} символов"
        assert len(
            actual_input_value2) <= 25, f"Ожидается, что длина поля ввода не будет больше 25 символов, текущая длина: {len(actual_input_value2)}"

        print("Тест пройден успешно, поле не обрабатывает больше 25 символов")

    def OpenTrainPage(self, timeout=10):
        print("Начинаем клик на кнопку Submit...")
        self.click_element(Train.Submit, timeout)

        try:
            print("Ожидание появления новой вкладки...")
            WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))

            print("Переключение на новую вкладку...")
            self.switch_to_new_tab()

            while True:
                new_page_url = self.driver.current_url
                print(f"Текущий URL: {new_page_url}")

                response_code = self.get_response_code(new_page_url)
                print(f"Код ответа: {response_code}")

                try:
                    print("Проверка наличия элемента с ошибкой...")
                    error_validation_element = WebDriverWait(self.driver, timeout).until(
                        EC.presence_of_element_located(Train.Error_Notification)
                    )
                    print("Ошибка редиректа - Нет видимости контента страницы Отели")
                    break
                except TimeoutException:
                    print("Элемент с ошибкой не найден, продолжаем...")
                    pass

                self.sleep(1)
        except (TimeoutException, WebDriverException) as e:
            print(f"Exception: {e}")


class Routs(BaseMethods, BaseActions, CheckBoxesMethods):
    RoutsSwitcher = (By.XPATH, '/html/body/div[2]/div/div[4]')
    InputIn = (By.XPATH, '/html/body/section[2]/div/div[4]/form/div[1]/input')
    DropDownExistingMenuIn = (By.XPATH, '/html/body/section[2]/div/div[4]/form/div[1]/div')
    GetItemIn = (By.XPATH, '/html/body/section[2]/div/div[4]/form/div[1]/div/ul/li[1]')
    InputOut = (By.XPATH, '/html/body/section[2]/div/div[4]/form/div[2]/input')
    DropDownExistingMenuOut = (By.XPATH, '/html/body/section[2]/div/div[4]/form/div[2]/div')
    GetItemOut = (By.XPATH, '/html/body/section[2]/div/div[4]/form/div[2]/div/ul/li[1]')
    Submit = (By.XPATH, '/html/body/section[2]/div/div[4]/form/button')

    SuccessBlock = (By.XPATH, '/html/body/main/div[2]/div')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def RoutsLoaded(self, timeout=10):
        self.page_loaded(MainURL.Current_url, timeout)

    def RoutsSwitch(self, timeout=10):
        self.click_element(Routs.RoutsSwitcher, timeout)

    def RoutsPullItemIn(self):
        self.send_keys_to_element(Routs.InputIn, CityDetails.Moscow)

    def DropDownExist(self, timeout=10):
        self.is_element_present(Routs.DropDownExistingMenuIn, timeout)

    def SelectItemIn(self, timeout=10):
        self.click_element(Routs.GetItemIn, timeout)

    def RoutsPullItemOut(self):
        self.send_keys_to_element(Routs.InputOut, CityDetails.Voronezh)

    def DropDownExistOut(self, timeout=10):
        self.is_element_present(Routs.DropDownExistingMenuOut, timeout)

    def SelectItemOut(self, timeout=10):
        self.click_element(Routs.GetItemOut, timeout)

    def OpenRoutsPage(self, timeout=10):
        try:
            print("Начинаем клик на кнопку Submit...")
            self.click_element(Routs.Submit, timeout)

            print("Ожидание появления новой вкладки...")
            WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))

            # Получение списка всех открытых вкладок и переключение на вторую вкладку
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            print("Переключение на новую вкладку выполнено")

            # Ожидание полной загрузки страницы
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            print("Страница полностью загружена")

            # Ожидание, что URL страницы соответствует ожидаемому
            WebDriverWait(self.driver, timeout).until(
                EC.url_to_be(MainURL.Routs_url)
            )
            print("Страница MainURL.Routs_url загрузилась на 100%")

            # Ожидание загрузки ключевого элемента на странице
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(Routs.SuccessBlock)
            )
            print("Ключевой элемент на второй странице загружен и виден")
            print("Успех: страница MainURL.Routs_url загружена на 100% и найден элемент DirectionBlockSuccess")

            # Проверка наличия контента на странице
            if self.is_visible(Routs.SuccessBlock):
                print("На странице обнаружен контент - редирект true")
            else:
                print("На странице нет контента")
                raise AssertionError("Ключевой элемент на второй странице не загрузился или не виден")

            # Проверка наличия элемента Error_Notification
            try:
                error_notification_element = self.driver.find_element(*Train.Error_Notification)
                if error_notification_element.is_displayed():
                    raise AssertionError("Страница не дала результат HTML")
            except NoSuchElementException:
                pass

            response = requests.get(self.driver.current_url)
            status_code = response.status_code
            print(f"Код статуса страницы: {status_code}")

            if status_code == 200:
                print("Успех: Страница успешно загружена")
            else:
                print(f"Ошибка: Страница не загружена, код состояния: {status_code}")

            return True

        except Exception as e:
            print(f"Exception: {e}")
            return False

    def Routs_validation_check_up_pos4(self, s=3):
        input_value = Valid_Data.TourInputSecretTokenHex4
        self.send_keys_to_element(Routs.InputIn, input_value)
        self.sleep(s)
        self.send_keys_to_element(Routs.InputOut, input_value)
        actual_input_value = self.driver.find_element(*Routs.InputIn).get_attribute("value")
        actual_input_value2 = self.driver.find_element(*Routs.InputOut).get_attribute("value")

        assert len(actual_input_value) == len(
            input_value), f"Input field contains {len(actual_input_value)} characters, expected {len(input_value)} characters"
        assert len(actual_input_value) == 8, f"Expected input field length: 25, but got {len(actual_input_value)}"
        assert len(actual_input_value2) == len(
            input_value), f"Input field contains {len(actual_input_value2)} characters, expected {len(input_value)} characters"
        assert len(actual_input_value2) == 8, f"Expected input field length: 25, but got {len(actual_input_value2)}"

        # Проверяем, что введено 8 символов, и завершаем тест с успехом
        if len(actual_input_value) == 8 and len(actual_input_value2) == 8:
            print("Успех: введено 8 символов в оба поля ввода")
            return True

    def Routs_validation_check_up_pos12(self, s=3):
        input_value = Valid_Data.TourInputSecretTokenHex12
        self.send_keys_to_element(Routs.InputIn, input_value)
        self.sleep(s)
        self.send_keys_to_element(Routs.InputOut, input_value)
        actual_input_value = self.driver.find_element(*Routs.InputIn).get_attribute("value")
        actual_input_value2 = self.driver.find_element(*Routs.InputOut).get_attribute("value")

        assert len(actual_input_value) == len(
            input_value), f"Поле ввода содержит {len(actual_input_value)} символов, ожидается {len(input_value)} символов"
        assert len(
            actual_input_value) == 24, f"Ожидаемая длина поля ввода: 24, текущая длина: {len(actual_input_value)}"
        assert len(actual_input_value2) == len(
            input_value), f"Поле ввода содержит {len(actual_input_value2)} символов, ожидается {len(input_value)} символов"
        assert len(
            actual_input_value2) == 24, f"Ожидаемая длина поля ввода: 24, текущая длина: {len(actual_input_value2)}"

        # Проверяем, что введено 8 символов, и завершаем тест с успехом
        if len(actual_input_value) == 24 and len(actual_input_value2) == 24:
            print("Успех: введено 24 символов в оба поля ввода")
            return True

    def Routs_validation_check_up_neg16(self, s=3):
        input_value = Valid_Data.TourInputSecretTokenHex16
        self.send_keys_to_element(Routs.InputIn, input_value)
        self.sleep(s)
        self.send_keys_to_element(Routs.InputOut, input_value)
        actual_input_value = self.driver.find_element(*Routs.InputIn).get_attribute("value")
        actual_input_value2 = self.driver.find_element(*Routs.InputOut).get_attribute("value")

        assert len(actual_input_value) == len(
            input_value), f"Поле ввода содержит {len(actual_input_value)} символов, ожидается {len(input_value)} символов"
        assert len(
            actual_input_value) <= 25, f"Ожидается, что длина поля ввода не будет больше 25 символов, текущая длина: {len(actual_input_value)}"
        assert len(actual_input_value2) == len(
            input_value), f"Поле ввода содержит {len(actual_input_value2)} символов, ожидается {len(input_value)} символов"
        assert len(
            actual_input_value2) <= 25, f"Ожидается, что длина поля ввода не будет больше 25 символов, текущая длина: {len(actual_input_value2)}"

        print("Тест пройден успешно, поле не обрабатывает больше 25 символов")

    def Routs_validation_check_up_neg32(self, s=3):
        input_value = Valid_Data.TourInputSecretTokenHex32
        self.send_keys_to_element(Routs.InputIn, input_value)
        self.sleep(s)
        self.send_keys_to_element(Routs.InputOut, input_value)
        actual_input_value = self.driver.find_element(*Routs.InputIn).get_attribute("value")
        actual_input_value2 = self.driver.find_element(*Routs.InputOut).get_attribute("value")

        assert len(actual_input_value) == len(
            input_value), f"Поле ввода содержит {len(actual_input_value)} символов, ожидается {len(input_value)} символов"
        assert len(
            actual_input_value) <= 25, f"Ожидается, что длина поля ввода не будет больше 25 символов, текущая длина: {len(actual_input_value)}"
        assert len(actual_input_value2) == len(
            input_value), f"Поле ввода содержит {len(actual_input_value2)} символов, ожидается {len(input_value)} символов"
        assert len(
            actual_input_value2) <= 25, f"Ожидается, что длина поля ввода не будет больше 25 символов, текущая длина: {len(actual_input_value2)}"

        print("Тест пройден успешно, поле не обрабатывает больше 25 символов")


class RedirectVacationItem(BaseMethods, BaseActions, CheckBoxesMethods):
    Item1 = (By.XPATH, '/html/body/section[4]/div/div/a[1]')
    Data_count_item1 = (By.XPATH, '/html/body/div[3]/div[2]/p')
    Item2 = (By.XPATH, '/html/body/section[4]/div/div/a[2]')
    Data_count_item2 = (By.XPATH, '//*[@id="header"]/div/div[1]/a[2]')
    Item3 = (By.XPATH, '/html/body/section[4]/div/div/a[3]')
    Data_count_item3 = (By.XPATH, '//*[@id="header"]/div/div[1]/a[2]')
    Item4 = (By.XPATH, '/html/body/section[4]/div/div/a[4]')
    Data_count_item4 = (By.XPATH, '//*[@id="header"]/div/div[1]/a[2]')
    Item5 = (By.XPATH, '/html/body/section[4]/div/div/a[5]')
    Data_count_item5 = (By.XPATH, '//*[@id="header"]/div/div[1]/a[2]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def PageLoaded(self, timout=10):
        self.page_loaded(MainURL.Current_url, timout)

    def ScrollView(self):
        self.window_scroll_by(0, 250)

    def GetItem1(self, timeout=5):
        self.is_element_present(RedirectVacationItem.Item1, timeout)

    def OpenAndReturnItem(self, item_locator, data_count_locator, item_name, timeout=10):
        # Действие: Кликнуть на элемент для открытия новой вкладки
        self.click_element(item_locator, timeout)
        print(f"Действие: Кликнули на элемент {item_name} для открытия новой вкладки")

        # Получить идентификаторы всех открытых вкладок
        window_handles = self.driver.window_handles
        assert len(window_handles) >= 2, f"Проверка: Ожидалось, что будет открыта вторая вкладка для {item_name}"

        # Действие: Переключиться на вторую вкладку
        self.driver.switch_to.window(window_handles[1])
        print("Проверка: Переключились на вторую вкладку")

        # Подождать, пока страница полностью загрузится
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located(data_count_locator))
        print(f"Действие: Страница {item_name} полностью загружена")

        # Получить URL текущей страницы
        current_url = self.driver.current_url

        # Отправить GET-запрос и получить код статуса
        response = requests.get(current_url)
        status_code = response.status_code
        print(f"Код статуса страницы {item_name}: {status_code}")

        # Проверить код статуса и сгенерировать ошибку элемента, если код > 200
        if status_code > 200:
            raise Exception(f"Ошибка элемента {item_name}: Код статуса {status_code}")

        # Подождать, пока элемент станет видимым
        wait = WebDriverWait(self.driver, timeout)
        data_count_element = wait.until(EC.visibility_of_element_located(data_count_locator))
        print("Действие: Элемент стал видимым")

        # Вернуться на предыдущую вкладку
        self.driver.close()
        self.driver.switch_to.window(window_handles[0])
        print("Действие: Вернулись на предыдущую вкладку")


class RedirectSliders(BaseMethods, BaseActions, CheckBoxesMethods):
    Item1 = (By.XPATH, '/html/body/section[5]/div/div[1]/div[1]/div/div/div/div[1]/div[1]/div/a/img')
    data_count_locator = (By.XPATH, '/html/body/div[3]/div[2]/p')
    Item2 = (By.XPATH, '/html/body/section[5]/div/div[1]/div[1]/div/div/div/div[1]/div[2]/div[1]/a/img')
    data_count_locator2 = (By.XPATH, '/html/body/div[3]/div[2]/p')
    Item3 = (By.XPATH, '/html/body/section[5]/div/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/a/img')
    data_count_locator3 = (By.XPATH, '/html/body/div[3]/div[2]/p')
    MoveItems = (By.XPATH, '/html/body/section[5]/div/div[1]/div[1]/div/button[2]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def ScrollView(self):
        self.window_scroll_by(0, 800)

    def PageLoaded(self, timeout=10):
        self.page_loaded(MainURL.Current_url)

    def GetItemContent(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        items = {'Адыгея': self.Item1, 'Байкал': self.Item2, 'Дагестан': self.Item3}
        for location, item in items.items():
            try:
                # Ожидание появления элемента
                wait.until(EC.presence_of_element_located(item))
                print(f"Блок туров {location} был найден")
            except TimeoutException:
                print(f"Блок туров {location} не был найден в течение заданного времени")

    def OpenAndReturnItem(self, item_locator, data_count_locator, item_name, timeout=10):
        try:
            self.click_element(item_locator, timeout)
        except ElementNotInteractableException:
            raise Exception(f"Ошибка: Элемент {item_name} не кликабельный")

        print(f"Действие: Кликнули на элемент {item_name} для открытия новой вкладки")

        window_handles = self.driver.window_handles
        assert len(window_handles) >= 2, f"Проверка: Ожидалось, что будет открыта вторая вкладка для {item_name}"

        self.driver.switch_to.window(window_handles[1])
        print("Проверка: Переключились на вторую вкладку")

        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.text_to_be_present_in_element(data_count_locator, "Найдено"))
        except TimeoutException:
            raise Exception(f"Ошибка: Страница {item_name} загружается слишком долго")

        print(f"Действие: Страница {item_name} полностью загружена")

        current_url = self.driver.current_url

        try:
            response = requests.get(current_url, timeout=10)
        except requests.exceptions.Timeout:
            raise Exception(f"Ошибка: Получение кода статуса для {item_name} заняло слишком много времени")

        status_code = response.status_code
        print(f"Код статуса страницы {item_name}: {status_code}")

        if status_code != 200:
            raise Exception(f"Ошибка элемента {item_name}: Код статуса {status_code}")

        try:
            wait = WebDriverWait(self.driver, timeout)
            data_count_element = wait.until(EC.visibility_of_element_located(data_count_locator))
        except TimeoutException:
            raise Exception(f"Ошибка: Элемент на странице {item_name} не стал видимым в течение заданного времени")

        print("Действие: Элемент стал видимым")

        data_count_text = data_count_element.text
        print(f"Текст элемента data_count: {data_count_text}")

        self.driver.close()
        self.driver.switch_to.window(window_handles[0])
        print("Действие: Вернулись на предыдущую вкладку")

    def MoveItem(self, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.element_to_be_clickable(RedirectSliders.MoveItems))
            self.click_element(RedirectSliders.MoveItems, timeout)
            print("Действие: Успешно кликнули на кнопку для переключения элемента")
        except TimeoutException:
            assert False, "Ошибка: Кнопка для переключения элемента не стала кликабельной в течение заданного времени"


class ArticlesSliders_form(BaseMethods, BaseActions, CheckBoxesMethods):
    ArticlesDescription1 = (By.XPATH, '//*[@id="swiper-wrapper-0710b67dc270042f3"]/div[1]/a/div')
    GetItemAttribute = (By.XPATH, '//*[@id="page-header"]/main/section[1]/div/div/div/div[2]/div[1]/h1')
    ArticlesDescription2 = (By.XPATH, '//*[@id="swiper-wrapper-0710b67dc270042f3"]/div[2]/a/div')
    ArticlesDescription3 = (By.XPATH, '//*[@id="swiper-wrapper-0710b67dc270042f3"]/div[3]/a/div')
    MoveItem = (By.XPATH, '/html/body/section[6]/div/div/div/div[1]/div[3]')

    OpenCountryItemList = (By.XPATH, '//*[@id="select2-country-container"]')
    GetItemCountryList = (By.XPATH, '/html/body/span/span')
    OpenCityItemCityList = (By.XPATH, '//*[@id="select2-city-container"]')
    GetItemCityList = (By.XPATH, '/html/body/span/span')
    OpenThematicItemList = (By.XPATH, '//*[@id="select2-theme-container"]')
    GetItemThematicList = (By.XPATH, '/html/body/span/span')

    Submit = (By.XPATH, '/html/body/section[6]/div/div/div/div[2]/form/button')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def ScrollView(self):
        self.window_scroll_by(0, 1400)

    def PageLoaded(self, timeout=10):
        self.page_loaded(MainURL.Current_url)

    """def GetItemContent(self, timeout=20):
        wait = WebDriverWait(self.driver, timeout)
        items = {'12 лучших': self.ArticlesDescription1, '15 лучших': self.ArticlesDescription2,
                 'Антальи': self.ArticlesDescription3}
        for location, item in items.items():
            try:
                # Ожидание появления элемента
                element = wait.until(EC.presence_of_element_located(item))
                print(f"Описание {location} было найдено")

                # Получение атрибутов элемента
                element_attributes = element.get_attribute('outerHTML')
                print(f"Атрибуты описания {location}: {element_attributes}")
            except TimeoutException:
                print(f"Описание {location} не было найдено в течение заданного времени")"""

    def OpenAndReturnItem(self, item_locator, item_name, timeout=10):
        try:
            self.click_element(item_locator, timeout)
        except ElementNotInteractableException:
            raise Exception(f"Ошибка: Элемент {item_name} не кликабельный")

        print(f"Действие: Кликнули на элемент {item_name} для открытия новой вкладки")

        window_handles = self.driver.window_handles
        assert len(window_handles) >= 2, f"Проверка: Ожидалось, что будет открыта вторая вкладка для {item_name}"

        self.driver.switch_to.window(window_handles[1])
        print("Проверка: Переключились на вторую вкладку")

        data_count_locator = (By.XPATH, '//*[@id="page-header"]/main/section[1]/div/div/div/div[2]/div[1]/h1')

        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.text_to_be_present_in_element(data_count_locator, "Найдено"))
        except TimeoutException:
            raise Exception(f"Ошибка: Страница {item_name} загружается слишком долго")

        print(f"Действие: Страница {item_name} полностью загружена")

        current_url = self.driver.current_url

        try:
            response = requests.get(current_url, timeout=10)
        except requests.exceptions.Timeout:
            raise Exception(f"Ошибка: Получение кода статуса для {item_name} заняло слишком много времени")

        status_code = response.status_code
        print(f"Код статуса страницы {item_name}: {status_code}")

        if status_code != 200:
            raise Exception(f"Ошибка элемента {item_name}: Код статуса {status_code}")

        try:
            wait = WebDriverWait(self.driver, timeout)
            data_count_element = wait.until(EC.visibility_of_element_located(data_count_locator))
        except TimeoutException:
            raise Exception(f"Ошибка: Элемент на странице {item_name} не стал видимым в течение заданного времени")

        print("Действие: Элемент стал видимым")

        data_count_text = data_count_element.text
        print(f"Текст элемента data_count: {data_count_text}")

        self.driver.close()
        self.driver.switch_to.window(window_handles[0])
        print("Действие: Вернулись на предыдущую вкладку")

