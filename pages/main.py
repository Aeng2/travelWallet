from appium.webdriver.common.appiumby import AppiumBy
from pages.base import BaseFunction


class MainPage(BaseFunction):
    charge_button = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="충전하기"]')

    def click_charge_button(self):
        self.click_by_locator(self.charge_button)
