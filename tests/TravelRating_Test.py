import softest
import pytest
from flaky import flaky

from tests.base_test import BaseTests
from screens.TravelRating import *
from utilities.ReadExcel import *
from utilities.Utils import PageUtils


class travelrating_test(BaseTests, softest.TestCase):
    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -TC_P2_051")
    def test_verify_travelrating_homepage(self):
        travel = travelrating(self.driver)
        description = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'A35')
        self.assertTrue(travel.verify_travelrating_landing(description))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_052")
    def test_verify_Travelrating_tutorial(self):
        travel = travelrating(self.driver)
        banner = read_excel('Austraila_travelrate_tut')
        banner_content = []
        for inner_list in banner:
            banner_content.append(inner_list[0])
        self.assertTrue(travel.verify_TravelRating_tutorial(banner_content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_056")
    def test_verify_Travelrating_tutorial_letspay(self):
        travel = travelrating(self.driver)
        banner = read_excel('Austraila_travelrate_tut')
        banner_content = []
        for inner_list in banner:
            banner_content.append(inner_list[0])
        self.assertTrue(travel.verify_TravelRating_tutorial_lastpage(banner_content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_057")
    def test_verify_Travelrating_game(self):
        travel = travelrating(self.driver)
        q1 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A3')
        q2 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A4')
        q3 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A5')
        q4 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A6')
        self.assertTrue(travel.verify_TravelRating_game(q1, q2, q3, q4))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_058")
    def test_verify_Travelrating_game_header(self):
        travel = travelrating(self.driver)
        q1 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A3')
        q2 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A4')
        q3 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A5')
        q4 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A6')
        self.assertTrue(travel.verify_TravelRating_game_header(q1, q2, q3, q4))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_060")
    def test_verify_Travelrating_pause_quit(self):
        travel = travelrating(self.driver)
        q1 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A3')
        q2 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A4')
        q3 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A5')
        q4 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A6')
        self.assertTrue(travel.verify_TravelRating_game_pause_quit(q1, q2, q3, q4))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_061")
    def test_verify_Travelrating_pause_restart(self):
        travel = travelrating(self.driver)
        q1 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A3')
        q2 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A4')
        q3 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A5')
        q4 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A6')
        self.assertTrue(travel.verify_TravelRating_game_pause_restart(q1, q2, q3, q4))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_061")
    def test_verify_Travelrating_pause_resume(self):
        travel = travelrating(self.driver)
        q1 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A3')
        q2 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A4')
        q3 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A5')
        q4 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A6')
        self.assertTrue(travel.verify_TravelRating_game_pause_resume(q1, q2, q3, q4))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_061")
    def test_verify_Travelrating_progree(self):
        travel = travelrating(self.driver)
        q1 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A3')
        q2 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A4')
        q3 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A5')
        q4 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A6')
        self.assertTrue(travel.verify_TravelRating_progress(q1, q2, q3, q4))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_061")
    def test_verify_Travelrating_clock(self):
        travel = travelrating(self.driver)
        q1 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A3')
        q2 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A4')
        q3 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A5')
        q4 = PageUtils.read_datas_from_excel(self.driver, 'Travel_Rating', 'A6')
        self.assertTrue(travel.verify_TravelRating_clock(q1, q2, q3, q4))
