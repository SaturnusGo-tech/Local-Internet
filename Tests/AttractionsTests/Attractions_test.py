import time

import pytest
from Local_Internet.Pages.Elements.AttractionsLocators.Attractions import (AttractionsList, ThematicRedirect, \
                                                                           GettingStatusLinksBlocks,
                                                                           NewAttractionsItems, AllTopicRedirectItem,
                                                                           AdditionalArticles, InnerPageAttractions,
                                                                           AttractionsItemsRedirect, Map)
from Local_Internet.Tests.AttractionsTests.TestBase import BaseTest
from Local_Internet.Pages.Base.URLS.Attractions.URL import AttractionsURL


class TestAttractionsList(BaseTest):
    @pytest.mark.Attractions
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

    @pytest.mark.Attractions
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

        # ThematicItems.MoveItem()

    @pytest.mark.Attractions
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

    @pytest.mark.Attractions
    def test_NewAttractionItemsRedirect(self, driver):
        driver.get(AttractionsURL.Current_url)
        AttractionsItemNew = NewAttractionsItems(driver)

        AttractionsItemNew.scroll_view()
        time.sleep(5)

        AttractionsItemNew.attractions_thematic_links_redirect(NewAttractionsItems.NewAttractionsItem1, 'NewAtt'
                                                                                                        'ractionsItem1')

    @pytest.mark.Attractions
    def test_AllTopicItem(self, driver):
        driver.get(AttractionsURL.Current_url)

        AllTopicItems = AllTopicRedirectItem(driver)

        AllTopicItems.ScrollView()

        time.sleep(5)

        AllTopicItems.TopicItemsLinksRedirect(AllTopicRedirectItem.CanyonItem, 'CanyonItem')
        AllTopicItems.TopicItemsLinksRedirect(AllTopicRedirectItem.AquaTopic, 'AquaTopic')
        AllTopicItems.TopicItemsLinksRedirect(AllTopicRedirectItem.Lakes, 'Lakes')
        AllTopicItems.TopicItemsLinksRedirect(AllTopicRedirectItem.Gallery, 'Gallery')
        AllTopicItems.TopicItemsLinksRedirect(AllTopicRedirectItem.Theatre, 'Theatre')

    @pytest.mark.Attractions
    def test_AdditionalArticles(self, driver):
        driver.get(AttractionsURL.Current_url)

        AdditionalArticlesItemsRedirect = AdditionalArticles(driver)

        AdditionalArticlesItemsRedirect.ScrollView()
        time.sleep(5)

        AdditionalArticlesItemsRedirect.AdditionalArticlesRedirect(AdditionalArticles.LinkItem1, 'LinkItem1')
        AdditionalArticlesItemsRedirect.AdditionalArticlesRedirect(AdditionalArticles.LinkItem2, 'LinkItem2')
        AdditionalArticlesItemsRedirect.AdditionalArticlesRedirect(AdditionalArticles.LinkItem3, 'LinkItem3')

        AdditionalArticlesItemsRedirect.OfferBlock(AdditionalArticles.Routs, 'Маршруты')
        AdditionalArticlesItemsRedirect.OfferBlock(AdditionalArticles.Tours, 'Туры')
        AdditionalArticlesItemsRedirect.OfferBlock(AdditionalArticles.Attractions, 'Достопримечательности')
        AdditionalArticlesItemsRedirect.OfferBlock(AdditionalArticles.Hotel, 'Отели')

    @pytest.mark.Attractions
    def test_InnerPageAttractionsItems(self, driver):
        driver.get(AttractionsURL.Current_url)

        attraction_list = InnerPageAttractions(driver)
        attractionsTopics = InnerPageAttractions(driver)

        attraction_list.Scroll_View()
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
        attraction_list.OpenAndReturnItems(AttractionsList.Submit, 'Submit')
        time.sleep(5)

        attractionsTopics.Scroll_View()
        time.sleep(5)
        attractionsTopics.AttractionsTopicsRedirect(InnerPageAttractions.NatureItem, 'Природа')
        time.sleep(5)
        attractionsTopics.AttractionsTopicsRedirect(InnerPageAttractions.ReligionItem, 'Религозные')
        attractionsTopics.AttractionsTopicsRedirect(InnerPageAttractions.FloraItem, 'Флора и Фауна')
        attractionsTopics.AttractionsTopicsRedirect(InnerPageAttractions.HistoricalItem, 'Исторические')
        attractionsTopics.AttractionsTopicsRedirect(InnerPageAttractions.ArchitectureItem, 'Архитектура')
        attractionsTopics.AttractionsTopicsRedirect(InnerPageAttractions.EntertainmentItem, 'Развлечения')

    @pytest.mark.Attractions
    def test_AttractionsBlockRedirecting(self, driver):
        driver.get(AttractionsURL.InnerPage)

        AttractionsInnerPage = AttractionsItemsRedirect(driver)

        AttractionsInnerPage.Scroll_View()
        time.sleep(5)

        AttractionsInnerPage.OpenAndReturnItem(AttractionsItemsRedirect.AttractionsItem1, 'AttractionsItem1')
        AttractionsInnerPage.OpenAndReturnItem(AttractionsItemsRedirect.AttractionsItem2, 'AttractionsItem2')
        AttractionsInnerPage.OpenAndReturnItem(AttractionsItemsRedirect.AttractionsItem3, 'AttractionsItem3')

        AttractionsInnerPage.OpenAndReturnItem(AttractionsItemsRedirect.AttractionsItem4, 'AttractionsItem4')
        AttractionsInnerPage.OpenAndReturnItem(AttractionsItemsRedirect.AttractionsItem5, 'AttractionsItem5')
        AttractionsInnerPage.OpenAndReturnItem(AttractionsItemsRedirect.AttractionsItem6, 'AttractionsItem6')
        time.sleep(2)

        """AttractionsInnerPage.OpenAndReturnItem(AttractionsItemsRedirect.AttractionsItem7, 'AttractionsItem7')
        AttractionsInnerPage.OpenAndReturnItem(AttractionsItemsRedirect.AttractionsItem8, 'AttractionsItem8')
        AttractionsInnerPage.OpenAndReturnItem(AttractionsItemsRedirect.AttractionsItem9, 'AttractionsItem9')

        AttractionsInnerPage.OpenAndReturnItem(AttractionsItemsRedirect.AttractionsItem10, 'AttractionsItem10')
        AttractionsInnerPage.OpenAndReturnItem(AttractionsItemsRedirect.AttractionsItem11, 'AttractionsItem11')
        AttractionsInnerPage.OpenAndReturnItem(AttractionsItemsRedirect.AttractionsItem12, 'AttractionsItem12')
        AttractionsInnerPage.OpenAndReturnItem(AttractionsItemsRedirect.AttractionsItem13, 'AttractionsItem13')"""

    @pytest.mark.Attractions
    def test_map_functionality(self, driver):
        driver.get(AttractionsURL.InnerPage)

        MapFunctionality = Map(driver)

        MapFunctionality.Scroll_View()

        MapFunctionality.map_functionality()
        time.sleep(5)

