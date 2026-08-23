import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self,driver):
        self.driver = driver

    def scroll_container_to_bottom(self,locator, pause_time=1.5, max_scrolls=100):
        container = self.driver.find_element(By.XPATH, locator)
        last_height = self.driver.execute_script("return arguments[0].scrollHeight;", container)
        scroll_count = 0

        while scroll_count < max_scrolls:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", container)
            time.sleep(pause_time)

            new_height = self.driver.execute_script("return arguments[0].scrollHeight;", container)

            if new_height == last_height:
                break

            last_height = new_height
            scroll_count += 1

    def ScrollIntoView(self,element):
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def WaitForPreseneceOfAllElements(self,locatorType, locator):
        wait = WebDriverWait(self.driver, 10)
        listOfElements = wait.until(EC.presence_of_all_elements_located((locatorType, locator)))

        return listOfElements

    def WaitForPresenceOfElement(self,locatorType,locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((locatorType,locator)))

        return element


    def WaitForAutoSuggest(self, airportCode, departFrom):
        wait = WebDriverWait(self.driver, 15, ignored_exceptions=(StaleElementReferenceException,))
        wait.until(
            lambda d: any(
                airportCode in el.text
                for el in d.find_elements(By.XPATH,departFrom)
            )
        )




# sc-jrAIFA bKcrqQ


