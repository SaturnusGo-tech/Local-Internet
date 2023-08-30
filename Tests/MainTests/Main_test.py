import time

import pytest
import requests
from Local_Internet.Pages.Elements.MainLocators.Main import MainLocators, MainWorldTour, Hotel, Train, Routs
from Local_Internet.Tests.MainTests.TestData.Validation_data.Validation_data_items import Valid_Data
from Local_Internet.Tests.TestBase import BaseTest
from Local_Internet.Pages.Base.URLS.Main.URL import MainURL


class TestRussianTour(BaseTest):
    @pytest.mark.smoke()
    def test_tour_positive(self, driver):
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

    @pytest.mark.smoke()
    def test_positive_with_hex_values4(self, driver):
        driver.get(MainURL.Current_url)

        main_page_Validation = MainLocators(driver)

        main_page_Validation.LoadPage()
        main_page_Validation.validation_check_up_pos()
        main_page_Validation.openPage()

        current_page_url = driver.current_url

        response = requests.get(current_page_url)
        assert response.status_code == 200, f"Network response code was {response.status_code}, expected 200"

    @pytest.mark.smoke()
    def test_positive_with_hex_values12(self, driver):
        driver.get(MainURL.Current_url)

        main_page_Validation = MainLocators(driver)

        main_page_Validation.LoadPage()
        main_page_Validation.validation_check_up_pos25()
        main_page_Validation.openPage()

        current_page_url = driver.current_url

        response = requests.get(current_page_url)
        assert response.status_code == 200, f"Network response code was {response.status_code}, expected 200"

    @pytest.mark.xfail()
    def test_negative_with_hex_values16(self, driver):
        driver.get(MainURL.Current_url)

        main_page_Validation = MainLocators(driver)

        main_page_Validation.LoadPage()
        main_page_Validation.validation_check_up_neg16()
        main_page_Validation.openPage()

        current_page_url = driver.current_url

        response = requests.get(current_page_url)
        assert response.status_code == 200, f"Network response code was {response.status_code}, expected 200"

    @pytest.mark.xfail()
    def test_negative_with_hex_values32(self, driver):
        driver.get(MainURL.Current_url)

        main_page_Validation = MainLocators(driver)

        main_page_Validation.LoadPage()
        main_page_Validation.validation_check_up_neg32()
        main_page_Validation.openPage()

        current_page_url = driver.current_url

        response = requests.get(current_page_url)
        assert response.status_code == 200, f"Network response code was {response.status_code}, expected 200"

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

        @pytest.mark.smoke()
        def test_positive_with_hex_values4(self, driver):
            driver.get(MainURL.Current_url)

            main_page_Validation = MainWorldTour(driver)

            main_page_Validation.LoadPage()
            main_page_Validation.LoadPage()
            main_page_Validation.SwitchToWorldTourToggle()
            main_page_Validation.validation_check_up_pos4()
            main_page_Validation.OpenPageTour()

            current_page_url = driver.current_url

            response = requests.get(current_page_url)
            assert response.status_code == 200, f"Network response code was {response.status_code}, expected 200"

        @pytest.mark.smoke()
        def test_positive_with_hex_values12(self, driver):
            driver.get(MainURL.Current_url)

            main_page_Validation = MainLocators(driver)

            main_page_Validation.LoadPage()
            main_page_Validation.validation_check_up_pos25()
            main_page_Validation.openPage()

            current_page_url = driver.current_url

            response = requests.get(current_page_url)
            assert response.status_code == 200, f"Network response code was {response.status_code}, expected 200"

        @pytest.mark.xfail()
        def test_negative_with_hex_values16(self, driver):
            driver.get(MainURL.Current_url)

            main_page_Validation = MainLocators(driver)

            main_page_Validation.LoadPage()
            main_page_Validation.validation_check_up_neg16()
            main_page_Validation.openPage()

            current_page_url = driver.current_url

            response = requests.get(current_page_url)
            assert response.status_code == 200, f"Network response code was {response.status_code}, expected 200"

        @pytest.mark.xfail()
        def test_negative_with_hex_values32(self, driver):
            driver.get(MainURL.Current_url)

            main_page_Validation = MainLocators(driver)

            main_page_Validation.LoadPage()
            main_page_Validation.validation_check_up_neg32()
            main_page_Validation.openPage()

            current_page_url = driver.current_url

            response = requests.get(current_page_url)
            assert response.status_code == 200, f"Network response code was {response.status_code}, expected 200"


