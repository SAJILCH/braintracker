import softest
import pytest
from flaky import flaky

from tests.base_test import BaseTests
from screens.Checkin import *
from utilities.ReadExcel import *
from utilities.Utils import PageUtils


class checkin_test(BaseTests, softest.TestCase):
    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_013")
    def test_verify_visiblity_of_checkin(self):
        cntry = checkin(self.driver)
        description = PageUtils.read_datas_from_excel(self.driver,'OnboardScreen', 'A12')
        self.assertTrue(cntry.verify_checkin_landing(description))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_014")
    def test_verify_checkin_game(self):
        cntry = checkin(self.driver)
        # self.assertTrue(cntry.verify_checkin_game(description))
        Quiz = read_excel('Austraila_checkin')
        quiz_questions = []
        quiz_answer = []
        for inner_list in Quiz:
            quiz_questions.append(inner_list[0])
        for inner_list in Quiz:
            quiz_answer.append(inner_list[1])
        self.assertTrue(cntry.verify_checkin_game(quiz_questions, quiz_answer))

    """@flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.describe("Test case Id - BP_TC_015")
    def test_verify_checkin_game_result(self):
        cntry = checkin(self.driver)
        # self.assertTrue(cntry.verify_checkin_game(description))
        Quiz = read_excel('Austraila_checkin')
        quiz_questions = []
        quiz_answer = []
        quiz_Insight = []
        quiz_Recommentation = []
        for inner_list in Quiz:
            quiz_questions.append(inner_list[0])
        for inner_list in Quiz:
            quiz_answer.append(inner_list[1])
        for inner_list in Quiz:
            quiz_Insight.append(inner_list[2])
        for inner_list in Quiz:
            quiz_Recommentation.append(inner_list[3])
        self.assertTrue(cntry.verify_checkin_results(quiz_questions, quiz_answer, quiz_Insight, quiz_Recommentation))"""

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_037")
    def test_verify_checkin_game_progress(self):
        cntry = checkin(self.driver)
        Quiz = read_excel('Austraila_checkin')
        quiz_questions = []
        quiz_answer = []
        for inner_list in Quiz:
            quiz_questions.append(inner_list[0])
        for inner_list in Quiz:
            quiz_answer.append(inner_list[1])
        self.assertTrue(cntry.verify_checkin_game_progress(quiz_questions, quiz_answer))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_044")
    def test_verify_checkin_pdf_export(self):
        cntry = checkin(self.driver)
        Quiz = read_excel('Austraila_checkin')
        quiz_questions = []
        quiz_answer = []
        for inner_list in Quiz:
            quiz_questions.append(inner_list[0])
        for inner_list in Quiz:
            quiz_answer.append(inner_list[1])
        self.assertTrue(cntry.verify_checkin_game_generatepdf(quiz_questions, quiz_answer))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BT_TC_P3_023")
    def test_verify_checkin_game_clock(self):
        cntry = checkin(self.driver)
        # self.assertTrue(cntry.verify_checkin_game(description))
        Quiz = read_excel('Austraila_checkin')
        quiz_questions = []
        quiz_answer = []
        for inner_list in Quiz:
            quiz_questions.append(inner_list[0])
        for inner_list in Quiz:
            quiz_answer.append(inner_list[1])
        self.assertTrue(cntry.verify_checkin_game_clock(quiz_questions, quiz_answer))
