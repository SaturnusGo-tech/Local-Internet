import time

import pytest
import requests
from Local_Internet.Pages.Elements.MainLocators.Main import MainLocators, MainWorldTour, Hotel
from Local_Internet.Tests.TestBase import BaseTest
from Local_Internet.Pages.Base.URLS.Main.URL import MainURL


class TestRussianTour(BaseTest):
    @pytest.mark.smoke()
    def test_positive(self, driver):
        driver.get(MainURL.Current_url)

        main_page = MainLocators(driver)

        main_page.LoadPage()
        main_page.city_Input()
        main_page.open_trip_menu()
        main_page.scroll_into_View()
        main_page.random_CheckBox_Selection()
        main_page.click_to_unblock()
        main_page.openPage()
        response_code = main_page.openPage()

        assert response_code == 200, f"Network response code was {response_code}, expected 200"

    @pytest.mark.xfail()
    def test_validation_error(self, driver):
        driver.get(MainURL.Current_url)

        main_page = MainLocators(driver)

        main_page.LoadPage()
        response_code = main_page.openPage()

        assert response_code is None, (f"Network response code was {response_code}, expected Ошибка валидации, форма "
                                       f"пропустила ошибку редиректа")

    class TestWorldTour(BaseTest):
        @pytest.mark.smoke
        def test_world_pos(self, driver):
            try:
                driver.get(MainURL.Current_url)

                world_tour_page = MainWorldTour(driver)

                world_tour_page.LoadPage()
                world_tour_page.SwitchToWorldTourToggle()
                world_tour_page.FieldInput()
                world_tour_page.CityAcceptFrom()
                world_tour_page.ClearFieldInput()
                world_tour_page.CityAcceptTo()
                world_tour_page.QuantityMenu()
                world_tour_page.addQuantity()
                world_tour_page.ShowMenuList()
                world_tour_page.OpenMenuList()
                world_tour_page.addChildToLocal()

                response_code = world_tour_page.OpenPageTour()

                assert response_code == 200, f"Network response code was {response_code}, expected 200"
                print("Позитивный сценарий теста был успешно пройден")

            except AssertionError as e:
                print("Тест провален:", e)

        class TestWorldTour(BaseTest):
            @pytest.mark.smoke
            def test_open_page_negative(self, driver):
                try:
                    driver.get(MainURL.Current_url)

                    world_tour_page = MainWorldTour(driver)

                    world_tour_page.LoadPage()
                    world_tour_page.SwitchToWorldTourToggle()

                    response_code = world_tour_page.OpenPageTour()

                    assert response_code != 200, f"Тест провален: ожидался код ответа не равный 200, но получен {response_code}"

                    print("Негативный тест успешно пройден")

                except AssertionError as e:
                    print("Тест провален:", e)
                    raise
                except Exception as e:
                    print("Exception:", e)
                    raise

        @pytest.mark.smoke
        def test_world_neg_pull_attribute(self, driver):
            try:
                driver.get(MainURL.Current_url)

                world_tour_page = MainWorldTour(driver)

                world_tour_page.LoadPage()
                world_tour_page.SwitchToWorldTourToggle()
                world_tour_page.FieldInput()
                world_tour_page.CityAcceptFrom()
                world_tour_page.ClearFieldInput()
                world_tour_page.CityAcceptTo()
                world_tour_page.QuantityMenu()
                world_tour_page.addQuantity()
                world_tour_page.ShowMenuList()
                world_tour_page.OpenMenuList()
                world_tour_page.ScrollView()
                world_tour_page.ClickLoop()

                result = world_tour_page.OpenPageTour()

                if result == "Успешно":
                    print("Тест успешно завершен.")
                else:
                    print("Тест провален:", result)

            except AssertionError as e:
                print("Тест провален:", e)


class TestHotel(BaseTest):
    @pytest.mark.smoke
    def test_hotel_pos(self, driver):
        driver.get(MainURL.Current_url)

        hotel_page = Hotel(driver)

        hotel_page.HotelToggleButton()
        hotel_page.SendKeys()
        hotel_page.Select()
        hotel_page.OpenItem()
        hotel_page.AddLoopItem()
        hotel_page.OpenChildMenuDown()
        hotel_page.GetItems()
        hotel_page.OpenPage()

