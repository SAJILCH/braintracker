import softest
import pytest
from flaky import flaky

from tests.base_test import BaseTests
from screens.SnapShot import *
from utilities.ReadExcel import *
from utilities.Utils import PageUtils


class snapshot_test(BaseTests, softest.TestCase):
    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -TC_P2_092")
    def test_verify_snapshot_homepage(self):
        travel = snapshot(self.driver)
        description = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'A41')
        travel.verify_snapshot_landing(description)

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_093")
    def test_verify_snapshot_tutorial(self):
        travel = snapshot(self.driver)
        banner = read_excel('Snapshot_tutorial')
        banner_content = []
        for inner_list in banner:
            banner_content.append(inner_list[0])
        print(banner_content)
        self.assertTrue(travel.verify_snapshot_tutorial(banner_content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_094")
    def test_verify_snapshot_tutorial_close(self):
        snap_shot = snapshot(self.driver)
        self.assertTrue(snap_shot.verify_snapshot_tutorial_close())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_095")
    def test_verify_snapshot_tutorial_content(self):
        snap_shot = snapshot(self.driver)
        banner = read_excel('Snapshot_tutorial')
        banner_content = []
        for inner_list in banner:
            banner_content.append(inner_list[0])
        self.assertTrue(snap_shot.verify_snapshot_tutorial_content(banner_content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_096")
    def test_verify_snapshot_game(self):
        snap_shot = snapshot(self.driver)
        self.assertTrue(snap_shot.verify_snapshot_game())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_097")
    def test_verify_snapshot_game_close(self):
        snap_shot = snapshot(self.driver)
        description = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'A41')
        self.assertTrue(snap_shot.verify_snapshot_game_close(description))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_097")
    def test_verify_snapshot_game_titile(self):
        snap_shot = snapshot(self.driver)
        self.assertTrue(snap_shot.verify_snapshot_game_titile())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_097")
    def test_verify_snapshot_progress(self):
        snap_shot = snapshot(self.driver)
        self.assertTrue(snap_shot.verify_snapshot_progress())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_105")
    def test_verify_snapshot_quit(self):
        snap_shot = snapshot(self.driver)
        self.assertTrue(snap_shot.verify_snapshot_Quit())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_106")
    def test_verify_snapshot_resart(self):
        snap_shot = snapshot(self.driver)
        self.assertTrue(snap_shot.verify_snapshot_restart())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_107")
    def test_verify_snapshot_resume(self):
        snap_shot = snapshot(self.driver)
        self.assertTrue(snap_shot.verify_snapshot_resume())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_104")
    def test_verify_snapshot_resultcomponet(self):
        snap_shot = snapshot(self.driver)
        self.assertTrue(snap_shot.verify_snapshot_resultscreen_componets())

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BT_TC_P3_025")
    def test_verify_snapshot_clock(self):
        snap_shot = snapshot(self.driver)
        self.assertTrue(snap_shot.verify_snapshot_clock())