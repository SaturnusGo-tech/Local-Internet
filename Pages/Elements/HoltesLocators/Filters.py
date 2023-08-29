from selenium.webdriver.common.by import By
from Local_Internet.Pages.Base.Utils.Hotels.HotelData import TestData
from Local_Internet.Pages.Base.Methods.CheckBoxesMrthods import CheckBoxesMethods
from selenium.common.exceptions import NoSuchElementException

from Local_Internet.Pages.Base.Methods.Methods import BaseMethods


# Класс с локаторами элементов страницы
class ModuleFiltersLocators(BaseMethods, CheckBoxesMethods):
    # Локаторы элементов
    CLOSE_MODAL = (By.XPATH, '//*[@id="hotels-modal-search"]/button')  # Кнопка закрытия модального окна
    Price_slider = (By.XPATH, '//*[@id="price-range"]/div/div[1]')  # Ползунок ценового диапазона
    Price_input_from = (By.ID, 'price-range-input-from')  # Поле ввода начальной цены
    Price_input_to = (By.ID, 'price-range-input-to')  # Поле ввода конечной цены
    CHECK_BOX_NULL = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[3]/div/ul/li[1]/label')
    CHECK_BOX_1_STAR = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[3]/div/ul/li[2]/label')
    CHECK_BOX_2_STAR = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[3]/div/ul/li[3]/label')
    CHECK_BOX_3_STAR = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[3]/div/ul/li[4]/label')
    CHECK_BOX_4_STAR = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[3]/div/ul/li[5]/label')
    CHECK_BOX_5_STAR = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[3]/div/ul/li[6]/label')
    STAR_RATING_HIDDEN_ARROW = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[3]/button')

    ANY_RATING = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[4]/div/ul/li[1]/label/span[2]')
    RATING_6 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[4]/div/ul/li[2]/label/span[2]')
    RATING_7 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[4]/div/ul/li[3]/label/span[2]')
    RATING_8 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[4]/div/ul/li[4]/label/span[2]')
    RATING_9 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[4]/div/ul/li[5]/label/span[2]')
    RATING_HIDDEN_ARROW = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[4]/button')

    DISTANCE_TO_THE_CENTER_SLIDER = (
        By.XPATH, '//*[@id="distance-range"]/div/div[1]/div')

    CHECK_BOX_1 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[6]/div/ul/li[1]/label/span[1]')
    CHECK_BOX_2 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[6]/div/ul/li[5]/label/span[1]')
    CHECK_BOX_3 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[6]/div/ul/li[2]/label/span[1]')
    CHECK_BOX_4 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[6]/div/ul/li[3]/label/span[1]')
    CHECK_BOX_5 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[6]/div/ul/li[4]/label/span[1]')

    AMENITIES_CHECK_BOX_1 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[7]/div/ul/li[1]/label/span[1]')
    AMENITIES_CHECK_BOX_5 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[7]/div/ul/li[3]/label/span[1]')
    AMENITIES_CHECK_BOX_4 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[7]/div/ul/li[2]/label/span[1]')
    AMENITIES_CHECK_BOX_3 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[7]/div/ul/li[5]/label/span[1]')
    AMENITIES_CHECK_BOX_2 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[7]/div/ul/li[4]/label/span[1]')

    AMENITIES_IN_THE_ROOM_CHECK_BOX_1 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[8]/div/ul/li[1]/label/span[1]')
    AMENITIES_IN_THE_ROOM_CHECK_BOX_2 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[8]/div/ul/li[2]/label/span[1]')
    AMENITIES_IN_THE_ROOM_CHECK_BOX_3 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[8]/div/ul/li[3]/label/span[1]')
    AMENITIES_IN_THE_ROOM_CHECK_BOX_4 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[8]/div/ul/li[4]/label/span[1]')
    AMENITIES_IN_THE_ROOM_CHECK_BOX_5 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[8]/div/ul/li[5]/label/span[1]')

    CLEAR_DEFAULT_OPTIONS = (By.CSS_SELECTOR, '[class="filters__apply-btn"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Метод для закрытия модального окна
    def Close_modal(self, y=2):
        self.click_element(ModuleFiltersLocators.CLOSE_MODAL)  # Нажатие на кнопку закрытия модального окна
        self.sleep(y)  # Ожидание завершения анимации или других действий

    # Метод для перемещения ползунка ценового диапазона
    def module_1_price_range(self, offset_x, offset_y, y=20):
        slider_element = self.driver.find_element(*ModuleFiltersLocators.Price_slider)  # Поиск элемента ползунка
        self.move_slider(slider_element, offset_x, offset_y)  # Перемещение ползунка на заданное смещение
        self.sleep(y)  # Ожидание завершения анимации или других действий

    # ... другие методы ...

    # Метод для ввода начальной цены
    def module_1_price_input_from(self, x=3):
        self.send_keys_to_element(ModuleFiltersLocators.Price_input_to, TestData.POSITIVE)  # Ввод значения в поле ввода
        self.sleep(x)  # Ожидание завершения действий

    # Метод для ввода конечной цены
    def module_1_price_input_to(self, s=2):
        self.send_keys_to_element(ModuleFiltersLocators.Price_input_from,
                                  TestData.POSITIVE)  # Ввод значения в поле ввода
        self.sleep(s)  # Ожидание завершения действий

    # Метод для ввода отрицательной цены
    def module_1_price_input_negative(self, s=2):
        self.send_keys_to_element(ModuleFiltersLocators.Price_input_from,
                                  TestData.NEGATIVE)  # Ввод значения в поле ввода
        self.sleep(s)  # Ожидание завершения действий

    # Метод для ввода SQL инъекции
    def module_1_price_input_sql_injection(self, s=2):
        self.send_keys_to_element(ModuleFiltersLocators.Price_input_from,
                                  TestData.SQL_INJECTION)  # Ввод значения в поле ввода
        self.sleep(s)  # Ожидание завершения действий

    def module_2_hotel_rating(self, h=5):
        self.assert_checkbox_not_selected(ModuleFiltersLocators.CHECK_BOX_NULL)
        self.sleep(h)

    def activate_checkbox(self, s=2):
        self.click_element(ModuleFiltersLocators.CHECK_BOX_1_STAR)
        self.sleep(s)

    def get_checkbox_value(self, s=2):
        self.assert_checkbox_not_selected(ModuleFiltersLocators.CHECK_BOX_1_STAR)
        self.sleep(s)

    def get_checkbox_active_value(self, s=2):
        self.assert_checkbox_enabled(ModuleFiltersLocators.CHECK_BOX_1_STAR)
        self.sleep(s)

    def perform_load_checkbox(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.CHECK_BOX_1_STAR)
        self.sleep(s)

    def perform_load_checkbox_1(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.CHECK_BOX_2_STAR)
        self.sleep(s)

    def perform_load_checkbox_2(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.CHECK_BOX_3_STAR)
        self.sleep(s)

    def perform_load_checkbox_3(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.CHECK_BOX_4_STAR)
        self.sleep(s)

    def perform_load_checkbox_4(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.CHECK_BOX_5_STAR)
        self.sleep(s)

    def hotel_rating_boxes(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.ANY_RATING)
        self.sleep(s)

    def hotel_rating_boxes_1(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.RATING_6)
        self.sleep(s)

    def hotel_rating_boxes_2(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.RATING_7)
        self.sleep(s)

    def hotel_rating_boxes_3(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.RATING_8)
        self.sleep(s)

    def hotel_rating_boxe_4(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.RATING_8)
        self.sleep(s)

    def scroll_into_view(self, s=2):
        self.window_scroll_by(0, 350)
        self.sleep(s)

    def get_location(self, offset_x, offset_y, y=2):
        slider_element = self.driver.find_element(*ModuleFiltersLocators.DISTANCE_TO_THE_CENTER_SLIDER)  # Поиск элемента ползунка
        self.move_slider(slider_element, offset_x, offset_y)  # Перемещение ползунка на заданное смещение
        self.sleep(y)  # Ожидание завершения анимации или других действий

    def get_location_back(self, offset_x, offset_y, y=2):
        slider_element = self.driver.find_element(
            *ModuleFiltersLocators.DISTANCE_TO_THE_CENTER_SLIDER)  # Поиск элемента ползунка
        self.move_slider(slider_element, offset_x, offset_y)  # Перемещение ползунка на заданное смещение
        self.sleep(y)  # Ожидание завершения анимации или других действий

    def load_page(self, s=10):
        self.sleep(s)

    def scroll_into_view_type_of_apart(self, s=2):
        self.window_scroll_by(0, 550)
        self.sleep(s)

    def get_performance_value_check_boxes_type_of_apart_1(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.CHECK_BOX_1)
        self.sleep(s)

    def get_performance_value_check_boxes_type_of_apart_2(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.CHECK_BOX_2)
        self.sleep(s)

    def get_performance_value_check_boxes_type_of_apart_3(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.CHECK_BOX_3)
        self.sleep(s)

    def get_performance_value_check_boxes_type_of_apart_4(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.CHECK_BOX_4)
        self.sleep(s)

    def get_performance_value_check_boxes_type_of_apart_5(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.CHECK_BOX_5)
        self.sleep(s)

    def scroll_into_view_room_amenities(self, x=2):
        self.window_scroll_by(0, 950)
        self.sleep(x)

    def get_performance_load_from_amenities_checkboxes_1(self, x=3):
        self.perform_load_test(ModuleFiltersLocators.AMENITIES_CHECK_BOX_1)
        self.sleep(x)

    def get_performance_load_from_amenities_checkboxes_2(self, x=3):
        self.perform_load_test(ModuleFiltersLocators.AMENITIES_CHECK_BOX_2)
        self.sleep(x)

    def get_performance_load_from_amenities_checkboxes_3(self, x=3):
        self.perform_load_test(ModuleFiltersLocators.AMENITIES_CHECK_BOX_3)
        self.sleep(x)

    def get_performance_load_from_amenities_checkboxes_4(self, x=3):
        self.perform_load_test(ModuleFiltersLocators.AMENITIES_CHECK_BOX_4)
        self.sleep(x)

    def get_performance_load_from_amenities_checkboxes_5(self, x=3):
        self.perform_load_test(ModuleFiltersLocators.AMENITIES_CHECK_BOX_4)
        self.sleep(x)

    def scroll_into_view_hotel_amenities(self, s=2):
        self.window_scroll_by(0, 1200)
        self.sleep(s)

    def get_performance_load_from_hotel_amenities_1(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.AMENITIES_IN_THE_ROOM_CHECK_BOX_1)
        self.sleep(s)

    def get_performance_load_from_hotel_amenities_2(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.AMENITIES_IN_THE_ROOM_CHECK_BOX_2)
        self.sleep(s)

    def get_performance_load_from_hotel_amenities_3(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.AMENITIES_IN_THE_ROOM_CHECK_BOX_3)
        self.sleep(s)

    def get_performance_load_from_hotel_amenities_4(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.AMENITIES_IN_THE_ROOM_CHECK_BOX_4)
        self.sleep(s)

    def get_performance_load_from_hotel_amenities_5(self, s=2):
        self.perform_load_test(ModuleFiltersLocators.AMENITIES_IN_THE_ROOM_CHECK_BOX_5)
        self.sleep(s)
