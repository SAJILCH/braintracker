import softest
import pytest
from flaky import flaky

from tests.base_test import BaseTests
from screens.MarketPlace import *
from utilities.ReadExcel import *
from utilities.Utils import PageUtils


class marketplace_test(BaseTests, softest.TestCase):
    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_030")
    def test_verify_marketplace_banner(self):
        cntry = marketplace(self.driver)
        banner = read_excel('Play_marketplace')
        banner_content = []
        for inner_list in banner:
            banner_content.append(inner_list[0])
        self.assertTrue(cntry.verify_marketplace(banner_content))


    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_031")
    def test_verify_marketplace_back_button(self):
        cntry = marketplace(self.driver)
        banner = read_excel('Play_marketplace')
        banner_content = []
        for inner_list in banner:
            banner_content.append(inner_list[0])
        self.assertTrue(cntry.verify_marketplace_backbutton(banner_content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_033")
    def test_verify_marketplace_introduction_description(self):
        cntry = marketplace(self.driver)
        description = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'A26')
        self.assertTrue(cntry.verify_marketplace_intro_screen_discription(description))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_032")
    def test_verify_marketplace_introduction_name(self):
        cntry = marketplace(self.driver)
        description = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'A26')
        self.assertTrue(cntry.verify_marketplace_intro_screen_name(description))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_034")
    def test_verify_marketplace_letsplay_button(self):
        cntry = marketplace(self.driver)
        banner = read_excel('Play_marketplace')
        banner_content = []
        for inner_list in banner:
            banner_content.append(inner_list[0])
        self.assertTrue(cntry.verify_marketplace_play_button(banner_content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_035")
    def test_verify_marketplace_tutorial(self):
        cntry = marketplace(self.driver)
        banner = read_excel('Play_marketplace')
        banner_content = []
        for inner_list in banner:
            banner_content.append(inner_list[0])
        self.assertTrue(cntry.verify_marketplace_tutorial(banner_content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_043")
    def test_verify_marketplace_game(self):
        cntry = marketplace(self.driver)
        banner = read_excel('Austraila_Market_Game')
        content = []
        for inner_list in banner:
            content.append(inner_list[0])
        self.assertTrue(cntry.verify_marketplace_Game(content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_046")
    def test_verify_marketplace_game_result(self):
        cntry = marketplace(self.driver)
        banner = read_excel('Austraila_Market_Game')
        content = []
        for inner_list in banner:
            content.append(inner_list[0])
        self.assertTrue(cntry.verify_marketplace_Game_result(content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_048")
    def test_verify_marketplace_game_result_welldone(self):
        cntry = marketplace(self.driver)
        banner = read_excel('Austraila_Market_Game')
        content = []
        for inner_list in banner:
            content.append(inner_list[0])
        self.assertTrue(cntry.verify_marketplace_Game_result_welldone(content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_049")
    def test_verify_marketplace_game_result_percentage(self):
        cntry = marketplace(self.driver)
        banner = read_excel('Austraila_Market_Game')
        content = []
        for inner_list in banner:
            content.append(inner_list[0])
        self.assertTrue(cntry.verify_marketplace_Game_result_percentage(content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_050")
    def test_verify_marketplace_game_summary_message(self):
        cntry = marketplace(self.driver)
        banner = read_excel('Austraila_Market_Game')
        content = []
        for inner_list in banner:
            content.append(inner_list[0])
        self.assertTrue(cntry.verify_marketplace_Game_result_summary(content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_051")
    def test_verify_marketplace_game_result_done(self):
        cntry = marketplace(self.driver)
        banner = read_excel('Austraila_Market_Game')
        content = []
        for inner_list in banner:
            content.append(inner_list[0])
        self.assertTrue(cntry.verify_marketplace_Game_done(content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_039")
    def test_verify_marketplace_game_header(self):
        cntry = marketplace(self.driver)
        banner = read_excel('Austraila_Market_Game')
        content = []
        for inner_list in banner:
            content.append(inner_list[0])
        self.assertTrue(cntry.verify_marketplace_Game_header(content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_038")
    def test_verify_marketplace_game_titile(self):
        cntry = marketplace(self.driver)
        banner = read_excel('Austraila_Market_Game')
        content = []
        for inner_list in banner:
            content.append(inner_list[0])
        self.assertTrue(cntry.verify_marketplace_Game_titile(content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BT_TC_P3_033")
    def test_verify_marketplace_game_clock(self):
        cntry = marketplace(self.driver)
        banner = read_excel('Austraila_Market_Game')
        content = []
        for inner_list in banner:
            content.append(inner_list[0])
        self.assertTrue(cntry.verify_marketplace_Game_clock(content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_052")
    def test_verify_marketplace_progress(self):
        cntry = marketplace(self.driver)
        banner = read_excel('Austraila_Market_Game')
        content = []
        for inner_list in banner:
            content.append(inner_list[0])
        self.assertTrue(cntry.verify_marketplace_progess(content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_052")
    def test_verify_marketplace_currency(self):
        cntry = marketplace(self.driver)
        banner = read_excel('Austraila_Market_Game')
        content = []
        for inner_list in banner:
            content.append(inner_list[0])
        self.assertTrue(cntry.verify_marketplace_currency(content))

