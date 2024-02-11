from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
from pages.base import BaseFunction


class SearchPage(BaseFunction):
    search_box = (AppiumBy.CLASS_NAME, "XCUIElementTypeTextField")
    back_button = (AppiumBy.XPATH, '//XCUIElementTypeNavigationBar\
    [@name="TravelWallet.SelectCurrencyView"]/XCUIElementTypeButton')

    def click_search_box(self):
        self.click_by_locator(self.search_box)

    def enter_search_keyword(self, search_input):
        self.enter_keyword(search_input, self.search_box)
        self.enter_keyword(Keys.RETURN, self.search_box)
        print(f"'{search_input}' 입력")

    def click_back_button(self):
        self.click_by_locator(self.back_button)

    def click_search_result(self, search_keyword):
        search_result = (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[@name="{search_keyword.upper()}"]')

        self.click_by_locator(search_result)
