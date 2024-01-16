import softest
import pytest
from flaky import flaky

from tests.base_test import BaseTests
from screens.PackYourBag import *
from utilities.ReadExcel import *
from utilities.Utils import PageUtils


class packyourbag_test(BaseTests, softest.TestCase):
    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -TC_P2_055")
    def test_verify_packyourbag_homepage(self):
        travel = packyourbag(self.driver)
        description = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'A38')
        self.assertTrue(travel.verify_packyourbag_landing(description))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_056")
    def test_verify_packyourbag_tutorial(self):
        travel = packyourbag(self.driver)
        banner = read_excel('PackYourBag_Tutorial')
        banner_content = []
        for inner_list in banner:
            banner_content.append(inner_list[0])
        print(banner_content)
        self.assertTrue(travel.verify_Packyourbag_tutorial(banner_content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -  TC_P2_073")
    def test_verify_packyourbag_game(self):
        travel = packyourbag(self.driver)
        self.assertTrue(travel.verify_Packyourbag_game())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -  TC_P2_074")
    def test_verify_packyourbag_game_titile(self):
        travel = packyourbag(self.driver)
        self.assertTrue(travel.verify_Packyourbag_game())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -  TC_P2_075")
    def test_verify_packyourbag_game_headertext(self):
        travel = packyourbag(self.driver)
        self.assertTrue(travel.verify_Packyourbag_game_header())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -  TC_P2_078")
    def test_verify_packyourbag_game_actionbutton(self):
        travel = packyourbag(self.driver)
        self.assertTrue(travel.verify_Packyourbag_game_round_Actionbuttons())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -  TC_P2_079")
    def test_verify_packyourbag_game_closebutton(self):
        travel = packyourbag(self.driver)
        self.assertTrue(travel.verify_Packyourbag_game_close())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -  TC_P2_088")
    def test_verify_packyourbag_game_result(self):
        travel = packyourbag(self.driver)
        self.assertTrue(travel.verify_Packyourbag_game_result())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -  TC_P2_089")
    def test_verify_packyourbag_game_restart(self):
        travel = packyourbag(self.driver)
        self.assertTrue(travel.verify_Packyourbag_game_restart())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -  TC_P2_089")
    def test_verify_packyourbag_game_resume(self):
        travel = packyourbag(self.driver)
        self.assertTrue(travel.verify_Packyourbag_game_resume())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -  TC_P2_090")
    def test_verify_packyourbag_game_progress(self):
        travel = packyourbag(self.driver)
        self.assertTrue(travel.verify_Packyourbag_game_progress())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -  TC_P2_091")
    def test_verify_packyourbag_game_clock(self):
        travel = packyourbag(self.driver)
        self.assertTrue(travel.verify_Packyourbag_game_clock())