import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from Local_Internet.Pages.Base.Utils.Hotels.HotelData import TestData
from Local_Internet.Pages.Base.Methods.CheckBoxesMrthods import CheckBoxesMethods
from Local_Internet.Pages.Base.URLS.Main.URL import MainURL
from Local_Internet.Pages.Base.Methods.Methods import BaseMethods
from Local_Internet.Pages.Base.Methods.Base import BaseActions
from Local_Internet.Tests.MainTests.TestData.TestData import CheckBoxes


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



