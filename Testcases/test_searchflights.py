import logging
import pytest
import softest


from Pages.ClearTrip_Launch_Page import LaunchPage
from Utilities.Utils import Utils
from ddt import ddt,data,file_data,unpack

@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):

    log = Utils.CustomLogger(logLevel=logging.DEBUG)

    @pytest.fixture(autouse=True)
    def class_setup(self,setup):
        self.lp = LaunchPage(self.driver)
        self.utility = Utils()

    @data(*Utils.ReadDataFromCSV("C:\\Python Selenium\\TestFramework\\Testdata\\testdata.csv"))
    @unpack
    def test_search_flights(self, departingFrom, departureAirportCode, arrivingTo, arrvingAirportCode, date, stops):
        # Launch Website
        #Searches Flights
        sfp = self.lp.searchFlights(departingFrom,departureAirportCode, arrivingTo,arrvingAirportCode,date)
        # Select non stop filter
        sfp.filter_flights_by_stop(stops)
        # Handle infinite Scroll
        sfp.scroll_to_bottom()
        # Get all of the flights
        allStops = sfp.getAllFlights()
        #Verify that all flights are nonstop
        self.log.info(len(allStops))
        self.utility.AssertListItems(allStops,stops)






