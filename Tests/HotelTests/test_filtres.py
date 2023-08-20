from ...Pages.Elements.HoltesLocators.Filters import ModuleFiltersLocators
from ..TestBase import BaseTest
import pytest


class TestModule1(BaseTest):
    @pytest.mark.smoke()
    def test_module_1(self, driver):
        driver.get('https://www.votpusk.ru/hotels/russia/moscow')
        module_filters = ModuleFiltersLocators(driver)

        module_filters.Close_modal()
        module_filters.module_1_price_range(5, -10)

        module_filters.module_1_price_input_from()

        module_filters.module_1_price_input_to()

        module_filters.module_1_price_input_negative()

        module_filters.module_1_price_input_sql_injection()

    @pytest.mark.smoke()
    def test_module_2(self, driver):
        driver.get('https://www.votpusk.ru/hotels/russia/moscow')
        checkboxes = ModuleFiltersLocators(driver)

        checkboxes.Close_modal()

        checkboxes.module_2_hotel_rating()

        checkboxes.activate_checkbox()

        checkbox_value = checkboxes.get_checkbox_value()
        checkbox_active_value = checkboxes.get_checkbox_active_value()

        assert checkbox_value == checkbox_active_value, f"Expected checkbox value {checkbox_active_value}, but got {checkbox_value}"

        checkboxes.perform_load_checkbox()

        checkbox_value = checkboxes.get_checkbox_value()
        checkbox_active_value = checkboxes.get_checkbox_active_value()

        assert checkbox_value == checkbox_active_value, f"Expected checkbox value {checkbox_active_value}, but got {checkbox_value}"

        checkboxes.perform_load_checkbox_2()

        checkbox_value = checkboxes.get_checkbox_value()
        checkbox_active_value = checkboxes.get_checkbox_active_value()

        assert checkbox_value == checkbox_active_value, f"Expected checkbox value {checkbox_active_value}, but got {checkbox_value}"

        checkboxes.perform_load_checkbox_3()

        checkbox_value = checkboxes.get_checkbox_value()
        checkbox_active_value = checkboxes.get_checkbox_active_value()

        assert checkbox_value == checkbox_active_value, f"Expected checkbox value {checkbox_active_value}, but got {checkbox_value}"

        checkboxes.perform_load_checkbox_4()

        checkbox_value = checkboxes.get_checkbox_value()
        checkbox_active_value = checkboxes.get_checkbox_active_value()

        assert checkbox_value == checkbox_active_value, f"Expected checkbox value {checkbox_active_value}, but got {checkbox_value}"

    @pytest.mark.smoke()
    def test_module_3(self, driver):
        driver.get('https://www.votpusk.ru/hotels/russia/moscow')
        hotel_rating = ModuleFiltersLocators(driver)
        hotel_rating.hotel_rating_boxes()
        hotel_rating.hotel_rating_boxes_1()
        hotel_rating.hotel_rating_boxes_2()
        hotel_rating.hotel_rating_boxes_3()
        hotel_rating.hotel_rating_boxe_4()

    @pytest.mark.smoke()
    def test_get_price_range_module_4(self, driver):
        driver.get('https://www.votpusk.ru/hotels/russia/moscow')
        close_modal = ModuleFiltersLocators(driver)
        close_modal.Close_modal()
        scroll_into_view = ModuleFiltersLocators(driver)
        scroll_into_view.scroll_into_view()
        get_location = ModuleFiltersLocators(driver)
        get_location.get_location(-10, 50)
        get_location_back = ModuleFiltersLocators(driver)
        get_location_back.get_location_back(-50, 10)
        load_page = ModuleFiltersLocators(driver)
        load_page.load_page()

    @pytest.mark.smoke()
    def test_get_performance_value_from_checkboxes_module_5(self, driver):
        driver.get('https://www.votpusk.ru/hotels/russia/moscow')
        close_modal = ModuleFiltersLocators(driver)
        close_modal.Close_modal()
        scroll_into_view_type_of_apart = ModuleFiltersLocators(driver)
        scroll_into_view_type_of_apart.scroll_into_view_type_of_apart()
        get_performance_value_check_boxes_type_of_apart_1 = ModuleFiltersLocators(driver)
        get_performance_value_check_boxes_type_of_apart_1.get_performance_value_check_boxes_type_of_apart_1()
        get_performance_value_check_boxes_type_of_apart_2 = ModuleFiltersLocators(driver)
        get_performance_value_check_boxes_type_of_apart_2.get_performance_value_check_boxes_type_of_apart_2()
        get_performance_value_check_boxes_type_of_apart_3 = ModuleFiltersLocators(driver)
        get_performance_value_check_boxes_type_of_apart_3.get_performance_value_check_boxes_type_of_apart_3()
        get_performance_value_check_boxes_type_of_apart_4 = ModuleFiltersLocators(driver)
        get_performance_value_check_boxes_type_of_apart_4.get_performance_value_check_boxes_type_of_apart_4()
        get_performance_value_check_boxes_type_of_apart_5 = ModuleFiltersLocators(driver)
        get_performance_value_check_boxes_type_of_apart_5.get_performance_value_check_boxes_type_of_apart_5()

    @pytest.mark.smoke()
    def test_get_performance_value_from_checkboxes_module_6(self, driver):
        driver.get('https://www.votpusk.ru/hotels/russia/moscow')
        close_modal = ModuleFiltersLocators(driver)
        close_modal.Close_modal()
        scroll_into_view_room_amenities = ModuleFiltersLocators(driver)
        scroll_into_view_room_amenities.scroll_into_view_room_amenities()
        get_performance_load_from_amenities_checkboxes_1 = ModuleFiltersLocators(driver)
        get_performance_load_from_amenities_checkboxes_1.get_performance_load_from_amenities_checkboxes_1()
        get_performance_load_from_amenities_checkboxes_2 = ModuleFiltersLocators(driver)
        get_performance_load_from_amenities_checkboxes_2.get_performance_load_from_amenities_checkboxes_2()
        get_performance_load_from_amenities_checkboxes_3 = ModuleFiltersLocators(driver)
        get_performance_load_from_amenities_checkboxes_3.get_performance_load_from_amenities_checkboxes_3()
        get_performance_load_from_amenities_checkboxes_4 = ModuleFiltersLocators(driver)
        get_performance_load_from_amenities_checkboxes_4.get_performance_load_from_amenities_checkboxes_4()
        get_performance_load_from_amenities_checkboxes_5 = ModuleFiltersLocators(driver)
        get_performance_load_from_amenities_checkboxes_5.get_performance_load_from_amenities_checkboxes_5()

    @pytest.mark.smoke()
    def test_get_performance_value_from_checkboxes_module_7(self, driver):
        driver.get('https://www.votpusk.ru/hotels/russia/moscow')
        close_modal = ModuleFiltersLocators(driver)
        close_modal.Close_modal()
        scroll_into_view_hotel_amenities = ModuleFiltersLocators(driver)
        scroll_into_view_hotel_amenities.scroll_into_view_hotel_amenities()
        get_performance_load_from_hotel_amenities_1 = ModuleFiltersLocators(driver)
        get_performance_load_from_hotel_amenities_1.get_performance_load_from_hotel_amenities_1()
        get_performance_load_from_hotel_amenities_2 = ModuleFiltersLocators(driver)
        get_performance_load_from_hotel_amenities_2.get_performance_load_from_hotel_amenities_2()
        get_performance_load_from_hotel_amenities_3 = ModuleFiltersLocators(driver)
        get_performance_load_from_hotel_amenities_3.get_performance_load_from_hotel_amenities_3()
        get_performance_load_from_hotel_amenities_4 = ModuleFiltersLocators(driver)
        get_performance_load_from_hotel_amenities_4.get_performance_load_from_hotel_amenities_4()
        get_performance_load_from_hotel_amenities_5 = ModuleFiltersLocators(driver)
        get_performance_load_from_hotel_amenities_5.get_performance_load_from_hotel_amenities_5()
