import softest
import pytest
from flaky import flaky

from tests.base_test import BaseTests
from screens.OnboardScreen import *
from utilities.Utils import *


class onboard_test(BaseTests, softest.TestCase):
    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_BT_P4_001")
    def test_verify_homepage_titiles(self):
        onboard = onboardscreen(self.driver)
        msg1 = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'A2')
        msg2 = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'B2')
        msg3 = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'C2')
        msg4 = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'D2')
        msg5 = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'E2')
        self.assertTrue(onboard.verify_onboardscreen(msg1, msg2, msg3, msg4, msg5))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_BT_P4_001")
    def test_verify_helpour_research(self):
        onboard = onboardscreen(self.driver)
        help_research = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'A6')
        self.assertTrue(onboard.verify_help_our_research_screen(help_research))

    def test_accesibilty(self):
        onboard = onboardscreen(self.driver)
        onboard.settings()