import time

import pytest
import softest
from ddt import ddt

from Pages.ClearTrip_Launch_Page import LaunchPage
from Utilities.Utils import Utils


@pytest.mark.usefixtures("setup")
class TestFlightPrices(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self,setup):
        self.lp = LaunchPage(self.driver)
        self.utility = Utils()


    def test_flightprices(self):
    #     search flight (values hardcoded, will be parameterized later)
        sfrp = self.lp.searchFlights("New York","(JFK)","New Orleans","(MSY)","Wed Sep 16 2026")
    #     sort by low to high
        flights = sfrp.GetAllFlightsLowToHigh("1 stop")

        prices = Utils.ConvertTextToNumber(flights)

        sortedPrices = Utils.SortLowToHigh(prices)

        self.utility.AssertTwoLists(prices,sortedPrices)




    #     assert that prices displayed are in order from low to high


# python -m pytest Testcases\test_flightprices.py -v -s --browser chrome --url https://www.cleartrip.com/
