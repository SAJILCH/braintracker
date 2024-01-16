import softest
import pytest
from flaky import flaky

from tests.base_test import BaseTests
from screens.HomePage import *
from utilities.ReadExcel import *


class homepage_test(BaseTests, softest.TestCase):
    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_BT_P4_001")
    def test_verify_visiblity_of_how_to_play(self):
        home = homepage(self.driver)
        self.assertFalse(home.how_to_play_button_removed())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_BT_P4_003")
    def test_verfiy_start_your_journey(self):
        home = homepage(self.driver)
        self.assertTrue(home.start_your_journey_validation())

    def test(self):
        home = homepage(self.driver)
        home.test()

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_010")
    def test_verfiy_country_and_playnow(self):
        home = homepage(self.driver)
        self.assertTrue(home.verify_playnow_button())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_011")
    def test_verfiy_homepage_icons(self):
        home = homepage(self.driver)
        self.assertTrue(home.verify_homepage_menu())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_P1_045")
    def test_verfiy_sound_and_haptics_settings(self):
        home = homepage(self.driver)
        self.assertTrue(home.verify_sound_and_haptics_settings())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_P1_036")
    def test_verfiy_progress_default(self):
        home = homepage(self.driver)
        self.assertTrue(home.verify_progress_default())

    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_P1_043")
    def test_verfiy_information_content(self):
        home = homepage(self.driver)
        data = read_excel('Information')
        content = []
        quiz_answer = []
        for inner_list in data:
            content.append(inner_list[0])
        self.assertTrue(home.verify_information_page(content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -TC_P2_010")
    def test_verfiy_developer_settings(self):
        home = homepage(self.driver)
        self.assertTrue(home.verify_settings_devlopermode())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_P1_043")
    def test_verfiy_country_based_settings(self):
        home = homepage(self.driver)
        pwd = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'A23')
        self.assertTrue(home.verify_countrybased_Settings(pwd))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_011")
    def test_verfiy_setting_page_unlocked(self):
        home = homepage(self.driver)
        pwd = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'A23')
        self.assertTrue(home.verify_settings_unlock(pwd))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_013")
    def test_verfiy_setting_tester_Access(self):
        home = homepage(self.driver)
        pwd = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'A23')
        self.assertTrue(home.verify_settings_tester_access_toggle(pwd))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BT_TC_P3_036")
    def test_clock_displayin_progress(self):
        home = homepage(self.driver)
        self.assertTrue(home.verify_clockin_progress())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BT_TC_P3_037")
    def test_clock_displayin_information(self):
        home = homepage(self.driver)
        self.assertTrue(home.verify_clockin_information())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BT_TC_P3_038")
    def test_clock_displayin_settings(self):
        home = homepage(self.driver)
        self.assertTrue(home.verify_clockin_settings())