class TestHotel(BaseTest):
    @pytest.mark.smoke
    def test_hotel_redirect(self, driver):
        driver.get(MainURL.Current_url)

        hotel_page = Hotel(driver)

        hotel_page.HotelToggleButton()
        hotel_page.SendKeys()
        hotel_page.DropdownMenuExist()
        hotel_page.Select()
        hotel_page.OpenItem()
        hotel_page.AddLoopItem()
        hotel_page.OpenChildMenuDown()
        hotel_page.GetItems()
        time.sleep(3)
        hotel_page.OpenPage()

    @pytest.mark.smoke
    def test_hotel_validation_checkUp_Len8(self, driver):
        driver.get(MainURL.Current_url)

        hotel_validation = Hotel(driver)

        hotel_validation.HotelToggleButton()
        hotel_validation.validation_check_up_pos()
        hotel_validation.DropdownMenuExist()
        time.sleep(3)
        hotel_validation.OpenPage()

    @pytest.mark.smoke
    def test_hotel_validation_checkUp_Len24(self, driver):
        driver.get(MainURL.Current_url)

        hotel_validation = Hotel(driver)

        hotel_validation.HotelToggleButton()
        hotel_validation.validation_check_up_pos25()
        hotel_validation.DropdownMenuExist()
        time.sleep(3)
        hotel_validation.OpenPage()

    @pytest.mark.xfail
    def test_hotel_validation_checkUp_Len32(self, driver):
        driver.get(MainURL.Current_url)

        hotel_validation = Hotel(driver)

        hotel_validation.HotelToggleButton()
        hotel_validation.validation_check_up_neg16()
        hotel_validation.DropdownMenuExist()
        time.sleep(3)
        hotel_validation.OpenPage()

    @pytest.mark.xfail
    def test_hotel_validation_checkUp_Len64(self, driver):
        driver.get(MainURL.Current_url)

        hotel_validation = Hotel(driver)

        hotel_validation.HotelToggleButton()
        hotel_validation.validation_check_up_neg32()
        hotel_validation.DropdownMenuExist()
        time.sleep(3)
        hotel_validation.OpenPage()


class TestTrain(BaseTest):
    @pytest.mark.smoke
    def test_Train_Redirect(self, driver, s=3):
        driver.get(MainURL.Current_url)

        train_redirecting = Train(driver)

        train_redirecting.Page_Loaded()
        train_redirecting.TrainSwitch()
        train_redirecting.GetInputIn()
        time.sleep(s)
        train_redirecting.DropdownMenuExistIn()
        train_redirecting.SelectCityItemIn()
        train_redirecting.GitInputOut()
        time.sleep(s)
        train_redirecting.DropdownMenuExistOut()
        train_redirecting.SelectCityItemOut()
        time.sleep(s)
        train_redirecting.OpenPage()

    @pytest.mark.smoke
    def test_validationPos8(self, driver):
        driver.get(MainURL.Current_url)

        train_validation = Train(driver)

        train_validation.Page_Loaded()
        train_validation.TrainSwitch()
        train_validation.Train_validation_check_up_pos4()

    @pytest.mark.smoke
    def test_validationPos25(self, driver):

        driver.get(MainURL.Current_url)

        train_validation = Train(driver)

        train_validation.Page_Loaded()
        train_validation.TrainSwitch()
        train_validation.Train_validation_check_up_pos12()

    @pytest.mark.xfail
    def test_validationNeg32(self, driver):

        driver.get(MainURL.Current_url)

        train_validation = Train(driver)

        train_validation.Page_Loaded()
        train_validation.TrainSwitch()
        train_validation.Train_validation_check_up_neg16()

    @pytest.mark.xfail
    def test_validationNeg64(self, driver):
        driver.get(MainURL.Current_url)

        train_validation = Train(driver)

        train_validation.Page_Loaded()
        train_validation.TrainSwitch()
        train_validation.Train_validation_check_up_neg32()


class TestRouts(BaseTest):
    @pytest.mark.smoke
    def test_routs_redirect(self, driver):
        driver.get(MainURL.Current_url)

        routs_redirect = Routs(driver)

        routs_redirect.RoutsLoaded()
        routs_redirect.RoutsSwitch()
        routs_redirect.RoutsPullItemIn()
        routs_redirect.DropDownExist()
        routs_redirect.SelectItemIn()
        routs_redirect.RoutsPullItemOut()
        routs_redirect.DropDownExistOut()
        routs_redirect.SelectItemOut()
        routs_redirect.OpenRoutsPage()

    @pytest.mark.smoke
    def test_validationPos8(self, driver):
        driver.get(MainURL.Current_url)

        routs_validation = Routs(driver)

        routs_validation.RoutsLoaded()
        routs_validation.RoutsSwitch()

        routs_validation.Routs_validation_check_up_pos4()

    @pytest.mark.smoke
    def test_validationPos25(self, driver):
        driver.get(MainURL.Current_url)

        routs_validation = Routs(driver)

        routs_validation.RoutsLoaded()
        routs_validation.RoutsSwitch()

        routs_validation.Routs_validation_check_up_pos12()

    @pytest.mark.xfail
    def test_validationNeg32(self, driver):
        driver.get(MainURL.Current_url)

        routs_validation = Routs(driver)

        routs_validation.RoutsLoaded()
        routs_validation.RoutsSwitch()

        routs_validation.Routs_validation_check_up_neg16()

    @pytest.mark.xfail
    def test_validationPos64(self, driver):
        driver.get(MainURL.Current_url)

        routs_validation = Routs(driver)

        routs_validation.RoutsLoaded()
        routs_validation.RoutsSwitch()

        routs_validation.Routs_validation_check_up_neg32()
