import time

import pytest
from Local_Internet.Pages.Elements.AttractionsLocators.Attractions import AttractionsList
from Local_Internet.Tests.AttractionsTests.TestBase import BaseTest
from Local_Internet.Pages.Base.URLS.Attractions.URL import AttractionsURL


class TestAttractionsList(BaseTest):
    @pytest.mark.smoke
    def test_AttractionsList(self, driver):
        driver.get(AttractionsURL.Current_url)

        attraction_list = AttractionsList(driver)

        attraction_list.ScrollView()
        attraction_list.PageLoaded(
            expected_url=AttractionsURL.Current_url)
        time.sleep(5)
        attraction_list.OpenCountryItems()
        attraction_list.GetCountryListItems()
        attraction_list.SelectCountryItem()
        time.sleep(5)
        attraction_list.OpenCityItems()
        attraction_list.GetCityListItems()
        time.sleep(5)

