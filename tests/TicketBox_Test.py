import softest
import pytest
from flaky import flaky

from tests.base_test import BaseTests
from screens.TicketBox import *
from utilities.ReadExcel import *
from utilities.Utils import PageUtils


class ticketbox_test(BaseTests, softest.TestCase):
    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -TC_P2_055")
    def test_verify_ticketbox_homepage(self):
        travel = ticketbox(self.driver)
        description = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'A44')
        self.assertTrue(travel.verify_ticketbox_landing(description))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_056")
    def test_verify_ticketbox_tutorial(self):
        travel = ticketbox(self.driver)
        banner = read_excel('Ticketbox_tutorial')
        banner_content = []
        for inner_list in banner:
            banner_content.append(inner_list[0])
        print(banner_content)
        self.assertTrue(travel.verify_ticketbox_tutorial(banner_content))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -  TC_P2_111")
    def test_verify_ticketbox_game(self):
        travel = ticketbox(self.driver)
        banner = read_excel('Austraila_Ticketbox')
        content = []
        row = []
        seat = []
        for inner_list in banner:
            content.append(inner_list[0])
            row.append(inner_list[1])
            seat.append(inner_list[2])
        print(content)
        print(row[0])
        print(seat[0])
        self.assertTrue(travel.verify_ticketbox_game(content, row, seat))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id -  TC_P2_112")
    def test_verify_ticketbox_game_titile(self):
        travel = ticketbox(self.driver)
        banner = read_excel('Austraila_Ticketbox')
        content = []
        row = []
        seat = []
        for inner_list in banner:
            content.append(inner_list[0])
            row.append(inner_list[1])
            seat.append(inner_list[2])
        print(content)
        print(row[0])
        print(seat[0])
        self.assertTrue(travel.verify_ticketbox_game_titile(content, row, seat))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_113")
    def test_verify_ticketbox_game_pause(self):
        travel = ticketbox(self.driver)
        banner = read_excel('Austraila_Ticketbox')
        content = []
        row = []
        seat = []
        for inner_list in banner:
            content.append(inner_list[0])
            row.append(inner_list[1])
            seat.append(inner_list[2])
        print(content)
        print(row[0])
        print(seat[0])
        self.assertTrue(travel.verify_ticketbox_game_pause(content, row, seat))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_114")
    def test_verify_ticketbox_game_restart(self):
        travel = ticketbox(self.driver)
        banner = read_excel('Austraila_Ticketbox')
        content = []
        row = []
        seat = []
        for inner_list in banner:
            content.append(inner_list[0])
            row.append(inner_list[1])
            seat.append(inner_list[2])
        print(content)
        print(row[0])
        print(seat[0])
        self.assertTrue(travel.verify_ticketbox_game_restart(content, row, seat))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_P2_115")
    def test_verify_ticketbox_game_resume(self):
        travel = ticketbox(self.driver)
        banner = read_excel('Austraila_Ticketbox')
        content = []
        row = []
        seat = []
        for inner_list in banner:
            content.append(inner_list[0])
            row.append(inner_list[1])
            seat.append(inner_list[2])
        print(content)
        print(row[0])
        print(seat[0])
        self.assertTrue(travel.verify_ticketbox_game_resume(content, row, seat))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BT_TC_P3_026")
    def test_verify_ticketbox_clock(self):
        travel = ticketbox(self.driver)
        banner = read_excel('Austraila_Ticketbox')
        content = []
        row = []
        seat = []
        for inner_list in banner:
            content.append(inner_list[0])
            row.append(inner_list[1])
            seat.append(inner_list[2])
        print(content)
        print(row[0])
        print(seat[0])
        self.assertTrue(travel.verify_ticketbox_clock(content, row, seat))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BT_TC_P3_026")
    def test_verify_ticketbox_progress(self):
        travel = ticketbox(self.driver)
        banner = read_excel('Austraila_Ticketbox')
        content = []
        row = []
        seat = []
        for inner_list in banner:
            content.append(inner_list[0])
            row.append(inner_list[1])
            seat.append(inner_list[2])
        print(content)
        print(row[0])
        print(seat[0])
        self.assertTrue(travel.verify_ticketbox_progress(content, row, seat))