import time

import pytest
import softest
from ddt import ddt, data, unpack

from Pages.ClearTrip_Launch_Page import LaunchPage
from Utilities.Utils import Utils


@pytest.mark.usefixtures("setup")
@ddt
class TestFlightPrices(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self,setup):
        self.lp = LaunchPage(self.driver)
        self.utility = Utils()

    @data(*Utils.ReadDataFromCSV("C:\\Python Selenium\\TestFramework\\Testdata\\testdata.csv"))
    @unpack
    def test_flightprices(self, departingFrom, departureAirportCode, arrivingTo, arrvingAirportCode, date, stops):
    #   search flight (values hardcoded, will be parameterized later)
        sfrp = self.lp.searchFlights(departingFrom,departureAirportCode, arrivingTo,arrvingAirportCode,date)
    #   sort by low to high
        flights = sfrp.GetAllFlightsLowToHigh(stops)

        prices = Utils.ConvertTextToNumber(flights)
        sortedPrices = Utils.SortLowToHigh(prices)
    #   assert that prices displayed are in order from low to high
        self.utility.AssertTwoLists(prices,sortedPrices)








