import logging
from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver
from Utilities.Utils import Utils

class SearchFlightsResultsPage(BaseDriver):

    log = Utils.CustomLogger(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    NONSTOP_FLIGHT_FILTER = "//div[@class='sc-bdfDLd kqxFRD sc-bf431f9f-0 bBkApZ flex flex-column flex-center p-3 c-pointer mb-3']"
    ONESTOP_FLIGHT_FILTER = "//div[@class='sc-bdfDLd gDayYQ sc-bf431f9f-0 iRBRXh flex flex-column flex-center p-3 c-pointer mb-3']"
    TWOSTOP_FLIGHT_FILTER = "//div[@class='sc-bdfDLd hdBCwG sc-bf431f9f-0 delFbx flex flex-column flex-center p-3 c-pointer mb-3']"

    ALL_FLIGHTS = "//div[contains(@class, 'bAgJWx')]/p[contains(@class, 'AGJlF')]"

    SCROLL_PANE_LOCATOR = "//div[contains(@class, 'iqHrEd')]"

    def getNonStopFlightFilter(self):
        return self.WaitForPresenceOfElement(By.XPATH,self.NONSTOP_FLIGHT_FILTER)

    def getOneStopFlightFilter(self):
        return self.WaitForPresenceOfElement(By.XPATH,self.ONESTOP_FLIGHT_FILTER)

    def getTwoStopFlightFilter(self):
        return self.WaitForPresenceOfElement(By.XPATH,self.TWOSTOP_FLIGHT_FILTER)

    def getAllFlights(self):
        return self.WaitForPreseneceOfAllElements(By.XPATH,self.ALL_FLIGHTS)

    def scroll_to_bottom(self):
        self.scroll_container_to_bottom(self.SCROLL_PANE_LOCATOR)

    def filter_flights_by_stop(self,by_stop):
        if by_stop == "1 stop":
            self.getOneStopFlightFilter().click()
            self.log.warning("Selected flights with 1 stop: ")

        elif by_stop == "2 stops":
            self.getTwoStopFlightFilter().click()
            self.log.warning("Selected flights with 2 stop: ")

        elif by_stop == "Non-stop":
            self.getNonStopFlightFilter().click()
            self.log.warning("Selected non stop flights: ")
        else:
            self.log.warning("PLease Enter Valid Option")






