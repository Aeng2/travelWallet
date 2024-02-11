from appium.webdriver.common.appiumby import AppiumBy
from pages.base import BaseFunction


class ChargePage(BaseFunction):
    back_button = (AppiumBy.XPATH,
                   '//XCUIElementTypeNavigationBar[@name="TravelWallet.ChargeAmountView"]/XCUIElementTypeButton')

    def click_back_button(self):
        self.click_by_locator(self.back_button)

    def check_currency_name(self, search_input):
        all_elements = self.find_element_by_locator((AppiumBy.XPATH, '//*'))

        assert any(element.get_attribute("name") and search_input.upper() in element.get_attribute("name").upper()
                   for element in all_elements), f"FAIL: 페이지에서 검색어 '{search_input}' 존재하지 않음"
        print(f"PASS: 페이지에서 검색어 '{search_input}' 확인")
        return

