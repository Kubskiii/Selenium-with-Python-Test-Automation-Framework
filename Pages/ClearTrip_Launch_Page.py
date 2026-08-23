from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver
from Pages.Search_Flights_Results_Page import SearchFlightsResultsPage


class LaunchPage(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    # Locators
    DEPART_FROM_FIELD = "//input[@placeholder='Where from?']"
    DEPART_FROM_ELEMENT = "//ul[@class='airportList']/li[@class='m-1']"
    DEPART_FROM_RESULTS = "//div[contains(@class,'dropdown')]//ul[contains(@class,'airportList')]/li"

    ARRIVING_TO_FIELD = "//input[@placeholder='Where to?']"
    ARRIVING_TO_ELEMENT = "//p[normalize-space()='New Orleans, US - Louis Armstrong (MSY)']"
    ARRIVING_TO_RESULTS = "//div[contains(@class,'dropdown')]//ul[contains(@class,'airportList')]/li"

    SELECT_DATE_FIELD = "//div[@class='focus:bc-secondary-500 t-all c-pointer flex flex-middle flex-between bg-neutral-100 c-neutral-900 p-4 py-3 px-4 h-10 fs-16 ba-solid bc-default c-neutral-900 fromDiv false']"
    ALL_DATES = "//div[contains(@class, 'DayPicker-Day')]"


    SEARCH_BUTTON = "//button[.//text()[contains(., 'Search Flights')]]"
    POP_UP_BUTTON = "//div[@class='pb-1 px-1 flex flex-middle nmx-1']//*[name()='svg']"

    def getDepartFromField(self):
        return self.driver.find_element(By.XPATH, self.DEPART_FROM_FIELD)

    def getDepartFromElement(self):
        return self.driver.find_element(By.XPATH, self.DEPART_FROM_ELEMENT)

    def getDepartFromResults(self):
        return self.driver.find_element(By.XPATH, self.DEPART_FROM_RESULTS)

    def getArrivingToField(self):
        return self.driver.find_element(By.XPATH, self.ARRIVING_TO_FIELD)

    def getDepartureDateField(self):
        return self.driver.find_element(By.XPATH, self.SELECT_DATE_FIELD)

    def getAllDates(self):
        return self.driver.find_elements(By.XPATH, self.ALL_DATES)

    def getSearchButton(self):
        return self.WaitForPresenceOfElement(By.XPATH, self.SEARCH_BUTTON)

    def getPopUpButtpon(self):
        return self.driver.find_element(By.XPATH, self.POP_UP_BUTTON)

    def enterDepartFromLocatation(self,departLocation,airportCode):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departLocation)


        self.WaitForAutoSuggest(airportCode, self.DEPART_FROM_RESULTS)

        searchResults = self.driver.find_elements(By.XPATH, self.DEPART_FROM_RESULTS)

        for result in searchResults:
            if airportCode in result.text:
                result.click()
                break
    def enterArrivingToLocation(self,arrivingLocation,airportCode):
        self.getArrivingToField().click()
        self.getArrivingToField().send_keys(arrivingLocation)


        self.WaitForAutoSuggest(airportCode, self.ARRIVING_TO_RESULTS)
        searchResults = self.driver.find_elements(By.XPATH, self.ARRIVING_TO_RESULTS)

        for result in searchResults:
            if airportCode in result.text:
                result.click()
                break

    def enterDepartureDate(self,departureDate):
        self.getDepartureDateField().click()
        allDates = self.getAllDates()
        for day in allDates:
            if day.get_attribute("aria-label") == departureDate:
                # days are stored in this format "Fri Jul 31 2026"
                day.click()
                break

    def ClickSearch(self):
         self.getSearchButton().click()

    def ClickPopUp(self):
        self.getPopUpButtpon().click()

    def ScrollToSearchButton(self):
        element = self.getSearchButton()
        self.ScrollIntoView(element)

    def searchFlights(self,departLocation,departCode,arrivingLocation,arrivingCode,departureDate):
        self.ClickPopUp()
        self.enterDepartFromLocatation(departLocation,departCode)
        self.enterArrivingToLocation(arrivingLocation,arrivingCode)
        self.enterDepartureDate(departureDate)
        self.ClickSearch()
        sfp = SearchFlightsResultsPage(self.driver)
        return sfp


