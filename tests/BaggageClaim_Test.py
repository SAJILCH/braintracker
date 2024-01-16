import softest
import pytest
from flaky import flaky

from tests.base_test import BaseTests
from screens.BaggageClaim import *
from utilities.ReadExcel import *


class baggage_test(BaseTests, softest.TestCase):
    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_016")
    def test_verify_baggage_claim(self):
        cntry = BaggageClaim(self.driver)
        self.assertTrue(cntry.verify_baggage_game())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_017")
    def test_verify_baggage_claim_tutorial(self):
        cntry = BaggageClaim(self.driver)
        content = read_excel('Austraila_Baggage_Tutorial')
        tutorial_cnt = []
        for inner_list in content:
            tutorial_cnt.append(inner_list[0])
        self.assertTrue(cntry.verify_baggageclaim_toutorial(tutorial_cnt))

    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_017")
    def test_verify_baggage_claim_startround(self):
        cntry = BaggageClaim(self.driver)
        self.assertTrue(cntry.verify_baggageclaim_round())


    @pytest.mark.describe("Test case Id - BP_TC_017")
    def test_verify_baggage_claim_game(self):
        cntry = BaggageClaim(self.driver)
        self.assertTrue(cntry.verify_baggageclaim_Game())