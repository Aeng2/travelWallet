from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import TimeoutException


class BaseFunction:
    def __init__(self, driver):
        self.driver = driver

    def click_by_locator(self, element_locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(element_locator)).click()

    def enter_keyword(self, keyword, element_locator):
        element = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(element_locator))
        element.send_keys(keyword)

    def find_element_by_locator(self, element_locator):
        try:
            element = WebDriverWait(self.driver, 5).until(
                expected_conditions.presence_of_all_elements_located(element_locator))
            return element
        except TimeoutException:
            return []
