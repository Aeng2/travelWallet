import unittest
from appium import webdriver
from appium.options.common import AppiumOptions
from pages.main import MainPage
from pages.search import SearchPage
from pages.charge import ChargePage


class TestScenario(unittest.TestCase):
    def setUp(self):
        appium_server_url = "http://localhost:4724"
        capabilities = AppiumOptions().load_capabilities({
            'platformName': 'iOS',
            'appium:platformVersion': '17.3',
            'automationName': 'XCUITest',
            'appium:udid': '00008120-000144262E40C01E',
            'noReset': True
        })

        self.driver = webdriver.Remote(appium_server_url, options=capabilities)
        self.main_page = MainPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.charge_page = ChargePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_search_scenario(self):
        search_keyword = "노르웨이"
        self.main_page.click_charge_button()
        self.search_page.click_search_box()
        self.search_page.enter_search_keyword(search_keyword)
        self.search_page.click_search_result(search_keyword)
        self.charge_page.check_currency_name(search_keyword)
        self.charge_page.click_back_button()
        self.search_page.click_back_button()
        self.search_page.click_back_button()
