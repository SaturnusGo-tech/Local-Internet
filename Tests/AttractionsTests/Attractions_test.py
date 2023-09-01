import time

import pytest
from Local_Internet.Pages.Elements.AttractionsLocators.Attractions import AttractionsList, ThematicRedirect, GettingStatusLinksBlocks
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
        attraction_list.SelectCityItem()
        attraction_list.OpenAndReturnItem(AttractionsList.Submit, 'Submit')
        time.sleep(5)

    @pytest.mark.smoke
    def test_ThematicItemsRedirect(self, driver):
        driver.get(AttractionsURL.Current_url)

        ThematicItems = ThematicRedirect(driver)

        ThematicItems.ScrollView()
        time.sleep(5)
        ThematicItems.PageLoaded(expected_url=AttractionsURL.Current_url)
        ThematicItems.TopicItemExist()
        ThematicItems.NameItemsExist(ThematicRedirect.NameItem1, 'NameItem1')

        ThematicItems.NameItemsExist(ThematicRedirect.NameItem2, 'NameItem2')

        ThematicItems.NameItemsExist(ThematicRedirect.NameItem3, 'NameItem3')

        time.sleep(5)

        #ThematicItems.MoveItem()

    def test_Getting_response_data_attractions(self, driver):
        driver.get(AttractionsURL.Current_url)

        AttractionsLinksResponse = GettingStatusLinksBlocks(driver)

        AttractionsLinksResponse.ScrollView()
        time.sleep(5)

        AttractionsLinksResponse.AttractionsItemsLinksRedirect(GettingStatusLinksBlocks.ArtItems1, 'ArtItems1')
        AttractionsLinksResponse.AttractionsItemsLinksRedirect(GettingStatusLinksBlocks.ArtItems2, 'ArtItems2')
        AttractionsLinksResponse.AttractionsItemsLinksRedirect(GettingStatusLinksBlocks.ArtItems3, 'ArtItems3')

        AttractionsLinksResponse.AttractionsItemsLinksRedirect(GettingStatusLinksBlocks.ArtItems4, 'ArtItems4')
        AttractionsLinksResponse.AttractionsItemsLinksRedirect(GettingStatusLinksBlocks.ArtItems5, 'ArtItems5')
        AttractionsLinksResponse.AttractionsItemsLinksRedirect(GettingStatusLinksBlocks.ArtItems6, 'ArtItems6')

        AttractionsLinksResponse.ScrollView_6()
        time.sleep(4)

        AttractionsLinksResponse.AttractionsItemsLinksRedirect(GettingStatusLinksBlocks.ArtItems7, 'ArtItems7')
        AttractionsLinksResponse.AttractionsItemsLinksRedirect(GettingStatusLinksBlocks.ArtItems8, 'ArtItems8')
        AttractionsLinksResponse.AttractionsItemsLinksRedirect(GettingStatusLinksBlocks.ArtItems9, 'ArtItems9')

        time.sleep(5)


