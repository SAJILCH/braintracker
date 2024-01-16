import softest
import pytest
from flaky import flaky

from tests.base_test import BaseTests
from screens.CityTour import *
from utilities.ReadExcel import *
from utilities.Utils import PageUtils


class citytour_test(BaseTests, softest.TestCase):
    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -TC_P2_117")
    def test_verify_citytour_homepage(self):
        travel = citytour(self.driver)
        description = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'A47')
        self.assertTrue(travel.verify_citytour_landing(description))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_118")
    def test_verify_citytour_tutorial(self):
        travel = citytour(self.driver)
        banner = read_excel('Citytour_Tutorial')
        banner_content = []
        for inner_list in banner:
            banner_content.append(inner_list[0])
        print(banner_content)
        self.assertTrue(travel.verify_citytour_tutorial(banner_content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_119")
    def test_verify_citytour_game(self):
        travel = citytour(self.driver)
        banner = read_excel('Citytour_Tutorial')
        banner_content = []
        for inner_list in banner:
            banner_content.append(inner_list[0])
        print(banner_content)
        self.assertTrue(travel.verify_citytour_game())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_120")
    def test_verify_citytour_game_titile(self):
        city = citytour(self.driver)

        self.assertTrue(city.verify_citytour_game())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_120")
    def test_verify_citytour_game_pause_quit(self):
        city = citytour(self.driver)
        self.assertTrue(city.verify_citytour_game_pause_quit())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_121")
    def test_verify_citytour_game_pause_restart(self):
        city = citytour(self.driver)
        self.assertTrue(city.verify_citytour_game_pause_restart())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_122")
    def test_verify_citytour_game_pause_resume(self):
        city = citytour(self.driver)
        self.assertTrue(city.verify_citytour_game_pause_resume())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_123")
    def test_verify_citytour_game_progress(self):
        city = citytour(self.driver)
        self.assertTrue(city.verify_citytour_game_progress())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_123")
    def test_verify_citytour_game_clock(self):
        city = citytour(self.driver)
        self.assertTrue(city.verify_citytour_game_clock())